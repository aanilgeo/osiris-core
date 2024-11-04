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
from logs import LogsFunction
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
        cls.stub.DeployFunction(
            osiris_pb2.DeployRequest(
                path_to_function_code='./functions/add_numbers.py',
                name='addNumbers',
                runtime_environment='python3.8'
            )
        )

    @classmethod
    def tearDownClass(cls):
        # Clean up server resources after all tests run
        cls.channel.close()
        cls.server.stop(0)

    def test_get_logs_basic(self):
        # Test getting logs without tail option
        response = LogsFunction.get_logs(self.stub, 'addNumbers')
        
        # Check if response is not None and contains logs
        self.assertIsNotNone(response)
        self.assertTrue(hasattr(response, 'logs'))

    def test_get_logs_with_tail(self):
        # Test getting logs with tail option
        response = LogsFunction.get_logs(self.stub, 'addNumbers', tail=True)
        
        # Check if response is not None and contains logs
        self.assertIsNotNone(response)
        self.assertTrue(hasattr(response, 'logs'))
        
        # Optionally, check if the number of logs returned is reasonable (e.g., less than or equal to 10)
        self.assertLessEqual(len(response.logs), 10)

    def test_get_logs_nonexistent_function(self):
        # Test getting logs for a non-existent function
        response = LogsFunction.get_logs(self.stub, 'nonExistentFunction')
        
        # Check if response is not None but contains appropriate message
        self.assertIsNotNone(response)
        self.assertTrue(len(response.logs) == 0 or 
                       'No logs found' in response.logs[0])

    def test_get_logs_server_error(self):
        # Shut down the server to simulate an unreachable server
        self.server.stop(0)
        
        # Attempt to get logs while the server is down
        response = LogsFunction.get_logs(self.stub, 'addNumbers')
        
        # Check that the response is None due to the RpcError
        self.assertIsNone(response)
        
        # Restart the server for other tests
        self.server.start()

if __name__ == '__main__':
    unittest.main()
