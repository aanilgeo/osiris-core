import sys
sys.path.append('C:/Users/harsh/osiris-core/cli/core/proto')
from concurrent import futures
import grpc
import time

import osiris_pb2
import osiris_pb2_grpc

# Acts as an in-memory storage for the lifecycle of each function
functions = {}

class OsirisServicer(osiris_pb2_grpc.OsirisServiceServicer):

    def DeployFunction(self, request, context):
        if request.function_name not in functions:
            functions[request.function_name] = {
                'path': request.path_to_function_code,
                'runtime': request.runtime_environment,
                'status': 'deployed'
            }
            return osiris_pb2.DeployResponse(success=True, message=f'Function {request.function_name} deployed successfully.')
        return osiris_pb2.DeployResponse(success=False, message=f'Function {request.function_name} already exists.')

    def UpdateFunction(self, request, context):
        if request.function_name in functions:
            functions[request.function_name]['path'] = request.path_to_function_code
            return osiris_pb2.UpdateResponse(success=True, message=f'Function {request.function_name} updated successfully.')
        return osiris_pb2.UpdateResponse(success=False, message=f'Function {request.function_name} not found.')

    def RemoveFunction(self, request, context):
        if request.function_name in functions:
            del functions[request.function_name]
            return osiris_pb2.RemoveResponse(success=True, message=f'Function "{request.function_name}" removed successfully.')
        return osiris_pb2.RemoveResponse(success=False, message=f'Function "{request.function_name}" not found.')

    def ListFunctions(self, request, context):
        for name, info in functions.items():
            yield osiris_pb2.FunctionInfo(function_name=name, runtime=info['runtime'], status=info['status'])

    def DescribeFunction(self, request, context):
        if request.function_name in functions:
            info = functions[request.function_name]
            return osiris_pb2.DescribeResponse(
                function_name=request.function_name,
                runtime=info['runtime'],
                status=info['status']
            )
        return osiris_pb2.DescribeResponse(function_name=request.function_name, runtime="", status="not found")

    def GetLogs(self, request, context):
        if request.name in functions:
            logs = ["Log entry 1", "Log entry 2"]
            for log in logs:
                yield osiris_pb2.LogEntry(message=log)
        else:
            yield osiris_pb2.LogEntry(message=f"No logs found for function '{request.name}'")

    def MonitorFunction(self, request, context):
        if request.name in functions:
            return osiris_pb2.MonitorResponse(
                cpu_usage="10%",
                memory_usage="20MB",
                execution_time="0.5ms"
            )
        return osiris_pb2.MonitorResponse(cpu_usage="", memory_usage="", execution_time="")

    def StartPlatform(self, request, context):
        return osiris_pb2.StartResponse(message="Osiris platform started successfully.")

    def StopPlatform(self, request, context):
        return osiris_pb2.StopResponse(message="Osiris platform stopped successfully.")

# Main function to start the server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    osiris_pb2_grpc.add_OsirisServiceServicer_to_server(OsirisServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started at port 50051")
    try:
        while True:
            time.sleep(86400)  # Server will keep running, refreshing every 24 hours
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()