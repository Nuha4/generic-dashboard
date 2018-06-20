# Python TCP Client A
import socket
import time

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 4000 
#MESSAGE = raw_input("tcpClientA: Enter message/ Enter exit:")

MESSAGE = "Hello from Client-1"
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

while MESSAGE != 'exit':
    tcpClientA.send(MESSAGE.encode())     
    data = tcpClientA.recv(BUFFER_SIZE)
    print("1.Client received data:", data.decode())
    #MESSAGE = raw_input("tcpClientA: Enter message to continue/ Enter exit:")
    MESSAGE = "Hello from Client-1"
    time.sleep(10)

tcpClientA.close() 
