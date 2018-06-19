# Python TCP Client B
import socket 

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 4096 
#MESSAGE = raw_input("tcpClientB: Enter message/ Enter exit:")
 
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientB.connect(('127.0.0.1', port))

#while MESSAGE != 'exit':
#    tcpClientB.send(MESSAGE)     
#    data = tcpClientB.recv(BUFFER_SIZE)
#    print " Client2 received data:", data
#    MESSAGE = raw_input("tcpClientB: Enter message to continue/ Enter exit:")

	
for i in range(200, 300): 
	status = str(i)+' '
	tcpClientB.send(status)
		
tcpClientB.close()