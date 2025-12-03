import socket

HOST = '0.0.0.0'
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server is listening...")

client_socket, addr = server.accept()
print(f"Connected with {addr}")

# Receive file info separately
filename = client_socket.recv(1024).decode('utf-8')
filesize = int(client_socket.recv(1024).decode('utf-8'))

print(f"Receiving file: {filename} ({filesize} bytes)")

# Receive file data
with open(f"received_{filename}", "wb") as f:
    bytes_read = 0
    while bytes_read < filesize:
        data = client_socket.recv(1024)
        if not data:
            break
        f.write(data)
        bytes_read += len(data)

print(f"{filename} received successfully!")
client_socket.close()
server.close()
