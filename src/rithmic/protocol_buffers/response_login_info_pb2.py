# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_login_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_login_info.proto',
  package='rti',
  serialized_pb=_b('\n\x19response_login_info.proto\x12\x03rti\"\xb1\x02\n\x11ResponseLoginInfo\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x12\n\x08user_msg\x18\x98\x8d\x08 \x03(\t\x12\x11\n\x07rp_code\x18\x9e\x8d\x08 \x03(\t\x12\x10\n\x06\x66\x63m_id\x18\x9d\xb3\t \x01(\t\x12\x0f\n\x05ib_id\x18\x9e\xb3\t \x01(\t\x12\x14\n\nfirst_name\x18\xe8\xb4\t \x01(\t\x12\x13\n\tlast_name\x18\xe9\xb4\t \x01(\t\x12\x34\n\tuser_type\x18\xb4\xb3\t \x01(\x0e\x32\x1f.rti.ResponseLoginInfo.UserType\"Z\n\x08UserType\x12\x13\n\x0fUSER_TYPE_ADMIN\x10\x00\x12\x11\n\rUSER_TYPE_FCM\x10\x01\x12\x10\n\x0cUSER_TYPE_IB\x10\x02\x12\x14\n\x10USER_TYPE_TRADER\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_RESPONSELOGININFO_USERTYPE = _descriptor.EnumDescriptor(
  name='UserType',
  full_name='rti.ResponseLoginInfo.UserType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER_TYPE_ADMIN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_TYPE_FCM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_TYPE_IB', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_TYPE_TRADER', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=250,
  serialized_end=340,
)
_sym_db.RegisterEnumDescriptor(_RESPONSELOGININFO_USERTYPE)


_RESPONSELOGININFO = _descriptor.Descriptor(
  name='ResponseLoginInfo',
  full_name='rti.ResponseLoginInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.ResponseLoginInfo.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_msg', full_name='rti.ResponseLoginInfo.user_msg', index=1,
      number=132760, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rp_code', full_name='rti.ResponseLoginInfo.rp_code', index=2,
      number=132766, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fcm_id', full_name='rti.ResponseLoginInfo.fcm_id', index=3,
      number=154013, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ib_id', full_name='rti.ResponseLoginInfo.ib_id', index=4,
      number=154014, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='rti.ResponseLoginInfo.first_name', index=5,
      number=154216, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='rti.ResponseLoginInfo.last_name', index=6,
      number=154217, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_type', full_name='rti.ResponseLoginInfo.user_type', index=7,
      number=154036, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESPONSELOGININFO_USERTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=340,
)

_RESPONSELOGININFO.fields_by_name['user_type'].enum_type = _RESPONSELOGININFO_USERTYPE
_RESPONSELOGININFO_USERTYPE.containing_type = _RESPONSELOGININFO
DESCRIPTOR.message_types_by_name['ResponseLoginInfo'] = _RESPONSELOGININFO

ResponseLoginInfo = _reflection.GeneratedProtocolMessageType('ResponseLoginInfo', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSELOGININFO,
  __module__ = 'response_login_info_pb2'
  # @@protoc_insertion_point(class_scope:rti.ResponseLoginInfo)
  ))
_sym_db.RegisterMessage(ResponseLoginInfo)


# @@protoc_insertion_point(module_scope)