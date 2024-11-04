import sys
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/proto')
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/src')
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/src/api')
import unittest
import osiris_pb2
import osiris_pb2_grpc
from server import OsirisServicer
from list import ListFunctions
from deploy import DeployFunction
from remove import RemoveFunction
import grpc
from concurrent import futures

import os

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

class ListFunctionsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the server in the background
        cls.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        osiris_pb2_grpc.add_OsirisServiceServicer_to_server(OsirisServicer(), cls.server)
        cls.port = '[::]:50051'
        cls.server.add_insecure_port(cls.port)
        cls.server.start()
        
        # Set up the channel and stub for the test client
        cls.channel = grpc.insecure_channel('localhost:50051')
        cls.stub = osiris_pb2_grpc.OsirisServiceStub(cls.channel)
        
        #Deploy a function for testing purposes
        DeployFunction.deploy_function(cls.stub, 'addNumbers', './functions/sample_function.py', 'python3.8')
        DeployFunction.deploy_function(cls.stub, 'subtractNumbers', './functions/sample_function.py', 'node.js')

    @classmethod
    def tearDownClass(cls):
        # Clean up server resources after all tests run
        cls.channel.close()
        cls.server.stop(0)
    
    def test_list_functions(self):
        #Use ListFunctions to make the request and handle responses
        response = ListFunctions.list_functions(self.stub)
        functions_list = list(response)
        
        #Check if response contains both functions
        self.assertIn("Function Name: addNumbers, Runtime: python3.8, Status: running", functions_list[0])
        self.assertIn("Function Name: subtractNumbers, Runtime: node.js, Status: running", functions_list[1])

        # Check if the response contains the correct details
        self.assertIsNotNone(response, "Response should not be None")
    
    def test_list_no_deployed_functions(self):
        #Removing the functions
        RemoveFunction.remove_function(self.stub, 'addNumbers')
        RemoveFunction.remove_function(self.stub, 'subtractNumbers')

        #Use ListFunctions to make the request and handle responses
        response = ListFunctions.list_functions(self.stub)
        
        #Check if response contains both functions
        self.assertIn("No function is deployed.", response)

        # Check if the response contains the correct details
        self.assertIsNotNone(response, "Response should not be None")
        

    def test_list_with_server_error(self):
        # Shut down the server to simulate an unreachable server
        self.server.stop(4).wait()
        
        # Attempt to describe a function while the server is down
        response = ListFunctions.list_functions(self.stub)
        
        # Check that the response is None due to the RpcError
        self.assertIsNone(response, "Response should be None when server is unreachable")
        
if __name__ == '__main__':
    unittest.main()
