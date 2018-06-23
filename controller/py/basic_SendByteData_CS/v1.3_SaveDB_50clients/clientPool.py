# Python TCP Client B
import socket
import time

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
#MESSAGE = raw_input("tcpClientB: Enter message/ Enter exit:")
#MESSAGE = "Hello from cleint"
 
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientB.connect(('127.0.0.1', port))
  
while True:
    message = '01010101010101010100000'
    tcpClientB.send(message.encode())  # send message
    time.sleep(2)
    #data = client_socket.recv(1024).decode()  # receive response
    #print('Received from server: ' + data)  # show in terminal
    #message = input(" -> ")  # again take input
    #client_socket.close()  # close the connection
tcpClientB.close()
