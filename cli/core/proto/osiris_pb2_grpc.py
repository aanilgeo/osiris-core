# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import osiris_pb2 as osiris__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in osiris_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class OsirisServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DeployFunction = channel.unary_unary(
                '/osiris.OsirisService/DeployFunction',
                request_serializer=osiris__pb2.DeployRequest.SerializeToString,
                response_deserializer=osiris__pb2.DeployResponse.FromString,
                _registered_method=True)
        self.UpdateFunction = channel.unary_unary(
                '/osiris.OsirisService/UpdateFunction',
                request_serializer=osiris__pb2.UpdateRequest.SerializeToString,
                response_deserializer=osiris__pb2.UpdateResponse.FromString,
                _registered_method=True)
        self.RemoveFunction = channel.unary_unary(
                '/osiris.OsirisService/RemoveFunction',
                request_serializer=osiris__pb2.RemoveRequest.SerializeToString,
                response_deserializer=osiris__pb2.RemoveResponse.FromString,
                _registered_method=True)
        self.ListFunctions = channel.unary_unary(
                '/osiris.OsirisService/ListFunctions',
                request_serializer=osiris__pb2.ListRequest.SerializeToString,
                response_deserializer=osiris__pb2.ListResponse.FromString,
                _registered_method=True)
        self.DescribeFunction = channel.unary_unary(
                '/osiris.OsirisService/DescribeFunction',
                request_serializer=osiris__pb2.DescribeRequest.SerializeToString,
                response_deserializer=osiris__pb2.DescribeResponse.FromString,
                _registered_method=True)
        self.GetLogs = channel.unary_unary(
                '/osiris.OsirisService/GetLogs',
                request_serializer=osiris__pb2.LogsRequest.SerializeToString,
                response_deserializer=osiris__pb2.LogsResponse.FromString,
                _registered_method=True)
        self.MonitorFunction = channel.unary_unary(
                '/osiris.OsirisService/MonitorFunction',
                request_serializer=osiris__pb2.MonitorRequest.SerializeToString,
                response_deserializer=osiris__pb2.MonitorResponse.FromString,
                _registered_method=True)
        self.StartPlatform = channel.unary_unary(
                '/osiris.OsirisService/StartPlatform',
                request_serializer=osiris__pb2.StartRequest.SerializeToString,
                response_deserializer=osiris__pb2.StartResponse.FromString,
                _registered_method=True)
        self.StopPlatform = channel.unary_unary(
                '/osiris.OsirisService/StopPlatform',
                request_serializer=osiris__pb2.StopRequest.SerializeToString,
                response_deserializer=osiris__pb2.StopResponse.FromString,
                _registered_method=True)


class OsirisServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DeployFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFunctions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLogs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MonitorFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartPlatform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopPlatform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OsirisServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DeployFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.DeployFunction,
                    request_deserializer=osiris__pb2.DeployRequest.FromString,
                    response_serializer=osiris__pb2.DeployResponse.SerializeToString,
            ),
            'UpdateFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateFunction,
                    request_deserializer=osiris__pb2.UpdateRequest.FromString,
                    response_serializer=osiris__pb2.UpdateResponse.SerializeToString,
            ),
            'RemoveFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveFunction,
                    request_deserializer=osiris__pb2.RemoveRequest.FromString,
                    response_serializer=osiris__pb2.RemoveResponse.SerializeToString,
            ),
            'ListFunctions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFunctions,
                    request_deserializer=osiris__pb2.ListRequest.FromString,
                    response_serializer=osiris__pb2.ListResponse.SerializeToString,
            ),
            'DescribeFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeFunction,
                    request_deserializer=osiris__pb2.DescribeRequest.FromString,
                    response_serializer=osiris__pb2.DescribeResponse.SerializeToString,
            ),
            'GetLogs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLogs,
                    request_deserializer=osiris__pb2.LogsRequest.FromString,
                    response_serializer=osiris__pb2.LogsResponse.SerializeToString,
            ),
            'MonitorFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.MonitorFunction,
                    request_deserializer=osiris__pb2.MonitorRequest.FromString,
                    response_serializer=osiris__pb2.MonitorResponse.SerializeToString,
            ),
            'StartPlatform': grpc.unary_unary_rpc_method_handler(
                    servicer.StartPlatform,
                    request_deserializer=osiris__pb2.StartRequest.FromString,
                    response_serializer=osiris__pb2.StartResponse.SerializeToString,
            ),
            'StopPlatform': grpc.unary_unary_rpc_method_handler(
                    servicer.StopPlatform,
                    request_deserializer=osiris__pb2.StopRequest.FromString,
                    response_serializer=osiris__pb2.StopResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'osiris.OsirisService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('osiris.OsirisService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class OsirisService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DeployFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/osiris.OsirisService/DeployFunction',
            osiris__pb2.DeployRequest.SerializeToString,
            osiris__pb2.DeployResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/osiris.OsirisService/UpdateFunction',
            osiris__pb2.UpdateRequest.SerializeToString,
            osiris__pb2.UpdateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RemoveFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/osiris.OsirisService/RemoveFunction',
            osiris__pb2.RemoveRequest.SerializeToString,
            osiris__pb2.RemoveResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListFunctions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/osiris.OsirisService/ListFunctions',
            osiris__pb2.ListRequest.SerializeToString,
            osiris__pb2.ListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DescribeFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/osiris.OsirisService/DescribeFunction',
            osiris__pb2.DescribeRequest.SerializeToString,
            osiris__pb2.DescribeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetLogs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/osiris.OsirisService/GetLogs',
            osiris__pb2.LogsRequest.SerializeToString,
            osiris__pb2.LogsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def MonitorFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/osiris.OsirisService/MonitorFunction',
            osiris__pb2.MonitorRequest.SerializeToString,
            osiris__pb2.MonitorResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def StartPlatform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/osiris.OsirisService/StartPlatform',
            osiris__pb2.StartRequest.SerializeToString,
            osiris__pb2.StartResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def StopPlatform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/osiris.OsirisService/StopPlatform',
            osiris__pb2.StopRequest.SerializeToString,
            osiris__pb2.StopResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
