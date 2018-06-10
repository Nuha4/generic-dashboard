#!/usr/bin/env python

import socket
TCP_IP = '192.168.137.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "0"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

#while True:
for i in range(3000000): 
    status = str(i)
    s.send(status.encode())
s.close()