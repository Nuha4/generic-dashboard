#!/usr/bin/env python

import socket
TCP_IP = '192.168.137.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "0"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
    status = input()
    s.send(status.encode())

#s.send(MESSAGE.encode())
#data = s.recv(BUFFER_SIZE)
#s.close()
#print("received data:", data)


#while True:
    #c,addr = s.accept() #Establish a connection with the client
    #print("Got connection from", addr)
    #c.send("Thank you for connecting!")
    #status = input()
    #c.send(status)

    #c.close()