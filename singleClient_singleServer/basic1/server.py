import socket
s=socket.socket()
print('socket created successfully')
port=12346
s.bind(('',port))
print('socket binded to %s',port)
s.listen(10)
print('socket is listening')
c,addr=s.accept()
print('Got connection from ',addr)
while True:
    a=raw_input()
    c.send(str(a))
    print('Message Sent to client successfully')
    print('Received from client: ' + c.recv(1024))
