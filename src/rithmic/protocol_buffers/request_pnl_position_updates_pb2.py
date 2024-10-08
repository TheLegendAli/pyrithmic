# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request_pnl_position_updates.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='request_pnl_position_updates.proto',
  package='rti',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"request_pnl_position_updates.proto\x12\x03rti\"\xe5\x01\n\x19RequestPnLPositionUpdates\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x12\n\x08user_msg\x18\x98\x8d\x08 \x03(\t\x12\x39\n\x07request\x18\xa0\x8d\x06 \x01(\x0e\x32&.rti.RequestPnLPositionUpdates.Request\x12\x10\n\x06\x66\x63m_id\x18\x9d\xb3\t \x01(\t\x12\x0f\n\x05ib_id\x18\x9e\xb3\t \x01(\t\x12\x14\n\naccount_id\x18\x98\xb3\t \x01(\t\")\n\x07Request\x12\r\n\tSUBSCRIBE\x10\x01\x12\x0f\n\x0bUNSUBSCRIBE\x10\x02'
)



_REQUESTPNLPOSITIONUPDATES_REQUEST = _descriptor.EnumDescriptor(
  name='Request',
  full_name='rti.RequestPnLPositionUpdates.Request',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUBSCRIBE', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNSUBSCRIBE', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=232,
  serialized_end=273,
)
_sym_db.RegisterEnumDescriptor(_REQUESTPNLPOSITIONUPDATES_REQUEST)


_REQUESTPNLPOSITIONUPDATES = _descriptor.Descriptor(
  name='RequestPnLPositionUpdates',
  full_name='rti.RequestPnLPositionUpdates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.RequestPnLPositionUpdates.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_msg', full_name='rti.RequestPnLPositionUpdates.user_msg', index=1,
      number=132760, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request', full_name='rti.RequestPnLPositionUpdates.request', index=2,
      number=100000, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fcm_id', full_name='rti.RequestPnLPositionUpdates.fcm_id', index=3,
      number=154013, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ib_id', full_name='rti.RequestPnLPositionUpdates.ib_id', index=4,
      number=154014, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='rti.RequestPnLPositionUpdates.account_id', index=5,
      number=154008, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUESTPNLPOSITIONUPDATES_REQUEST,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=273,
)

_REQUESTPNLPOSITIONUPDATES.fields_by_name['request'].enum_type = _REQUESTPNLPOSITIONUPDATES_REQUEST
_REQUESTPNLPOSITIONUPDATES_REQUEST.containing_type = _REQUESTPNLPOSITIONUPDATES
DESCRIPTOR.message_types_by_name['RequestPnLPositionUpdates'] = _REQUESTPNLPOSITIONUPDATES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestPnLPositionUpdates = _reflection.GeneratedProtocolMessageType('RequestPnLPositionUpdates', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTPNLPOSITIONUPDATES,
  '__module__' : 'request_pnl_position_updates_pb2'
  # @@protoc_insertion_point(class_scope:rti.RequestPnLPositionUpdates)
  })
_sym_db.RegisterMessage(RequestPnLPositionUpdates)


# @@protoc_insertion_point(module_scope)
