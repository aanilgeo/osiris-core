import sys
sys.path.append('C:/Users/neelp/osiris-core/cli/core/proto')
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
                'status': 'running'
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
        function_list = [
            osiris_pb2.FunctionInfo(function_name=name, runtime=info['runtime'], status=info['status'])
            for name, info in functions.items()
        ]
        return osiris_pb2.ListResponse(functions=function_list)

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
        # Create an instance of LogsResponse
        response = osiris_pb2.LogsResponse()
        log_data = [
            {"timestamp": 1666246800, "message": "Function started with inputs: 3, 5"},
            {"timestamp": 1666246810, "message": "Function executed successfully. Result: 8"}
        ]

        for log in log_data:
            # Create a LogEntry object
            log_entry = osiris_pb2.LogEntry(
                timestamp=log["timestamp"],
                message=log["message"]
            )
            # Append the LogEntry object to the response's logs field
            response.logs.append(log_entry)

        return response

    def MonitorFunction(self, request, context):
        print(f"Received MonitorFunction request for: {request.function_name} (type: {type(request.function_name)})")
        response = osiris_pb2.MonitorResponse()
        if request.function_name in functions:
            response.function_name = request.function_name
            response.cpu_usage = str(10)
            response.memory_usage = str(20)
            response.execution_time = str(0.5)
            return response
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Function not found')
            return response


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