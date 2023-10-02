from socket import *

def send_data(clientSocket, data):
    clientSocket.sendall(data.encode())

def receive_data(clientSocket):
    data = clientSocket.recv(1024).decode()
    return data

clientSocket = socket(AF_INET, SOCK_STREAM)
serverName = 'localhost'
serverPort = 12000
clientSocket.connect((serverName, serverPort))

while True:
    operation = input("Enter operation (Random, Add, Subtract) or 'exit' to quit: ")
    if operation == "exit":
        break
    
    if operation not in ["Random", "Add", "Subtract"]:
        print("Invalid operation. Please try again.")
        continue

    if operation == "Random":
        min_num = input("Enter the minimum number: ")
        max_num = input("Enter the maximum number: ")
        request = f"{operation} {min_num} {max_num}"
    elif operation in ["Add", "Subtract"]:
        n1 = input("Enter the first number: ")
        n2 = input("Enter the second number: ")
        request = f"{operation} {n1} {n2}"

    send_data(clientSocket, request)
    response = receive_data(clientSocket)

    print(f"Result: {response}")

clientSocket.close()
