from socket import *
import json

def send_json(connectionSocket, data):
    json_data = json.dumps(data)
    connectionSocket.sendall(json_data.encode())

def receive_json(connectionSocket):
    data = connectionSocket.recv(1024).decode()
    return json.loads(data)

clientSocket = socket(AF_INET, SOCK_STREAM)
serverName = 'localhost'  
serverPort = 12000
clientSocket.connect((serverName, serverPort))


operation = input("Enter operation (Random, Add, Subtract): ")
if operation not in ["Random", "Add", "Subtract"]:
    print("Invalid operation. Please try again.")
        

request = {"operation": operation}
if operation == "Random":
    min_num = int(input("Enter the minimum number: "))
    max_num = int(input("Enter the maximum number: "))
    request["min_num"] = min_num
    request["max_num"] = max_num

elif operation in ["Add", "Subtract"]:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    request["n1"] = n1
    request["n2"] = n2
        

send_json(clientSocket, request)
response = receive_json(clientSocket)

result = response.get("result")
print(f"Result: {result}")

