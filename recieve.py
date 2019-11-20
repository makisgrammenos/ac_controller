import socket

IP = "192.168.1.13"
PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((IP,PORT))
while True:
    data,addr = sock.recvfrom(1024)
    print data