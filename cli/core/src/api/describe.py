import sys
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/proto')
import osiris_pb2
import osiris_pb2_grpc
import grpc

class DescribeFunction:

    @staticmethod
    def describe_function(stub, function_name):
        # try:
            # Build the request with the function name
            request = osiris_pb2.DescribeRequest(function_name=function_name)
            
            # Call the DescribeFunction endpoint on the server
            response = stub.DescribeFunction(request)
            
            # Check if function details were found
            if response.status == "not found":
                print(f"Function '{function_name}' not found.")
            else:
                print(f"Function Details for '{function_name}':")
                print(f"Name: {response.name}")
                print(f"Runtime: {response.runtime}")
                print(f"Status: {response.status}")

            # Return the response for further use or testing
            return response
            
        # except grpc.RpcError as e:
        #     print(f"An error occurred while describing the function: {e}")
        #     return None

if __name__ == "__main__":
    # Connect to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = osiris_pb2_grpc.OsirisServiceStub(channel)
        
        # Example usage of DescribeFunction for a function named 'addNumbers'
        DescribeFunction.describe_function(stub, "addNumbers")