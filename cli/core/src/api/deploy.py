
import sys
sys.path.append('C:/Users/harsh/osiris-core/cli/core/proto')
import osiris_pb2
import osiris_pb2_grpc
import grpc

import os

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

class DeployFunction:

    @staticmethod
    def deploy_function(stub, function_name, path, runtime):
        try:
            # Build the request with the function name
            request = osiris_pb2.DeployRequest(
                function_name = function_name,
                path_to_function_code = path,
                runtime_environment = runtime
            )
            
            # Call the DeployFunction endpoint on the server
            response = stub.DeployFunction(request)
            
            # Check if function details were found
            if response.success:
                print(f"Function '{function_name}' already exists.")
            else:
                print(f"Function '{function_name}' deployed successfully.")

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
        
        # Example usage of DeployFunction for a function named 'addNumbers'
        DeployFunction.deploy_function(stub, "addNumbers")
