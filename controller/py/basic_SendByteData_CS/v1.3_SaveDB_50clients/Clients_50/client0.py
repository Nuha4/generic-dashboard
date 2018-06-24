# Python TCP Client B
import socket
import time

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
 
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientB.connect((host, port))

MESSAGE = "00000000000000000000111"
tcpClientB.send(MESSAGE.encode())     
tcpClientB.close()
