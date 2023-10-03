from socket import *
import threading
import random

def send_data(connectionSocket, data):
    connectionSocket.sendall(data.encode())

def receive_data(connectionSocket):
    data = connectionSocket.recv(1024).decode()
    return data

def handle_client(connectionSocket, client_address):
    print('Connection established with', client_address)
    
    request = receive_data(connectionSocket)
    request_parts = request.split()
    
    if len(request_parts) < 1:
        result = "Invalid"
    else:
        operation = request_parts[0]

        if operation == "Random" and len(request_parts) == 3:
            min_num = int(request_parts[1])
            max_num = int(request_parts[2])
            result = str(random.randint(min_num, max_num))
        elif (operation == "Add" or operation == "Subtract") and len(request_parts) == 3:
            n1 = int(request_parts[1])
            n2 = int(request_parts[2])
            if operation == "Add":
                result = str(n1 + n2)
            else:
                result = str(n1 - n2)
        else:
            result = "Invalid"

    send_data(connectionSocket, result)

   

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('Server is ready to listen')

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handle_client, args=(connectionSocket, addr)).start()
