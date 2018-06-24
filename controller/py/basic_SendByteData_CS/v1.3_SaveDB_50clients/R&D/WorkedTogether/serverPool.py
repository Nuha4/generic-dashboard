import socket
from concurrent.futures import ThreadPoolExecutor
from enum import Enum
import pymysql

db = pymysql.connect(host='localhost',user='root',password='',db='watertank')
cursor=db.cursor()

HOST = socket.gethostname()
PORT = 2004

ProcessingState = Enum('ProcessingState', 'WAIT_FOR_MSG IN_MSG')

def serve_connection(sockobj, client_address):
    print('{0} connected'.format(client_address))
    #sockobj.sendall(b'Hello')
    state = ProcessingState.WAIT_FOR_MSG

    while True:
        try:
            data = sockobj.recv(1024)
            print(data.decode())
            print("21th and 22nd data in bytearray: " +data[20] + " " + data[21])
            print("from connected user: "+str(data))
            status = data[21]
            device_id = data[2:13]
            print("Device ID: "+device_id+"   "+"New Status: "+status)
            sql="UPDATE tank_status SET tank_status='%s' WHERE device_id='%s'" %(status,device_id)
            cursor.execute(sql)
            db.commit()
            if status == '0':
            
                sql="UPDATE tank_status SET expected_time_empty='0' WHERE device_id='%s'" %(device_id)
                cursor.execute(sql)
                db.commit()

                notification = "Tank Id: "+device_id+" is Empty."
                print(notification)
                sql1= "INSERT INTO tank_notification(device_id,notification,danger,seen) VALUES ('%s','%s','1','0')" %(device_id,notification)
                cursor.execute(sql1)
                db.commit()
            elif status == '1':
            
                sql="UPDATE tank_status SET expected_time_empty='24' WHERE device_id='%s'" %(device_id)
                cursor.execute(sql)
                db.commit()

                notification = "Tank Id: "+device_id+" is Full."
                print(notification)
                sql1= "INSERT INTO tank_notification(device_id,notification,danger,seen) VALUES ('%s','%s','0','0')" %(device_id,notification)
                cursor.execute(sql1)
                db.commit()

                sql2= "UPDATE tank_notification SET danger='0' WHERE device_id='%s'" %(device_id)
                #sql2= "DELETE from tank_notification WHERE device_id='%s'" %(device_id)
                cursor.execute(sql2)
                db.commit()
            
            if not data:
                break
        except IOError as e:
            break

    print('{0} done'.format(client_address))
    sys.stdout.flush()
    sockobj.close()
	

def main():	
	pool = ThreadPoolExecutor(max_workers=50)
	sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sockobj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sockobj.bind((HOST, PORT))
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
