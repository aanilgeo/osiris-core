import sys
import os
import grpc
import osiris_pb2
import osiris_pb2_grpc

# Add proto directory to system path
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/proto')

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

class MonitorFunction:

    @staticmethod
    def monitor_function(stub, function_name):
        try:
            # Create the request object with the function name
            request = osiris_pb2.MonitorRequest(function_name=function_name)

            # Call the MonitorFunction endpoint on the server
            response = stub.MonitorFunction(request)

            # Display the metrics
            if response.cpu_usage or response.memory_usage or response.execution_time:
                print(f"Function Name: {function_name}")
                print(f"Execution Time: {response.execution_time}")
                print(f"CPU Usage: {response.cpu_usage}")
                print(f"Memory Usage: {response.memory_usage}")
            else:
                print(f"No metrics found for function '{function_name}'.")

            # Return the metrics as a dictionary for further use or testing
            return {
                "function_name": function_name,
                "execution_time": response.execution_time,
                "cpu_usage": response.cpu_usage,
                "memory_usage": response.memory_usage
            }
        
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                print("gRPC server is unavailable.")
                return None
            else:
                print(f"An unknown error occurred: {e}")
                return None

if __name__ == "__main__":
    import argparse
    
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Monitor a specific function on the Osiris platform.")
    parser.add_argument("function_name", type=str, help="The name of the function to monitor.")

    # Parse command line arguments
    args = parser.parse_args()

    # Connect to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = osiris_pb2_grpc.OsirisServiceStub(channel)
        
        # Retrieve function metrics based on the function name
        MonitorFunction.monitor_function(stub, args.function_name)
