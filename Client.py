from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

operation = input("Enter operation (Random/Add/Subtract): ")
clientSocket.sendall(operation.encode())

if operation == "Random":
    min_num, max_num = map(int, input("Enter min and max number separated by a ;(Semicolon): ").split(";"))
    clientSocket.sendall(f"{min_num};{max_num}".encode())

elif operation in ["Add", "Subtract"]:
    n1, n2 = map(int, input("Enter the two numbers you want to add or subtract separated by a ;(Semicolon): ").split(";"))
    clientSocket.sendall(f"{n1};{n2}".encode())
else:
    print("Invalid operation")
    clientSocket.close()
    exit()

result = clientSocket.recv(1024).decode()
print("Result from server:", result)

clientSocket.close()