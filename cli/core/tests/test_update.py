import sys
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/proto')
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/src')
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/src/api')
import unittest
import osiris_pb2_grpc
import grpc
from concurrent import futures
from server import OsirisServicer
from deploy import DeployFunction
from update import UpdateFunction

import os

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

class DeployFunctionTest(unittest.TestCase):
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

        DeployFunction.deploy_function(cls.stub, 'newFunction', '~/cli/core/functions', 'python3.8')

    @classmethod
    def tearDownClass(cls):
        # Clean up server resources after all tests run
        cls.channel.close()
        cls.server.stop(0)
    
    def test_update_function(self):
        # Use UpdateFunction to make the request and handle responses
        response = UpdateFunction.update_function(self.stub, 'newFunction', '~/cli/core/functions')
        
        # Check if the response contains the correct details
        self.assertIsNotNone(response, "Response should not be None")
        self.assertEqual(response.success, True)

    def test_update_nonexistent_function(self):
        # Use UpdateFunction for an already existing function
        response = UpdateFunction.update_function(self.stub, 'nofAFunction', '~/cli/core/functions')
        
        # Check if the response indicates function already exists
        self.assertIsNotNone(response, "Response should not be None")
        self.assertEqual(response.success, False)

    def test_update_with_server_error(self):
        # Shut down the server to simulate an unreachable server
        self.server.stop(0).wait()
        
        # Attempt to describe a function while the server is down
        response = UpdateFunction.update_function(self.stub, 'testFunction', '~/cli/core/functions')
        
        # Check that the response is None due to the RpcError
        self.assertIsNone(response, "Response should be None when server is unreachable")

if __name__ == '__main__':
    unittest.main()