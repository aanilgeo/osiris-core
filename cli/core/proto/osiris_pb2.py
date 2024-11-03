# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: osiris.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'osiris.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cosiris.proto\x12\x06osiris\"b\n\rDeployRequest\x12\x1d\n\x15path_to_function_code\x18\x01 \x01(\t\x12\x15\n\rfunction_name\x18\x02 \x01(\t\x12\x1b\n\x13runtime_environment\x18\x03 \x01(\t\"2\n\x0e\x44\x65ployResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"E\n\rUpdateRequest\x12\x15\n\rfunction_name\x18\x01 \x01(\t\x12\x1d\n\x15path_to_function_code\x18\x02 \x01(\t\"2\n\x0eUpdateResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"&\n\rRemoveRequest\x12\x15\n\rfunction_name\x18\x01 \x01(\t\"2\n\x0eRemoveResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\r\n\x0bListRequest\"7\n\x0cListResponse\x12\'\n\tfunctions\x18\x01 \x03(\x0b\x32\x14.osiris.FunctionInfo\"F\n\x0c\x46unctionInfo\x12\x15\n\rfunction_name\x18\x01 \x01(\t\x12\x0f\n\x07runtime\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\"(\n\x0f\x44\x65scribeRequest\x12\x15\n\rfunction_name\x18\x01 \x01(\t\"_\n\x10\x44\x65scribeResponse\x12\x15\n\rfunction_name\x18\x01 \x01(\t\x12\x0f\n\x07runtime\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65ployed_at\x18\x04 \x01(\t\"2\n\x0bLogsRequest\x12\x15\n\rfunction_name\x18\x01 \x01(\t\x12\x0c\n\x04tail\x18\x02 \x01(\x08\"\x1c\n\x0cLogsResponse\x12\x0c\n\x04logs\x18\x01 \x03(\t\"\'\n\x0eMonitorRequest\x12\x15\n\rfunction_name\x18\x01 \x01(\t\"i\n\x0fMonitorResponse\x12\x15\n\rfunction_name\x18\x01 \x01(\t\x12\x16\n\x0e\x65xecution_time\x18\x02 \x01(\t\x12\x11\n\tcpu_usage\x18\x03 \x01(\t\x12\x14\n\x0cmemory_usage\x18\x04 \x01(\t\"\x0e\n\x0cStartRequest\"1\n\rStartResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\r\n\x0bStopRequest\"0\n\x0cStopResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xc8\x04\n\rOsirisService\x12?\n\x0e\x44\x65ployFunction\x12\x15.osiris.DeployRequest\x1a\x16.osiris.DeployResponse\x12?\n\x0eUpdateFunction\x12\x15.osiris.UpdateRequest\x1a\x16.osiris.UpdateResponse\x12?\n\x0eRemoveFunction\x12\x15.osiris.RemoveRequest\x1a\x16.osiris.RemoveResponse\x12:\n\rListFunctions\x12\x13.osiris.ListRequest\x1a\x14.osiris.ListResponse\x12\x45\n\x10\x44\x65scribeFunction\x12\x17.osiris.DescribeRequest\x1a\x18.osiris.DescribeResponse\x12\x34\n\x07GetLogs\x12\x13.osiris.LogsRequest\x1a\x14.osiris.LogsResponse\x12\x42\n\x0fMonitorFunction\x12\x16.osiris.MonitorRequest\x1a\x17.osiris.MonitorResponse\x12<\n\rStartPlatform\x12\x14.osiris.StartRequest\x1a\x15.osiris.StartResponse\x12\x39\n\x0cStopPlatform\x12\x13.osiris.StopRequest\x1a\x14.osiris.StopResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osiris_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DEPLOYREQUEST']._serialized_start=24
  _globals['_DEPLOYREQUEST']._serialized_end=122
  _globals['_DEPLOYRESPONSE']._serialized_start=124
  _globals['_DEPLOYRESPONSE']._serialized_end=174
  _globals['_UPDATEREQUEST']._serialized_start=176
  _globals['_UPDATEREQUEST']._serialized_end=245
  _globals['_UPDATERESPONSE']._serialized_start=247
  _globals['_UPDATERESPONSE']._serialized_end=297
  _globals['_REMOVEREQUEST']._serialized_start=299
  _globals['_REMOVEREQUEST']._serialized_end=337
  _globals['_REMOVERESPONSE']._serialized_start=339
  _globals['_REMOVERESPONSE']._serialized_end=389
  _globals['_LISTREQUEST']._serialized_start=391
  _globals['_LISTREQUEST']._serialized_end=404
  _globals['_LISTRESPONSE']._serialized_start=406
  _globals['_LISTRESPONSE']._serialized_end=461
  _globals['_FUNCTIONINFO']._serialized_start=463
  _globals['_FUNCTIONINFO']._serialized_end=533
  _globals['_DESCRIBEREQUEST']._serialized_start=535
  _globals['_DESCRIBEREQUEST']._serialized_end=575
  _globals['_DESCRIBERESPONSE']._serialized_start=577
  _globals['_DESCRIBERESPONSE']._serialized_end=672
  _globals['_LOGSREQUEST']._serialized_start=674
  _globals['_LOGSREQUEST']._serialized_end=724
  _globals['_LOGSRESPONSE']._serialized_start=726
  _globals['_LOGSRESPONSE']._serialized_end=754
  _globals['_MONITORREQUEST']._serialized_start=756
  _globals['_MONITORREQUEST']._serialized_end=795
  _globals['_MONITORRESPONSE']._serialized_start=797
  _globals['_MONITORRESPONSE']._serialized_end=902
  _globals['_STARTREQUEST']._serialized_start=904
  _globals['_STARTREQUEST']._serialized_end=918
  _globals['_STARTRESPONSE']._serialized_start=920
  _globals['_STARTRESPONSE']._serialized_end=969
  _globals['_STOPREQUEST']._serialized_start=971
  _globals['_STOPREQUEST']._serialized_end=984
  _globals['_STOPRESPONSE']._serialized_start=986
  _globals['_STOPRESPONSE']._serialized_end=1034
  _globals['_OSIRISSERVICE']._serialized_start=1037
  _globals['_OSIRISSERVICE']._serialized_end=1621
# @@protoc_insertion_point(module_scope)
