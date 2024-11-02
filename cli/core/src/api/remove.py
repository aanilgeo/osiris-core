import sys
sys.path.append('C:/Users/harsh/osiris-core/cli/core/proto')
import osiris_pb2
import osiris_pb2_grpc
import grpc

import os

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

class RemoveFunction:

    @staticmethod
    def remove_function(stub, function_name):
        try:
            # Build the request with the function name
            request = osiris_pb2.RemoveRequest(function_name=function_name)
            
            # Call the RemoveFunction endpoint on the server
            response = stub.RemoveFunction(request)
            
            if response.success:
                print(f'Function "{function_name}" removed successfully.')
            else:
                print(f'Function "{function_name}" not found.')
                
            # Return the response for further use or testing
            return response
            
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
        
        # Example usage of RemoveFunction for a function named 'addNumbers'
        RemoveFunction.remove_function(stub, "addNumbers")
