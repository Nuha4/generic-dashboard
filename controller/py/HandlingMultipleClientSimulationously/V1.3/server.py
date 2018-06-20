import socket
import threading
import time
from threading import Thread 
from socketserver import ThreadingMixIn 


def handle(conn_addr):
  print("Someone Connected")
  time.sleep(12)
  #print("And now I die")
  while True: 
      data = args.recv(2048)
      print("Server received data:", data.decode())
      #MESSAGE = raw_input("Multithreaded Python server : Enter Response from Server/Enter exit:")
      MESSAGE = "Reply from Server - Hello"
      if MESSAGE == 'exit':
        break
      conn.send(MESSAGE.encode())  # echo 


host = ''
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
  s.bind(('',port))
except socket.error as e:
  print(str(e))

s.listen(2)

while True:
  #threading.Thread(handle(s.accept())).start()
  print("Multithreaded Python server : Waiting for connections from TCP clients...")
  (conn, (ip,port)) = tcpServer.accept()
  #threading.Thread(target=handle, args=(s.accept(),)).start()
  threading.Thread(target=handle, args=(s.accept(),)).start()


print("Should never be reached")
