import socket

HOST, PORT = '127.0.0.1', 12345
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print(f"UDP Server listening on {HOST}:{PORT}")

while True:
    data, client_address = server.recvfrom(1024)  # Receive filename from client
    filename = data.decode()
    print(f"Client requested file: {filename}")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            server.sendto(content.encode(), client_address)
            print("File sent successfully.")
    except FileNotFoundError:
        server.sendto(b"Error: File not found.", client_address)
        print("File not found.")
