import socket

HOST, PORT = '127.0.0.1', 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server listening on {HOST}:{PORT}") 
while True:
    client, _ = server.accept()
    filename = client.recv(1024).decode()
    try:
        with open(filename, 'r') as f:
            client.send(f.read().encode())
    except FileNotFoundError:
        client.send(b"Error: File not found.")
    client.close()
