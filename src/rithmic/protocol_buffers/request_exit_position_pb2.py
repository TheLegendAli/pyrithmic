# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request_exit_position.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='request_exit_position.proto',
  package='rti',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1brequest_exit_position.proto\x12\x03rti\"\xbe\x02\n\x13RequestExitPosition\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x12\n\x08user_msg\x18\x98\x8d\x08 \x03(\t\x12\x15\n\x0bwindow_name\x18\x85\xb8\t \x01(\t\x12\x10\n\x06\x66\x63m_id\x18\x9d\xb3\t \x01(\t\x12\x0f\n\x05ib_id\x18\x9e\xb3\t \x01(\t\x12\x14\n\naccount_id\x18\x98\xb3\t \x01(\t\x12\x10\n\x06symbol\x18\x94\xdc\x06 \x01(\t\x12\x12\n\x08\x65xchange\x18\x95\xdc\x06 \x01(\t\x12\x1b\n\x11trading_algorithm\x18\xca\xb8\t \x01(\t\x12\x41\n\x0emanual_or_auto\x18\xd6\xb8\t \x01(\x0e\x32\'.rti.RequestExitPosition.OrderPlacement\"&\n\x0eOrderPlacement\x12\n\n\x06MANUAL\x10\x01\x12\x08\n\x04\x41UTO\x10\x02'
)



_REQUESTEXITPOSITION_ORDERPLACEMENT = _descriptor.EnumDescriptor(
  name='OrderPlacement',
  full_name='rti.RequestExitPosition.OrderPlacement',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MANUAL', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUTO', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=317,
  serialized_end=355,
)
_sym_db.RegisterEnumDescriptor(_REQUESTEXITPOSITION_ORDERPLACEMENT)


_REQUESTEXITPOSITION = _descriptor.Descriptor(
  name='RequestExitPosition',
  full_name='rti.RequestExitPosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.RequestExitPosition.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_msg', full_name='rti.RequestExitPosition.user_msg', index=1,
      number=132760, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='window_name', full_name='rti.RequestExitPosition.window_name', index=2,
      number=154629, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fcm_id', full_name='rti.RequestExitPosition.fcm_id', index=3,
      number=154013, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ib_id', full_name='rti.RequestExitPosition.ib_id', index=4,
      number=154014, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='rti.RequestExitPosition.account_id', index=5,
      number=154008, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='rti.RequestExitPosition.symbol', index=6,
      number=110100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='rti.RequestExitPosition.exchange', index=7,
      number=110101, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trading_algorithm', full_name='rti.RequestExitPosition.trading_algorithm', index=8,
      number=154698, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='manual_or_auto', full_name='rti.RequestExitPosition.manual_or_auto', index=9,
      number=154710, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUESTEXITPOSITION_ORDERPLACEMENT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=355,
)

_REQUESTEXITPOSITION.fields_by_name['manual_or_auto'].enum_type = _REQUESTEXITPOSITION_ORDERPLACEMENT
_REQUESTEXITPOSITION_ORDERPLACEMENT.containing_type = _REQUESTEXITPOSITION
DESCRIPTOR.message_types_by_name['RequestExitPosition'] = _REQUESTEXITPOSITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestExitPosition = _reflection.GeneratedProtocolMessageType('RequestExitPosition', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTEXITPOSITION,
  '__module__' : 'request_exit_position_pb2'
  # @@protoc_insertion_point(class_scope:rti.RequestExitPosition)
  })
_sym_db.RegisterMessage(RequestExitPosition)


# @@protoc_insertion_point(module_scope)