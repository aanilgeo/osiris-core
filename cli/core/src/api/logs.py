import sys
import argparse
sys.path.append('C:/Users/neelp/osiris-core/cli/core/proto')
import osiris_pb2
import osiris_pb2_grpc
import grpc
from list import ListFunctions
import datetime


# Suppress logging warnings
import os
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

class OsirisLogs:

    @staticmethod
    def get_logs(stub, function_name, tail):
        try:
            #Get the list of deployed functions
            deployed_functions = ListFunctions.list_functions(stub) #call the method to get the function list
            
            #check if the function is deployed
            function_names = [func.function_name for func in deployed_functions] if deployed_functions else []
            if function_name not in function_names:
                print(f"Function '{function_name}' is not deployed.")
                return None
            
            # Build the request with the function name and tail option
            request = osiris_pb2.LogsRequest(function_name=function_name, tail=tail)

            # Call the GetLogs endpoint on the server
            response = stub.GetLogs(request)

            # Check if logs were retrieved
            if response.logs:
                print(f"Logs for function '{function_name}':")
                for log_entry in response.logs:
                    # Convert timestamp from seconds to a human-readable format
                    readable_time = datetime.datetime.fromtimestamp(log_entry.timestamp).strftime('%Y-%m-%d %H:%M:%S')
                    print(f"{readable_time} - {log_entry.message}")
            else:
                print(f"No logs found for function '{function_name}'.")

            # Return the logs for further use or testing
            return response.logs
            
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                print("gRPC server is unavailable.")
                return None
            else:
                # Handle other gRPC errors
                print(f"An unknown error occurred: {e}")
                return None

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Retrieve logs for a specific function in the Osiris platform.")
    parser.add_argument("function_name", type=str, help="The name of the function whose logs are being retrieved.")
    parser.add_argument("--tail", action="store_true", help="Retrieve the most recent logs.")

    # Parse the command line arguments
    args = parser.parse_args()

    # Connect to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = osiris_pb2_grpc.OsirisServiceStub(channel)

        # Retrieve logs based on the function name and tail option
        OsirisLogs.get_logs(stub, args.function_name, args.tail)

if __name__ == "__main__":
    main()
