# Python TCP Client B
import socket
import time

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
#MESSAGE = raw_input("tcpClientB: Enter message/ Enter exit:")
MESSAGE = "Hello from cleint 1"
 
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientB.connect(('127.0.0.1', port))

while MESSAGE != 'exit':
    tcpClientB.send(MESSAGE.encode())     
    data = tcpClientB.recv(BUFFER_SIZE)
    print(" Client 1 received data:", data.decode())
    #MESSAGE = raw_input("tcpClientB: Enter message to continue/ Enter exit:")
    MESSAGE = "Hello from cleint 1"
    for i in range(1, 100): 
      status = str(i)+'\n'
      tcpClientB.send(status.encode())
      time.sleep(3)

    
tcpClientB.close()
