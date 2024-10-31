import sys
sys.path.append('C:/Users/sebia/CS490/osiris-core/cli/core/proto')
sys.path.append('C:/Users/sebia/CS490/osiris-core/cli/core/src')
sys.path.append('C:/Users/sebia/CS490/osiris-core/cli/core/src/api')
import unittest
import osiris_pb2
import osiris_pb2_grpc
from server import OsirisServicer
from describe import DescribeFunction
import grpc
from concurrent import futures

import os

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

class DescribeFunctionTest(unittest.TestCase):
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
        
        # Deploy a function for testing purposes
        #cls.stub.DeployFunction(
        #    osiris_pb2.DeployRequest(
        #        path_to_function_code='./functions/sample_function.py',
        #        function_name='testFunction',
        #        runtime_environment='python3.8'
        #    )
        #)

    @classmethod
    def tearDownClass(cls):
        # Clean up server resources after all tests run
        cls.channel.close()
        cls.server.stop(0)
    
    def test_describe_function(self):
        # Use DescribeFunction to make the request and handle responses
        response = DescribeFunction.describe_function(self.stub, 'testFunction')
        
        # Check if the response contains the correct details
        self.assertIsNotNone(response, "Response should not be None")
        self.assertEqual(response.name, 'testFunction')
        self.assertEqual(response.runtime, 'python3.8')
        self.assertEqual(response.status, 'deployed')

    def test_describe_non_existent_function(self):
        # Use DescribeFunction for a non-existent function
        response = DescribeFunction.describe_function(self.stub, 'nonExistentFunction')
        
        # Check if the response indicates function not found
        self.assertIsNotNone(response, "Response should not be None")
        self.assertEqual(response.name, 'nonExistentFunction')
        self.assertEqual(response.status, 'not found')

    def test_describe_with_server_error(self):
        # Shut down the server to simulate an unreachable server
        self.server.stop(4).wait()
        
        # Attempt to describe a function while the server is down
        response = DescribeFunction.describe_function(self.stub, 'testFunction')
        
        # Check that the response is None due to the RpcError
        self.assertIsNone(response, "Response should be None when server is unreachable")
        
        # Restart the server for other tests
        self.server.start()

if __name__ == '__main__':
    unittest.main()