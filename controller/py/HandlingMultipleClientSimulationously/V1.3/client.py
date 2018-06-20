# Import socket module
import socket               
import time
# Create a socket object
s = socket.socket()         
 
# Define the port on which you want to connect
port = 5000               

BUFFER_SIZE = 4000
# connect to the server on local computer
s.connect(('127.0.0.1', port))

for i in range(0, 40):
    MESSAGE = str(i)+' '
    s.send(MESSAGE.encode())
    data = s.recv(BUFFER_SIZE)
    print("1.Client received data:", data.decode())
    time.sleep(2)
	
 
# receive data from the server
#print s.recv(1024)
# close the connection
s.close()   
