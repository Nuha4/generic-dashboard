# Python TCP Client A
import socket 

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 65536
#MESSAGE = raw_input("tcpClientA: Enter message/ Enter exit:") 
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect(('127.0.0.1', port))

#while MESSAGE != 'exit':
    #tcpClientA.send(MESSAGE)     
    #data = tcpClientA.recv(BUFFER_SIZE)
    #print " Client1 received data:", data
    #MESSAGE = raw_input("tcpClientA: Enter message to continue/ Enter exit:")
	
for i in range(1, 100): 
	status = str(i)+'. '
	tcpClientA.send(status)
	if i%2==0:
		status = '0'+' '
		tcpClientA.send(status)
	else:
		status = '1'+' '
		tcpClientA.send(status)
	tcpClientA.send('\n')
 
#tcpClientA.send('\n')	
tcpClientA.close() 