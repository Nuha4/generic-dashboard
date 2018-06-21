#from multiprocessing.pool import ThreadPool
import socket
#import concurrent.futures
#from concurrent.futures 
from concurrent.futures import ThreadPoolExecutor
#import ThreadPoolExecutor
from enum import Enum

HOST = ''
PORT = 2004

	
ProcessingState = Enum('ProcessingState', 'WAIT_FOR_MSG IN_MSG')

def serve_connection(sockobj, client_address):
    print('{0} connected'.format(client_address))
    sockobj.sendall(b'*')
    state = ProcessingState.WAIT_FOR_MSG

    while True:
        try:
            buf = sockobj.recv(1024)
            print(buf.decode())
            if not buf:
                break
        except IOError as e:
            break
        for b in buf:
            if state == ProcessingState.WAIT_FOR_MSG:
                if b == ord(b'^'):
                    state = ProcessingState.IN_MSG
            elif state == ProcessingState.IN_MSG:
                if b == ord(b'$'):
                    state = ProcessingState.WAIT_FOR_MSG
                else:
                    sockobj.send(bytes([b + 1]))
            else:
                assert False

    print('{0} done'.format(client_address))
    sys.stdout.flush()
    sockobj.close()
	

def main():	
	print("SERVER is lisitening")
	pool = ThreadPoolExecutor(max_workers=4)
	print("pool is lisitening")
	sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sockobj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sockobj.bind(('', PORT))
	sockobj.listen(15)
	print("SERVER is lisitening")

	try:
		while True:
			client_socket, client_address = sockobj.accept()
			pool.submit(serve_connection, client_socket, client_address)
	except KeyboardInterrupt as e:
		print(e)
		sockobj.close()

if __name__ == '__main__':
    main()
