from socket import *
import threading
import random

def handle_client(connectionSocket, client_address):
    print('Connection established with', client_address)
    operation = connectionSocket.recv(1024).decode()

    if operation == "Random":
        min_num, max_num = map(int, connectionSocket.recv(1024).decode().split())
        result = random.randint(min_num, max_num)

    elif operation == "Add":
        n1, n2 = map(int, connectionSocket.recv(1024).decode().split(";"))
        result = n1 + n2

    elif operation == "Subtract":
        n1, n2 = map(int, connectionSocket.recv(1024).decode().split(";"))
        result = n1 - n2

    else:
        result = "Invalid"

    connectionSocket.sendall(str(result).encode())
    connectionSocket.close()


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handle_client, args=(connectionSocket, addr)).start()