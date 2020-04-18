import socket
s=socket.socket()
port=12346
s.connect(('127.0.0.1',port))
while True:
    print('Received from server: '+ s.recv(1024))
    a=raw_input()
    s.send(str(a))
    print('Sent to server successfully!')
