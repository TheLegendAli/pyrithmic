import asyncio
import logging
import time
import websockets
from datetime import datetime as dt
from typing import Union, Tuple, Callable, Dict

import pandas as pd
import pytz
from pandas import NaT

from rithmic import RithmicEnvironment, CallbackManager, CallbackId
from rithmic.interfaces.base import RithmicBaseApi, SHARED_RESPONSE_MAP
from rithmic.protocol_buffers import request_login_pb2, request_pnl_position_updates_pb2
from rithmic.protocol_buffers.instrument_pnl_position_update_pb2 import InstrumentPnLPositionUpdate
from rithmic.protocol_buffers.account_pnl_position_update_pb2 import AccountPnLPositionUpdate


from rithmic.tools.general import dict_destructure, get_utc_now
from rithmic.tools.meta import ApiType
from rithmic.tools.pyrithmic_exceptions import (
    NoValidTradingAccountException, NoValidTradeRouteException, NoTradingConfigException, WebsocketClosedException,
)
from rithmic.tools.pyrithmic_logger import logger, configure_logging
from rithmic.tools.pyrithmic_exceptions import WebsocketClosedException, MissingCustomCallback

# Mapping of Template ID to the proto to use and the internal method used to process this message type
CONSUMPTION_RESPONSE_MAP = {
    450: dict(proto=InstrumentPnLPositionUpdate, fn='_process_instrument_pnl'),
    451: dict(proto=AccountPnLPositionUpdate, fn='_process_account_pnl'),
}
CONSUMPTION_RESPONSE_MAP.update(SHARED_RESPONSE_MAP)



