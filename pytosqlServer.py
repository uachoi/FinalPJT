import socket
#import pymysql
##import mysql
##pymysql.install_as_MySQLdb()
##connection=pymysql.connect(...)
import mysql.connector
from datetime import datetime

import cv2
import numpy as np


## box img + cvbelt img
def overlay_images(background,overlay,x,y):
	rows,cols,channels=overlay.shape
	roi=background[y:y+rows, x:x+cols]
	
	overlay_image=overlay[:, :, :3]
	mask=overlay[:, :, :3]
	
	background[y:y+rows, x:x+cols]=(overlay_image*(mask/255.0) +
									roi * (1.0 - mask / 255.0)).astype('uint8')


# png img read	
cvbelt=cv2.imread("cvresultimg.png")

bred_box=cv2.imread("rb_big.png",cv2.IMREAD_UNCHANGED)
sred_box=cv2.imread("rb_small.png",cv2.IMREAD_UNCHANGED)

bblue_box=cv2.imread("bb_big.png",cv2.IMREAD_UNCHANGED)
sblue_box=cv2.imread("bb_small.png",cv2.IMREAD_UNCHANGED)

# box: small
small_x,small_y,small_w,small_h=90,40,20,15

# box: big
big_x,big_y,big_w,big_h=110,60,40,30



now=datetime.now()
t_now=now.strftime('%Y-%m-%d %H:%M:%S')


##print(mysql.connector.__version__)

'''
db_config = {
    'user': 'root',
    'password': '0000',
    'host': 'localhost',  
    'database': 'ConveyorBelt',
    'port': '3306',
}
'''

HOST='192.168.0.12'
PORT=12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))  
server_socket.listen(5)

print('Server waiting...')

#Define color and size
RED='RED'
BLUE='BLUE'
BIG='BIG'
SMALL='SMALL'

conn = mysql.connector.connect(user='root',
                                password='0000',
                                host='localhost',
                               database='ConveyorBelt',
                                port='3306')
cursor = conn.cursor(prepared=True) #create cursor
query = "INSERT INTO cResult (productID,cRESULT,cTIME) VALUES (%s,%s,%s)" ##data insert
##print('Before the loop')

try:
    while True:
        client_socket, addr = server_socket.accept()  
        print(f'Client connecting: {addr}')    
    ##sys.stdout.flush()
    
        while True:
            data = client_socket.recv(1024).decode()
            if not data: #no data->quit loop
                break
            print(f'recv data: {data}') #msg from client
    
        #msg parsing
            query_params=dict(param.split('=',1) for param in data.split(', '))
            product_color=query_params['color']
            product_size=query_params['size']
            if product_color==RED: #11xx
                if product_size==SMALL:
                    product_id=1170
                    # img print
                    cv2.destroyAllWindows() #**
                    overlay_images(cvbelt,sred_box,small_x,small_y) #ADD box img
                    cv2.imshow("ConveyorBelt RESULT",cvbelt)
                    cv2.waitKey(500)#update img
                    ##
                    cvbelt=overlay_images(cvbelt,sred_box,small_x,small_y)
                    ##
                    
                elif product_size==BIG:
                    product_id=1190
                    # img print
                    cv2.destroyAllWindows() #**
                    overlay_images(cvbelt,bred_box,big_x,big_y) #ADD box img
                    cv2.imshow("ConveyorBelt RESULT",cvbelt)
                    cv2.waitKey(500)#update img
                    
                    ##
                    cvbelt=overlay_images(cvbelt,sred_box,big_x,big_y)
                    ##
                else:
                    product_id=1100
            elif product_color==BLUE:#22xx
                if product_size==SMALL:
                    product_id=2270
                    # img print
                    cv2.destroyAllWindows() #**
                    overlay_images(cvbelt,sblue_box,small_x,small_y) #ADD box img
                    cv2.imshow("ConveyorBelt RESULT",cvbelt)
                    cv2.waitKey(500) #update img
                    
                    ##
                    cvbelt=overlay_images(cvbelt,sblue_box,small_x,small_y)
                    ##
                elif product_size==BIG:
                    product_id=2290
                    # img print
                    cv2.destroyAllWindows() #**
                    overlay_images(cvbelt,bblue_box,big_x,big_y) #ADD box img
                    cv2.imshow("ConveyorBelt RESULT",cvbelt)
                    cv2.waitKey(500)#update img
                  
                    ##
                    cvbelt=overlay_images(cvbelt,big_box,big_x,big_y)
                    ##
                else:
                    product_id=2200
            else: #00xx
                if product_size==SMALL:
                    product_id=70
                elif product_size==BIG:
                    product_id=90
                else:
                    product_id=0
            
            product_id=int(product_id)
            
            result=f"ProductID: {product_id}, Color: {product_color}, Size: {product_size}"
    

        #values=(int(product_id),result,t_now)
    
    
            try:
                cursor.execute(query,(product_id, result,t_now))
                conn.commit()
                print("Record success")
            except mysql.connector.Error as err:
                print(f"error:{err}")
            
        client_socket.close()
