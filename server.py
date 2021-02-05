import socket
s=socket.socket()
print("socket is created !")
s.bind(('localhost',9999))
s.listen(3)
print("waiting for users ")
while True:
    c,addr=s.accept()
    name = c.recv(1024).decode()
    print("connection with",addr,name)
    c.send(bytes('welcome to class a','utf-8'))

    c.close()