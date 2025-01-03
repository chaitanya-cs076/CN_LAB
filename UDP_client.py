import socket

HOST, PORT = '127.0.0.1', 12345
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Enter filename: ")
client.sendto(filename.encode(), (HOST, PORT))  # Send filename to server

response, _ = client.recvfrom(1024)  # Receive server response
print("Response from server:")
print(response.decode())

client.close()
