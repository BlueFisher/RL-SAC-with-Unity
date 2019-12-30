# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: learner.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ndarray_pb2 as ndarray__pb2
import pingpong_pb2 as pingpong__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='learner.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rlearner.proto\x1a\rndarray.proto\x1a\x0epingpong.proto\"_\n\x10GetActionRequest\x12\x17\n\x05state\x18\x01 \x01(\x0b\x32\x08.NDarray\x12\x15\n\rhas_rnn_state\x18\x02 \x01(\x08\x12\x1b\n\trnn_state\x18\x03 \x01(\x0b\x32\x08.NDarray\"V\n\x06\x41\x63tion\x12\x18\n\x06\x61\x63tion\x18\x01 \x01(\x0b\x32\x08.NDarray\x12\x15\n\rhas_rnn_state\x18\x02 \x01(\x08\x12\x1b\n\trnn_state\x18\x03 \x01(\x0b\x32\x08.NDarray\".\n\x0fPolicyVariables\x12\x1b\n\tvariables\x18\x01 \x03(\x0b\x32\x08.NDarray\"2\n\x11GetTDErrorRequest\x12\x1d\n\x0btransitions\x18\x01 \x03(\x0b\x32\x08.NDarray\"%\n\x07TDError\x12\x1a\n\x08td_error\x18\x01 \x01(\x0b\x32\x08.NDarray\"-\n\x11PostRewardRequest\x12\x18\n\x06reward\x18\x01 \x01(\x0b\x32\x08.NDarray2\xe0\x01\n\x0eLearnerService\x12\x1f\n\x0bPersistence\x12\x05.Ping\x1a\x05.Pong(\x01\x30\x01\x12\'\n\tGetAction\x12\x11.GetActionRequest\x1a\x07.Action\x12.\n\x12GetPolicyVariables\x12\x06.Empty\x1a\x10.PolicyVariables\x12*\n\nGetTDError\x12\x12.GetTDErrorRequest\x1a\x08.TDError\x12(\n\nPostReward\x12\x12.PostRewardRequest\x1a\x06.Emptyb\x06proto3')
  ,
  dependencies=[ndarray__pb2.DESCRIPTOR,pingpong__pb2.DESCRIPTOR,])




_GETACTIONREQUEST = _descriptor.Descriptor(
  name='GetActionRequest',
  full_name='GetActionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='GetActionRequest.state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_rnn_state', full_name='GetActionRequest.has_rnn_state', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rnn_state', full_name='GetActionRequest.rnn_state', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=143,
)


_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='Action.action', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_rnn_state', full_name='Action.has_rnn_state', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rnn_state', full_name='Action.rnn_state', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=231,
)


_POLICYVARIABLES = _descriptor.Descriptor(
  name='PolicyVariables',
  full_name='PolicyVariables',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variables', full_name='PolicyVariables.variables', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=279,
)


_GETTDERRORREQUEST = _descriptor.Descriptor(
  name='GetTDErrorRequest',
  full_name='GetTDErrorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transitions', full_name='GetTDErrorRequest.transitions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=331,
)


_TDERROR = _descriptor.Descriptor(
  name='TDError',
  full_name='TDError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='td_error', full_name='TDError.td_error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=370,
)


_POSTREWARDREQUEST = _descriptor.Descriptor(
  name='PostRewardRequest',
  full_name='PostRewardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reward', full_name='PostRewardRequest.reward', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=417,
)

