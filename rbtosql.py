import socket
import mysql.connector
from datetime import datetime

now=datetime.now()
t_now=now.strftime('%Y-%m-%d %H:%M:%S')

HOST='192.168.0.12'
PORT=11111

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen(5)

print('Server waiting ...')

##define

conn=mysql.connector.connect(user='root', password='0000',
                             database='ConveyorBelt',port='3306')
cursor=conn.cursor(prepared=True) #create cursor

##data insert
query1="INSERT INTO rResult (rLINE,curLOC,rTIME) VALUES (%s,%s,%s)"

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
            
            #parsing
            query_params=dict(param.split('=',1) for param in data.split(', '))
            line_color=query_params['rLINE']
            robot_loc=query_params['LOC']
            
            result=f"LineColor: {line_color}, Location: {robot_loc}"
            
            try:
                cursor.execute(query,(line_color,robot_loc,t_now))
                conn.commit()
                print("Record Success")
            except mysql.connector.Error as err:
                print(f"error:{err}")
            
        client_socket.close()
        
except KeyboardInterrupt:
    exit
finally:
    cursor.close()
    conn.close()
    server_socket.close()




=================================================

import socket
import mysql.connector
from datetime import datetime

now=datetime.now()
t_now=now.strftime('%Y-%m-%d %H:%M:%S')

HOST='192.168.0.12'
PORT=11111

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen(5)

print('Server waiting ...')

##define

conn=mysql.connector.connect(user='root', password='0000',
                             database='ConveyorBelt',port='3306')
cursor=conn.cursor(prepared=True) #create cursor

##data insert
query1="INSERT INTO "

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
            
            
            
            
            
        client_socket.close()
except KeyboardInterrupt:
    exit
finally:
    cursor.close()
    conn.close()
    server_socket.close()

