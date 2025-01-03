import socket

HOST, PORT = '127.0.0.1', 12345
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send(input("Enter filename: ").encode())
print("Response:", client.recv(1024).decode())

client.close()
