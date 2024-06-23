##py to sql
import socket
import mysql.connector
from datetime import datetime
'''
db_config={
    'user':'root', ##?
    'password': '0000',
    'host':'localhost',
    'database':'ConveyorBelt',
    'port':'3306',
}
'''

#socket
server_addr=('192.168.0.12',12345)
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(server_addr)



...

 ##send to db
def send_to_db(msg):
    '''
    conn=mysql.connector.connect(user='root',
                                 password='0000',
                                 host='localhost',
                                 database='ConveyorBelt',
                                 port='3306') #err
    cursor=conn.cursor()
    query="INSERT INTO cResult(cRESULT,cTIME) VALUES(%s,%s)" ##resultID is auto
    values=(msg,datetime.now()) ##datetime->timestamp
    '''
    
    client_socket.send(str(msg).encode('utf-8'))
    
    #cursor.execute(msg)
    #conn.commit()
    
    #cursor.close()
    #conn.close()    
   

...


if checkB<10 and np.sum(mask_blue > 0) > 1300:
            checkB+=1
            if checkB>9:
                if Wdata>=20 and Wdata<70:
                    print('add B1')
                    
                    msg="color=BLUE , size=SMALL(>=20,<70)"
                    send_to_db(msg)
                    
                    colorList.append('B1')
                    print(colorList)
                elif Wdata>=70 and Wdata<110:
                    print('add B2')
                    
                    msg="color=BLUE , size=BIG(>=70,<110)"
                    send_to_db(msg)
                    
                    colorList.append('B2')
                    print(colorList)
        elif checkR<10 and np.sum(mask_red > 0) > 1300:
            checkR+=1
            if checkR>9:
                if Wdata>=20 and Wdata<70:
                    print('add R1')
                    
                    msg="color=RED , size=SMALL(>=20,<70)"
                    send_to_db(msg) ## err
                    
                    colorList.append('R1')
                    print(colorList)
                elif Wdata>=70 and Wdata<110:
                    print('add R2')
                    
                    msg="color=RED , size=SMALL(>=70,<110)"
                    send_to_db(msg)
                    
                    colorList.append('R2')
                    print(colorList)
