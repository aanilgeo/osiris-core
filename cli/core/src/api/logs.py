import sys
import grpc
import os
import datetime
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/proto')
import osiris_pb2
import osiris_pb2_grpc
from list import ListFunctions  

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

class GetLogs:

    @staticmethod
    def get_logs(stub, function_name, tail):
        try:
            # Get the list of deployed functions as formatted strings
            deployed_functions = ListFunctions.list_functions(stub)
            print("Deployed functions from list_functions:", deployed_functions)

            # Check if `deployed_functions` is None
            if deployed_functions is None:
                print("Error: Unable to retrieve deployed functions.")
                return None  # Return None if there's an error fetching deployed functions

            # Extract function names from the formatted strings
            function_names = []
            for func in deployed_functions:
                # Parse each string to extract the function name
                if "Function Name:" in func:
                    function_name_part = func.split(",")[0]  # Get the "Function Name: <name>" part
                    extracted_name = function_name_part.split(":")[1].strip()  # Extract the name itself
                    function_names.append(extracted_name)
            
            # Check if the function is deployed
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

if __name__ == "__main__":
    # Connect to the server and call get_logs with a specific function name and tail option
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = osiris_pb2_grpc.OsirisServiceStub(channel)
        
        # Example usage of get_logs for a function named 'addNumbers' with tail=True
        OsirisLogs.get_logs(stub, "addNumbers", tail=True)