except KeyboardInterrupt:
    exit
finally:
    cursor.close()
    conn.close()
    server_socket.close()




========================================================

/////// 라즈베리파이 IP: 192.163.0.12  //////
////// server


import socket
#import pymysql
##import mysql
##pymysql.install_as_MySQLdb()
##connection=pymysql.connect(...)
import mysql.connector
from datetime import datetime

now=datetime.now()
t_now=now.strftime('%Y-%m-%d %H:%M:%S')


##print(mysql.connector.__version__)

'''
db_config = {
    'user': 'root',
    'password': '0000',
    'host': 'localhost',  
    'database': 'ConveyorBelt',
    'port': '3306',
}
'''

HOST='192.168.0.12'
PORT=12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))  
server_socket.listen(5)

print('Server waiting...')

#Define color and size
RED='RED'
BLUE='BLUE'
BIG='BIG'
SMALL='SMALL'

conn = mysql.connector.connect(user='root',
                                password='0000',
                                host='localhost',
                               database='ConveyorBelt',
                                port='3306')
cursor = conn.cursor(prepared=True) #create cursor
query = "INSERT INTO cResult (productID,cRESULT,cTIME) VALUES (%s,%s,%s)" ##data insert
##print('Before the loop')

try:
    while True:
        client_socket, addr = server_socket.accept()  
        print(f'Client connecting: {addr}')    
    ##sys.stdout.flush()
    
        while True:
            data = client_socket.recv(1024).decode()
            if not data: #no data->quit loop
                break
            print(f'recv data: {data}') #msg from client
    
        #msg parsing
            query_params=dict(param.split('=',1) for param in data.split(', '))
            product_color=query_params['color']
            product_size=query_params['size']
            if product_color==RED: #11xx
                if product_size==SMALL:
                    product_id=1170
                elif product_size==BIG:
                    product_id=1190
                else:
                    product_id=1100
            elif product_color==BLUE:#22xx
                if product_size==SMALL:
                    product_id=2270
                elif product_size==BIG:
                    product_id=2290
                else:
                    product_id=2200
            else: #00xx
                if product_size==SMALL:
                    product_id=70
                elif product_size==BIG:
                    product_id=90
                else:
                    product_id=0
            
            product_id=int(product_id)
            
            result=f"ProductID: {product_id}, Color: {product_color}, Size: {product_size}"
    

        #values=(int(product_id),result,t_now)
    
    
            try:
                cursor.execute(query,(product_id, result,t_now))
                conn.commit()
                print("Recode success")
            except mysql.connector.Error as err:
                print(f"error:{err}")
            
        client_socket.close()
except KeyboardInterrupt:
    exit
finally:
    cursor.close()
    conn.close()
    server_socket.close()


----------------------------------------------------------

import socket
#import pymysql
##import mysql
##pymysql.install_as_MySQLdb()
##connection=pymysql.connect(...)
import mysql.connector
from datetime import datetime

now=datetime.now()
t_now=now.strftime('%Y-%m-%d %H:%M:%S')


##print(mysql.connector.__version__)

'''
db_config = {
    'user': 'root',
    'password': '0000',
    'host': 'localhost',  
    'database': 'ConveyorBelt',
    'port': '3306',
}
'''

HOST='192.168.0.12'
PORT=12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))  
server_socket.listen(5)

print('Server waiting...')