_GETACTIONREQUEST.fields_by_name['state'].message_type = ndarray__pb2._NDARRAY
_GETACTIONREQUEST.fields_by_name['rnn_state'].message_type = ndarray__pb2._NDARRAY
_ACTION.fields_by_name['action'].message_type = ndarray__pb2._NDARRAY
_ACTION.fields_by_name['rnn_state'].message_type = ndarray__pb2._NDARRAY
_POLICYVARIABLES.fields_by_name['variables'].message_type = ndarray__pb2._NDARRAY
_GETTDERRORREQUEST.fields_by_name['transitions'].message_type = ndarray__pb2._NDARRAY
_TDERROR.fields_by_name['td_error'].message_type = ndarray__pb2._NDARRAY
_POSTREWARDREQUEST.fields_by_name['reward'].message_type = ndarray__pb2._NDARRAY
DESCRIPTOR.message_types_by_name['GetActionRequest'] = _GETACTIONREQUEST
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.message_types_by_name['PolicyVariables'] = _POLICYVARIABLES
DESCRIPTOR.message_types_by_name['GetTDErrorRequest'] = _GETTDERRORREQUEST
DESCRIPTOR.message_types_by_name['TDError'] = _TDERROR
DESCRIPTOR.message_types_by_name['PostRewardRequest'] = _POSTREWARDREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetActionRequest = _reflection.GeneratedProtocolMessageType('GetActionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACTIONREQUEST,
  '__module__' : 'learner_pb2'
  # @@protoc_insertion_point(class_scope:GetActionRequest)
  })
_sym_db.RegisterMessage(GetActionRequest)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), {
  'DESCRIPTOR' : _ACTION,
  '__module__' : 'learner_pb2'
  # @@protoc_insertion_point(class_scope:Action)
  })
_sym_db.RegisterMessage(Action)

PolicyVariables = _reflection.GeneratedProtocolMessageType('PolicyVariables', (_message.Message,), {
  'DESCRIPTOR' : _POLICYVARIABLES,
  '__module__' : 'learner_pb2'
  # @@protoc_insertion_point(class_scope:PolicyVariables)
  })
_sym_db.RegisterMessage(PolicyVariables)

GetTDErrorRequest = _reflection.GeneratedProtocolMessageType('GetTDErrorRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTDERRORREQUEST,
  '__module__' : 'learner_pb2'
  # @@protoc_insertion_point(class_scope:GetTDErrorRequest)
  })
_sym_db.RegisterMessage(GetTDErrorRequest)

TDError = _reflection.GeneratedProtocolMessageType('TDError', (_message.Message,), {
  'DESCRIPTOR' : _TDERROR,
  '__module__' : 'learner_pb2'
  # @@protoc_insertion_point(class_scope:TDError)
  })
_sym_db.RegisterMessage(TDError)

PostRewardRequest = _reflection.GeneratedProtocolMessageType('PostRewardRequest', (_message.Message,), {
  'DESCRIPTOR' : _POSTREWARDREQUEST,
  '__module__' : 'learner_pb2'
  # @@protoc_insertion_point(class_scope:PostRewardRequest)
  })
_sym_db.RegisterMessage(PostRewardRequest)



_LEARNERSERVICE = _descriptor.ServiceDescriptor(
  name='LearnerService',
  full_name='LearnerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=420,
  serialized_end=644,
  methods=[
  _descriptor.MethodDescriptor(
    name='Persistence',
    full_name='LearnerService.Persistence',
    index=0,
    containing_service=None,
    input_type=pingpong__pb2._PING,
    output_type=pingpong__pb2._PONG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAction',
    full_name='LearnerService.GetAction',
    index=1,
    containing_service=None,
    input_type=_GETACTIONREQUEST,
    output_type=_ACTION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPolicyVariables',
    full_name='LearnerService.GetPolicyVariables',
    index=2,
    containing_service=None,
    input_type=ndarray__pb2._EMPTY,
    output_type=_POLICYVARIABLES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTDError',
    full_name='LearnerService.GetTDError',
    index=3,
    containing_service=None,
    input_type=_GETTDERRORREQUEST,
    output_type=_TDERROR,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PostReward',
    full_name='LearnerService.PostReward',
    index=4,
    containing_service=None,
    input_type=_POSTREWARDREQUEST,
    output_type=ndarray__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LEARNERSERVICE)

DESCRIPTOR.services_by_name['LearnerService'] = _LEARNERSERVICE

# @@protoc_insertion_point(module_scope)