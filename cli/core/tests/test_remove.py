import sys
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/proto')
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/src')
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/src/api')
import unittest
import osiris_pb2
import osiris_pb2_grpc
from server import OsirisServicer
from remove import RemoveFunction
from deploy import DeployFunction
import grpc
from concurrent import futures

import os

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

class RemoveFunctionTest(unittest.TestCase):
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
        DeployFunction.deploy_function(cls.stub, 'testFunction', './functions/sample_function.py', 'python3.8')

    @classmethod
    def tearDownClass(cls):
        # Clean up server resources after all tests run
        cls.channel.close()
        cls.server.stop(0)
    
    def test_remove_function(self):
        # Use RemoveFunction to make the request and handle responses
        response = RemoveFunction.remove_function(self.stub, 'testFunction')
        
        # Check if the response contains the correct details
        self.assertIsNotNone(response, "Response should not be None")
        self.assertEqual(response.success, True, 'Function "testFunction" removed successfully.')

    def test_remove_non_existent_function(self):
        # Use RemoveFunction for a non-existent function
        response = RemoveFunction.remove_function(self.stub, 'nonExistentFunction')
        
        # Check if the response indicates function not found
        self.assertIsNotNone(response, "Response should not be None")
        self.assertEqual(response.success, False, 'Function "nonExistentFunction" not found.')

    def test_remove_with_server_error(self):
        # Shut down the server to simulate an unreachable server
        self.server.stop(4).wait()
        
        # Attempt to describe a function while the server is down
        response = RemoveFunction.remove_function(self.stub, 'testFunction')
        
        # Check that the response is None due to the RpcError
        self.assertIsNone(response, "Response should be None when server is unreachable")
        
if __name__ == '__main__':
    unittest.main()
