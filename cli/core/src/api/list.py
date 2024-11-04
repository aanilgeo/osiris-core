import sys
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/proto')
import osiris_pb2
import osiris_pb2_grpc
import grpc

import os

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

class ListFunctions:

    @staticmethod
    def list_functions(stub):
        try:
            # Build the request
            request = osiris_pb2.ListRequest()
            
            # Call the ListFunction endpoint on the server
            response = stub.ListFunctions(request)

            #List of all the functions currently deployed
            functions_list = []
            functions_list = response.functions
            formatted_func_list = []
            
            # Check if function details were found
            if len(functions_list) != 0:
                print("Deployed Functions:")
                for index, deployed_func_info in enumerate(functions_list, 1):
                    print(f"{index}. Function Name: {deployed_func_info.function_name}, Runtime: {deployed_func_info.runtime}, Status: {deployed_func_info.status}")
                    formatted_func_list.append(f"Function Name: {deployed_func_info.function_name}, Runtime: {deployed_func_info.runtime}, Status: {deployed_func_info.status}")
            else:
                print("No function is deployed.")
                #For testing
                return ["No function is deployed."]

            # Return the functions in a list format for testing
            return formatted_func_list
            
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                return None
            else:
                # Handle other gRPC errors
                print(f"An unknown error occurred: {e}")
                return None

if __name__ == "__main__":
    # Connect to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = osiris_pb2_grpc.OsirisServiceStub(channel)
        
        # Example usage of ListFunction for a function named 'addNumbers'
        ListFunctions.list_functions(stub)
