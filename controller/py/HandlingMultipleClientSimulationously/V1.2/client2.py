# Python TCP Client B
import socket 
import time

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
#MESSAGE = raw_input("tcpClientB: Enter message/ Enter exit:")
MESSAGE = "Hello from Client-1"
 
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientB.connect((host, port))

#while MESSAGE != 'exit':
#    tcpClientB.send(MESSAGE.encode())     
#    data = tcpClientB.recv(BUFFER_SIZE)
#    print("2.Client received data:", data.decode())
    #MESSAGE = raw_input("tcpClientB: Enter message to continue/ Enter exit:")
#    MESSAGE = "Hello from Client-2"
#    time.sleep(10)


for i in range(20, 40):
    MESSAGE = str(i)+' '
    tcpClientB.send(MESSAGE.encode())
    data = tcpClientB.recv(BUFFER_SIZE)
    print("1.Client received data:", data.decode())
    time.sleep(2)

tcpClientB.close() 
