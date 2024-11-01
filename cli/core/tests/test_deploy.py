import sys
sys.path.append('C:/Users/sebia/CS490/osiris-core/cli/core/proto')
sys.path.append('C:/Users/sebia/CS490/osiris-core/cli/core/src')
sys.path.append('C:/Users/sebia/CS490/osiris-core/cli/core/src/api')
import unittest
import osiris_pb2_grpc
import grpc
from concurrent import futures
from server import OsirisServicer
from deploy import DeployFunction

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

    @classmethod
    def tearDownClass(cls):
        # Clean up server resources after all tests run
        cls.channel.close()
        cls.server.stop(0)
    
    def test_deploy_function(self):
        # Use DeployFunction to make the request and handle responses
        response = DeployFunction.deploy_function(self.stub, 'testFunction', '~/cli/core/functions', 'python3.8')
        
        # Check if the response contains the correct details
        self.assertIsNotNone(response, "Response should not be None")
        self.assertEqual(response.success, True)

    def test_deploy_existing_function(self):
        # Use DeployFunction for an already existing function
        response = DeployFunction.deploy_function(self.stub, 'testFunction1', '~/cli/core/functions', 'python3.8')
        response = DeployFunction.deploy_function(self.stub, 'testFunction1', '~/cli/core/functions', 'python3.8')
        
        # Check if the response indicates function already exists
        self.assertIsNotNone(response, "Response should not be None")
        self.assertEqual(response.success, False)

    def test_deploy_with_server_error(self):
        # Shut down the server to simulate an unreachable server
        self.server.stop(0).wait()
        
        # Attempt to describe a function while the server is down
        response = DeployFunction.deploy_function(self.stub, 'testFunction', '~/cli/core/functions', 'python3.8')
        
        # Check that the response is None due to the RpcError
        self.assertIsNone(response, "Response should be None when server is unreachable")

if __name__ == '__main__':
    unittest.main()