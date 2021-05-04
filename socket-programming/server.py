import socket

s = socket.socket()

port = 1989
s.bind(('', port))

s.listen(5)

while True:
    c, addr = s.accept()
    print('Received connection from', addr)
    c.send(b'Thank you for connecting\n')
    c.close()