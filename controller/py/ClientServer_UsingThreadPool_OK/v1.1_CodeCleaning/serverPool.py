import socket
from concurrent.futures import ThreadPoolExecutor
from enum import Enum

HOST = ''
PORT = 2004

ProcessingState = Enum('ProcessingState', 'WAIT_FOR_MSG IN_MSG')

def serve_connection(sockobj, client_address):
    print('{0} connected'.format(client_address))
    sockobj.sendall(b'Hello')
    state = ProcessingState.WAIT_FOR_MSG

    while True:
        try:
            buf = sockobj.recv(1024)
            print(buf.decode())
            if not buf:
                break
        except IOError as e:
            break

    print('{0} done'.format(client_address))
    sys.stdout.flush()
    sockobj.close()
	

def main():	
	pool = ThreadPoolExecutor(max_workers=10)
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