class RithmicPnlApi(RithmicBaseApi):
    """
    Rithmic PnL API For the PnL PLANT to get PnL for account
    """
    infra_type = request_login_pb2.RequestLogin.SysInfraType.PNL_PLANT
    api_type = ApiType.HISTORY

    def __init__(self, env: RithmicEnvironment = None, callback_manager: CallbackManager = None,
                 auto_connect: bool = True, loop=None, periodic_sync_interval_seconds: float = 0.1,
                 fcm_id: str = None, ib_id: str = None, user_type: str = None, accounts: list = None,
                 primary_account_id: str = None):
        """
        Rithmic History API to download historical tick data

        :param env: (RithmicEnvironment) provide a rithmic environment to connect to, if omitted, tries to get the
                    default environment from the Environment Variable RITHMIC_ENVIRONMENT_NAME
        :param auto_connect: (bool) automatically connect and log into Rithmic, defaults to True
        :param callback_manager: (CallbackManager) provide a configured manager with callbacks registered
        :param loop: (AbstractEventLoop) asyncio event loop can be provided to share/use existing loop
        :param periodic_sync_interval_seconds: (float) interval in seconds to sync with Rithmic, defaults to 0.1
        """
        self.subscribed_for_updates = False
        self._consuming_updates = False
        self.fcm_id = fcm_id
        self.ib_id = ib_id
        self.user_type = user_type
        self.accounts = accounts
        self.primary_account_id = primary_account_id
        self.set_account_pnl()
        self.primary_account_info = self.account_pnl[self.primary_account_id]
        self.instrument_pnl = {}
        RithmicBaseApi.__init__(self, env, callback_manager, auto_connect, loop)
        
      
    def set_account_pnl(self) -> None:
        self.account_pnl = {}
        for account in self.accounts:
            self.account_pnl[account] = {
                'template_id': None,
                'ssboe': None, 
                'usecs': None, 
                'update_time': None,
                'account_id': None,
                'fcm_id': None,
                'ib_id': None,
                'order_buy_qty': None,
                'order_sell_qty': None,
                'fill_buy_qty': None,
                'fill_sell_qty': None,
                'buy_qty': None,
                'sell_qty': None,
                'mtm_account': None,
                'open_position_pnl': None,
                'open_position_quantity': None,
                'closed_position_pnl': None,
                'closed_position_quantity': None,
                'percent_maximum_allowable_loss': None,
                'net_quantity': None,
                'min_account_balance': None,
                'account_balance': None,
                'cash_on_hand': None,
                'min_margin_balance': None,
                'margin_balance': None,
                'excess_buy_margin': None,
                'excess_sell_margin': None,
                'reserved_buying_power': None,
                'used_buying_power': None,
                'available_buying_power': None,
                'open_long_options_value': None,
                'open_short_options_value': None,
                'closed_options_value': None,
                'option_cash_reserved': None,
                'option_open_pnl': None,
                'option_closed_pnl': None,
                'day_open_pnl': None,
                'day_closed_pnl': None,
                'day_pnl': None,
                'day_open_pnl_offset': None,
                'day_closed_pnl_offset': None,
            }

    
    def get_account_pnl(self, account_id: str) -> dict:
        """
        Get the account pnl for a specific account

        :param account_id: (str) account id to get pnl for
        :return: (dict) account pnl data
        """
        return self.account_pnl[account_id]


    def get_primary_account_pnl(self) -> dict:
        """
        Get the account pnl for the primary account

        :return: (dict) account pnl data
        """
        return self.primary_account_info
    
    def get_instrument_pnl(self, symbol: str) -> dict:
        """
        Get the instrument pnl for a specific symbol

        :param symbol: (str) symbol to get pnl for
        :return: (dict) instrument pnl data
        """
        return self.instrument_pnl[symbol]
    
    def connect_and_login(self) -> None:
        """Connects, Logs in to Rithmic and subscribes to updates"""
        logged_in = super(RithmicPnlApi, self).connect_and_login()
        self._run_update_subscription()
        
    def _set_periodic_sync_interval(self, seconds: float):
        """
        Sets the interval for periodic syncing and starts the processing callback if registered

        :param seconds: (float) number of seconds between processing new data
        :return:
        """
        self.periodic_sync_interval_seconds = seconds
        self._register_periodic_sync()

    def _register_periodic_sync(self) -> None:
        """
        Starts the periodic syncing callback for asynchronous processing
        :return: None
        """
        has_sync_callback = self.callback_manager.get_callback_by_callback_id(
            CallbackId.ACCOUNT_PNL)
        if has_sync_callback:
            asyncio.run_coroutine_threadsafe(self.periodic_syncing(), loop=self.loop)
    
    def _run_update_subscription(self) -> None:
        """Check config and start consumption process"""
        self._check_update_status()
        if self._consuming_updates is False:
            asyncio.run_coroutine_threadsafe(self._consume_subscription(), self.loop)
    
    async def _consume_subscription(self) -> None:
        """
        Consumes new messages as data is streamed, sends a heartbeat if no data received after 5 seconds and
        the websocket is still open. Starts once api is connected and logged in.

        :return: None
        """
        connected = True
        self.consuming_subscription = True
        await self.send_heartbeat()
        while connected:
            msg_buf = bytearray()
            waiting_for_msg = True
            while waiting_for_msg:
                try:
                    logger.debug('Waiting for msg...')
                    msg_buf = await asyncio.wait_for(self.recv_buffer(), timeout=5)
                    waiting_for_msg = False
                except asyncio.TimeoutError:
                    try:
                        # Send a ping to check if the connection is still alive
                        await self.ws.ping()
                    except websockets.ConnectionClosed:
                        print("Connection is closed.")
                        logger.info("connection appears to be closed.  exiting consume()")
                        raise WebsocketClosedException('Websocket has closed')
            template_id = self.get_template_id_from_message_buffer(msg_buf)
            if template_id == 19:
                continue
            if template_id == 13:
                connected = False
                continue
            else:
                self._process_new_message(template_id, msg_buf)

    def _process_new_message(self, template_id: int, msg_buf) -> Union[dict, None]:
        """
        Processes messages and routes based on template id

        :param template_id: (int) template id of the message
        :param msg_buf: (bytes) message received in bytes
        :return:
        """
        if template_id in CONSUMPTION_RESPONSE_MAP:
            meta = CONSUMPTION_RESPONSE_MAP[template_id]
            msg = meta['proto']()
            msg.ParseFromString(msg_buf[4:])
            fn = getattr(self, meta['fn'])
            result = fn(template_id, msg)
            callback_fn = self.callback_manager.get_callback_by_template_id(template_id)
            if callback_fn is not None:
                self.perform_callback(callback_fn, [result])
            return result
    
    def _process_account_pnl(self, template_id: int, msg: AccountPnLPositionUpdate) -> None:
        """
        Processes new tick data message as it streams in. 
        Save values to the dict

        :param template_id: (int) template id of the message received over the websocket
        :param msg: (LastTrade) protocol buffer message
        :return: None
        """
        data = self._get_row_information(template_id, msg)
        self.account_pnl[data['account_id']] = data
        if data['account_id'] == self.primary_account_id:
            self.primary_account_info = self.account_pnl[self.primary_account_id]

    def _process_instrument_pnl(self, template_id: int, msg: InstrumentPnLPositionUpdate):
        """
        Processes new instrumeeent pnl data message as it streams in.

        :param template_id: (int) template id of the message received over the websocket
        :param msg: (LastTrade) protocol buffer message
        """
        data = self._get_row_information(template_id, msg)
        self.instrument_pnl[data['symbol']] = data
    
    def _check_update_status(self):
        """Confirm everything is configured and subscription consumption requests sent"""
        if self.subscribed_for_updates is False:
            for account in self.accounts:
                asyncio.run_coroutine_threadsafe(
                    self._subscribe_to_pnl_stream(account_id = account), loop=self.loop
                )
            self.subsciribed_for_updates = True
    
    async def _subscribe_to_pnl_stream(self, account_id: str) -> None:
        """
        Creates request and sends to subscribe for a tick data stream

        :param account_id: (str) account id to subscribe to
        """
        rq = request_pnl_position_updates_pb2.RequestPnLPositionUpdates()
        rq.template_id = 400;
        rq.user_msg.append("hello")
        rq.request    = request_pnl_position_updates_pb2.RequestPnLPositionUpdates.Request.SUBSCRIBE
        rq.fcm_id     = self.fcm_id
        rq.ib_id      = self.ib_id
        rq.account_id = account_id
        buffer = self._convert_request_to_bytes(rq)
        await self.send_buffer(buffer)
        logger.info(f"Subscribed to PnL Stream for {account_id}")