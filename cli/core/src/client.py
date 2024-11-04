import sys
sys.path.append('/Users/HP/NJIT/CS-490/osiris-core/cli/core/proto')
import osiris_pb2
import osiris_pb2_grpc
import grpc
import datetime


def run():
    # Establish connection to server
    channel = grpc.insecure_channel('localhost:50051')
    stub = osiris_pb2_grpc.OsirisServiceStub(channel)

    while True:
        print("\nChoose an action:")
        print("1. Deploy Function")
        print("2. Update Function")
        print("3. Remove Function")
        print("4. List Functions")
        print("5. Describe Function")
        print("6. Get Logs")
        print("7. Monitor Function")
        print("8. Start Platform")
        print("9. Stop Platform")
        print("10. Exit")
        
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            path = input("Enter the path to function code: ")
            name = input("Enter the function name: ")
            runtime = input("Enter the runtime environment (e.g., python3.8): ")
            response = stub.DeployFunction(
                osiris_pb2.DeployRequest(
                    path_to_function_code=path,
                    function_name=name,
                    runtime_environment=runtime
                )
            )
            print("DeployFunction Response:", response)

        elif choice == "2":
            name = input("Enter the function name to update: ")
            path = input("Enter the new path to function code: ")
            response = stub.UpdateFunction(
                osiris_pb2.UpdateRequest(
                    function_name=name,
                    path_to_function_code=path
                )
            )
            print("UpdateFunction Response:", response.message)

        elif choice == "3":
            name = input("Enter the function name to remove: ")
            response = stub.RemoveFunction(
                osiris_pb2.RemoveRequest(function_name=name)
            )
            print("RemoveFunction Response:", response.message)

        elif choice == "4":
            print("Deployed Functions:")
            response = stub.ListFunctions(osiris_pb2.ListRequest())
            for index, function in enumerate(response.functions, 1):
                print(f"{index}. Function Name: {function.function_name}, Runtime: {function.runtime}, Status: {function.status}")

        elif choice == "5":
            name = input("Enter the function name to describe: ")
            response = stub.DescribeFunction(
                osiris_pb2.DescribeRequest(function_name=name)
            )
            print(f"DescribeFunction Response:-")
            print(f"Function Name: {response.function_name}")
            print(f"Runtime: {response.runtime}")
            print(f"Status: {response.status}")
            print(f"Deployed At: {response.deployed_at}")

        elif choice == "6":
            name = input("Enter the function name to get logs: ")
            tail = True

            print("Logs:")
            response = stub.GetLogs(osiris_pb2.LogsRequest(function_name=name, tail=tail))
            
            for log_entry in response.logs:  
                # Convert timestamp to a human-readable format
                readable_timestamp = datetime.datetime.fromtimestamp(log_entry.timestamp).strftime('%Y-%m-%d %H:%M:%S')
                # Print formatted log entry
                print(f"{readable_timestamp} - {log_entry.message}")
                #print(log_entry)

        elif choice == "7":
            name = input("Enter the function name to monitor: ")
            response = stub.MonitorFunction(
                osiris_pb2.MonitorRequest(function_name=name)
            )
            print(f"MonitorFunction Response: CPU Usage: {response.cpu_usage}, Memory Usage: {response.memory_usage}, Execution Time: {response.execution_time}")
            print(f"Function Name: {response.function_name}")
            print(f"Execution Time: {response.execution_time}")
            print(f"CPU Usage: {response.cpu_usage}")
            print(f"Memory Usage: {response.memory_usage}")

        elif choice == "8":
            response = stub.StartPlatform(osiris_pb2.StartRequest())
            print("StartPlatform Response:", response.message)

        elif choice == "9":
            response = stub.StopPlatform(osiris_pb2.StopRequest())
            print("StopPlatform Response:", response.message)

        elif choice == "10":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()