import socket
import pymysql

db = pymysql.connect(host='localhost',user='root',password='',db='watertank')
cursor=db.cursor()


def server_program():

    
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        #print("Length of the data is in byte: ")
        #print(len(data))
        print("21th and 22nd data in bytearray: " +data[20] + " " + data[21])
        if not data:
          break
        print("from connected user: "+str(data))
        status = data[21]
        device_id = data[2:13]
        print("Device ID: "+device_id+"   "+"New Status: "+status) 
        #sql = "INSERT INTO tank_status(device_id,tank_status) VALUES ('%s','%s')" %(status,device_id)
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
                    
            #data = input(' -> ')
            #conn.send(data.encode())  # send data to the client
    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()

