import socket
import os
import time

HOST = '192.168.0.109'  # server IP
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

filename = input("Enter file name to send: ")

if not os.path.exists(filename):
    print("File does not exist!")
    client.close()
    exit()

filesize = os.path.getsize(filename)

# Send file info (with small delay to avoid merge)
client.send(filename.encode('utf-8'))
time.sleep(0.2)  # short delay
client.send(str(filesize).encode('utf-8'))
time.sleep(0.2)

# Send file data
with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(1024)
        if not bytes_read:
            break
        client.sendall(bytes_read)

print(f"{filename} sent successfully!")
client.close()
