# Import socket module
import socket               
import time
# Create a socket object
#s = socket.socket()         

host = socket.gethostname() 
# Define the port on which you want to connect
port = 5000               

BUFFER_SIZE = 4000

# connect to the server on local computer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host, port))

for i in range(40, 60):
    MESSAGE = str(i)+' '
    s.send(MESSAGE.encode())
    data = s.recv(BUFFER_SIZE)
    print("1.Client received data:", data.decode())
    time.sleep(2)
	
 
# receive data from the server
#print s.recv(1024)
# close the connection
s.close()   
