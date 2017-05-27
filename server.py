import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Starting server on port 3000")
server.bind((socket.gethostname(), 3000))
server.listen(1)

while True:
    conn, client = server.accept()
    try:
        print("Connection from", client)

        while True:
            data = conn.recv(1024)
            print("Receive from client:", data)
            if data:
                print("Response to client")
                conn.sendall(data)
            else:
                print("No data received")
                break
    finally:
        conn.close()