📨 Python File Transfer

A simple Python socket-based file transfer system where the client sends a file and the server receives and saves it over a local network.

🚀 How It Works

The client connects to the server using TCP.

It sends the filename, filesize, and file data in chunks.

The server receives the data and saves it as received_<filename>.

📁 Files Included

client.py — sends a file to the server

server.py — receives and stores the file

▶️ Usage
1. Start the Server
python server.py

2. Run the Client
python client.py


Both devices must be connected to the same network.

👨‍💻 Author

Vivek Rao
GitHub: 
