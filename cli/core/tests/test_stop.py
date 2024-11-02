import sys
sys.path.append('C:/Users/jrcud/CS490/osiris-core/cli/core/proto')
sys.path.append('C:/Users/jrcud/CS490/osiris-core/cli/core/src')
sys.path.append('C:/Users/jrcud/CS490/osiris-core/cli/core/src/api')
import unittest
import osiris_pb2
import osiris_pb2_grpc
from server import OsirisServicer
from start import StartPlatform
from stop import StopPlatform
import grpc
from concurrent import futures

import os

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

class StopPlatformTest(unittest.TestCase):
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
    
    def test_stop_platform(self):
        # Start the platform
        StartPlatform.start_platform(self.stub)

        # Use StopPlatform to make the request and handle the response
        response = StopPlatform.stop_platform(self.stub)
        
        # Check if the response contains the correct details
        self.assertIsNotNone(response, "Response should not be None")
        self.assertEqual(response.success, True)
        self.assertEqual(response.message, "Osiris platform stopped successfully.")

    def test_stop_platform_already_stopped(self):
        # Attempt to stop the platform again, expecting a different response
        response = StopPlatform.stop_platform(self.stub)
        self.assertIsNotNone(response, "Response should not be None")
        self.assertEqual(response.success, False)
        self.assertEqual(response.message, "Platform is already stopped.")

    def test_stop_platform_with_server_error(self):
        # Shut down the server to simulate an unreachable server
        self.server.stop(0).wait()
        
        # Attempt to start the platform while the server is down
        response = StopPlatform.stop_platform(self.stub)
        
        # Check that the response is None due to the RpcError
        self.assertIsNone(response, "Response should be None when server is unreachable")

if __name__ == '__main__':
    unittest.main()