#Define color and size
RED='RED'
BLUE='BLUE'
BIG='BIG'
SMALL='SMALL'

conn = mysql.connector.connect(user='root',
                                password='0000',
                                host='localhost',
                                database='ConveyorBelt',
                                port='3306')
cursor = conn.cursor(prepared=True) #create cursor
query = "INSERT INTO cResult (productID,cRESULT,cTIME) VALUES (%s,%s,%s)" ##data insert
##print('Before the loop')

try:
    while True:
        client_socket, addr = server_socket.accept()  
        print(f'Client connecting: {addr}')    
    ##sys.stdout.flush()
    
        while True:
            data = client_socket.recv(1024).decode()
            if not data: #no data->quit loop
                break
            print(f'recv data: {data}') #msg from client
    
        #msg parsing
            query_params=dict(param.split('=',1) for param in data.split(', '))
            product_color=query_params['color']
            product_size=query_params['size']
            if product_color==RED: #11xx
                if product_size==SMALL:
                    product_id=1170
                elif product_size==BIG:
                    product_id=1190
                else:
                    product_id=1100
            elif product_color==BLUE:#22xx
                if product_size==SMALL:
                    product_id=2270
                elif product_size==BIG:
                    product_id=2290
                else:
                    product_id=2200
            else: #00xx
                if product_size==SMALL:
                    product_id=70
                elif product_size==BIG:
                    product_id=90
                else:
                    product_id=0
            
            product_id=int(product_id)
            
            result=f"ProductID: {product_id}, Color: {product_color}, Size: {product_size}"
    

        #values=(int(product_id),result,t_now)
    
    
            try:
                cursor.execute(query,(product_id, result,t_now))
                conn.commit()
                print("Recode success")
            except mysql.connector.Error as err:
                print(f"error:{err}")
            
        client_socket.close()
except KeyboardInterrupt:
    exit
finally:
    cursor.close()
    conn.close()
    server_socket.close()



==========================

import socket
##import mysql
##pymysql.install_as_MySQLdb()
##connection=pymysql.connect(...)
import pymysql
import mysql.connector

##print(mysql.connector.__version__)

db_config = {
    'user': 'root',
    'password': '0000',
    'host': 'localhost',  
    'database': 'ConveyorBelt',
    'port': '3306',
}

HOST='192.168.0.12'
PORT=12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))  
server_socket.listen(5)

print('Server waiting...')


##print('Before the loop')

while True:
    client_socket, addr = server_socket.accept()  
    print(f'Client connecting: {addr}')
    ##sys.stdout.flush()

    data = client_socket.recv(1024).decode() 
    print(f'recv data: {data}') ##

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = "INSERT INTO cRESULT (cRESULT,cTIME) VALUES (%s,%s)" ##
    values = (msg,datetime.now())

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    client_socket.close()




=========================================

import socket
import mysql.connector


db_config = {
    'user': 'root',
    'password': '0000',
    'host': 'localhost',  
    'database': 'ConveyorBelt',
    'port': '3306',
}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.0.3', 1111))  
server_socket.listen(5)

print('Server waiting...')

while True:
    client_socket, addr = server_socket.accept()  
    print(f'Client connecting: {addr}')

    data = client_socket.recv(1024).decode() 
    print(f'recv data: {data}') ##

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = "INSERT INTO cRESULT (cRESULT,cTIME) VALUES (%s,%s)" ##
    values = (msg,datetime.now())

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    client_socket.close()  

-------------------------------------------------------------

import mysql.connector
from datetime import datetime
import time

# MySQL connect
config = {
    'user': 'root',
    'password': '0000',
    'host': 'localhost',
    'database': 'conveyorBelt',
    'port': '3306',
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

def insert_data(r_id, obj_name):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # SQL query
    query = "INSERT INTO cResult(resultID, productID, cRESULT, cTIME) VALUES (%s, %s, %s)"
    values = (r_id, p_id, c_result, c_time)

    cursor.execute(query, values)
    conn.commit()
    print("Data inserted successfully!")

# real-time data transfer
while True:
    # Collecting data from sensor)
    resultID = 1
    object_name = "Object_A"

    # func: insert data
    insert_data(object_id, object_name)

    # loop 
    time.sleep(5)  # 5sec
