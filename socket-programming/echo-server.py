import socket

HOST = '127.0.0.1' # localhost
PORT = 65432

# AF_INET: address family, i.e. IPv4
# SOCK_STREAM: socket type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # with statement means no need to explicitly close socket
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
