from proto import osiris_pb2
from proto import osiris_pb2_grpc
from concurrent import futures
import grpc
import time

# Acts as an in-memory storage for the lifecycle of each function
functions = {}

class OsirisServicer(osiris_pb2_grpc.OsirisServicer):

    def DeployFunction(self, request, context):
        functions[request.name] = {
            'path': request.path_to_function_code,
            'runtime': request.runtime_environment,
            'status': 'deployed'
        }
        return osiris_pb2.DeployResponse(message=f'Function "{request.name}" deployed successfully.')

    def UpdateFunction(self, request, context):
        if request.name in functions:
            functions[request.name]['path'] = request.path_to_function_code
            return osiris_pb2.UpdateResponse(message=f'Function "{request.name}" updated successfully.')
        return osiris_pb2.UpdateResponse(message=f'Function "{request.name}" not found.')

    def RemoveFunction(self, request, context):
        if request.name in functions:
            del functions[request.name]
            return osiris_pb2.RemoveResponse(message=f'Function "{request.name}" removed successfully.')
        return osiris_pb2.RemoveResponse(message=f'Function "{request.name}" not found.')

    def ListFunctions(self, request, context):
        for name, info in functions.items():
            yield osiris_pb2.FunctionInfo(name=name, runtime=info['runtime'], status=info['status'])

    def DescribeFunction(self, request, context):
        if request.name in functions:
            info = functions[request.name]
            return osiris_pb2.DescribeResponse(
                name=request.name,
                runtime=info['runtime'],
                status=info['status']
            )
        return osiris_pb2.DescribeResponse(name=request.name, runtime="", status="not found")

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
    osiris_pb2_grpc.add_OsirisServicer_to_server(OsirisServicer(), server)
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