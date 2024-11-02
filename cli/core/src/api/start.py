import sys
sys.path.append('C:/Users/jrcud/CS490/osiris-core/cli/core/proto')
import osiris_pb2
import osiris_pb2_grpc
import grpc

import os

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

class StartPlatform:

    @staticmethod
    def start_platform(stub):
        try:
            # Build the request 
            request = osiris_pb2.StartRequest()
            
            # Call the StartPlatform endpoint on the server
            response = stub.StartPlatform(request)
            
            # Print the response message
            print(response.message)
            
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
        
        # Example usage of StartPlatform
        StartPlatform.start_platform(stub)