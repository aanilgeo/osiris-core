import sys
import unittest
from unittest.mock import MagicMock
import osiris_pb2
import osiris_pb2_grpc
from monitor import MonitorFunction
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/proto')
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/src')
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/src/api')

class TestMonitorFunction(unittest.TestCase):

    def setUp(self):
        # Mock the gRPC stub
        self.stub = MagicMock(spec=osiris_pb2_grpc.OsirisServiceStub)

    def test_monitor_function_success(self):
        # Define a mock response for a successful call
        mock_response = osiris_pb2.MonitorResponse(
            execution_time="0.5ms",
            cpu_usage="10%",
            memory_usage="20MB"
        )
        
        # Set up the stub's MonitorFunction method to return the mock response
        self.stub.MonitorFunction.return_value = mock_response

        # Call the monitor_function method
        metrics = MonitorFunction.monitor_function(self.stub, "addNumbers")

        # Verify the results
        self.assertIsNotNone(metrics)
        self.assertEqual(metrics["execution_time"], "0.5ms")
        self.assertEqual(metrics["cpu_usage"], "10%")
        self.assertEqual(metrics["memory_usage"], "20MB")

    def test_monitor_function_no_metrics(self):
        # Define a mock response with empty metrics
        mock_response = osiris_pb2.MonitorResponse(
            execution_time="",
            cpu_usage="",
            memory_usage=""
        )
        
        # Set up the stub's MonitorFunction method to return the mock response
        self.stub.MonitorFunction.return_value = mock_response

        # Call the monitor_function method
        metrics = MonitorFunction.monitor_function(self.stub, "unknownFunction")

        # Verify the results
        self.assertIsNotNone(metrics)
        self.assertEqual(metrics["execution_time"], "")
        self.assertEqual(metrics["cpu_usage"], "")
        self.assertEqual(metrics["memory_usage"], "")

    def test_monitor_function_server_unavailable(self):
        # Simulate a gRPC error for an unavailable server
        self.stub.MonitorFunction.side_effect = grpc.RpcError("gRPC server is unavailable.")

        # Call the monitor_function method
        metrics = MonitorFunction.monitor_function(self.stub, "addNumbers")

        # Verify that the result is None due to server unavailability
        self.assertIsNone(metrics)

if __name__ == "__main__":
    unittest.main()
