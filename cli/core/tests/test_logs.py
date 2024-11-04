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
from logs import GetLogs
import grpc
from concurrent import futures

import os

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

class LogsFunctionTest(unittest.TestCase):
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
        
        # Deploy a test function
        DeployFunction.deploy_function(cls.stub, 'testFunction', './functions/sample_function.py', 'python3.8')

    @classmethod
    def tearDownClass(cls):
        # Clean up server resources after all tests run
        cls.channel.close()
        cls.server.stop(0)

    def test_get_logs_basic(self):
        # Test retrieving logs for an existing function
        response = GetLogs.get_logs(self.stub, 'testFunction', tail=True)

        self.assertTrue(len(response) > 0, "Expected logs for deployed function")
        
        # Check that each log entry has 'message' and 'timestamp' attributes
        for log_entry in response:
            self.assertTrue(hasattr(log_entry, 'message'), "Log entry missing 'message'")
            self.assertTrue(hasattr(log_entry, 'timestamp'), "Log entry missing 'timestamp'")

    def test_get_logs_with_tail(self):
        # Test getting logs with the tail option enabled
        response = GetLogs.get_logs(self.stub, 'testFunction', tail=True)
        
        # Check if response has log entries
        if response is not None:
            self.assertTrue(len(response) > 0, "Expected logs for deployed function")
            # Ensure the length is reasonable if tail is applied
            self.assertLessEqual(len(response), 10, "Expected fewer than or equal to 10 log entries with tail=True")


    def test_get_logs_nonexistent_function(self):
        # Test retrieving logs for a non-existent function
        response = GetLogs.get_logs(self.stub, 'nonExistentFunction', tail=False)
        
        # Check if response is None for a non-existent function
        self.assertIsNone(response, "Expected None response for a non-existent function")

    def test_get_logs_server_error(self):
        # Shut down the server to simulate an unreachable server
        self.server.stop(0).wait()
        
        # Attempt to get logs while the server is down
        response = GetLogs.get_logs(self.stub, 'testFunction', tail=False)
        
        # Check that the response is None since the server is unreachable
        self.assertIsNone(response, "Expected None response when the server is unreachable")

if __name__ == '__main__':
    unittest.main()