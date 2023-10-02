from socket import *
import threading
import json
import random

def send_json(connectionSocket, data):
    json_data = json.dumps(data)
    connectionSocket.sendall(json_data.encode())

def receive_json(connectionSocket):
    data = connectionSocket.recv(1024).decode()
    return json.loads(data)

def handle_client(connectionSocket, client_address):
    print('Connection established with', client_address)
    
    request = receive_json(connectionSocket)
    operation = request.get("operation")

    if operation == "Random":
        min_num = request.get("min_num")
        max_num = request.get("max_num")
        result = random.randint(min_num, max_num)
    elif operation == "Add":
        n1 = request.get("n1")
        n2 = request.get("n2")
        result = n1 + n2
    elif operation == "Subtract":
        n1 = request.get("n1")
        n2 = request.get("n2")
        result = n1 - n2
    else:
        result = "Invalid"

    response = {"result": result}
    send_json(connectionSocket, response)
    connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('Server is ready to listen')

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handle_client, args=(connectionSocket, addr)).start()
