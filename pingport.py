import os
import socket
def IsAvailable(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        print '%d available~' % port
        return True
    except:
        print '%d is busy!' % port
        return False
if __name__ == '__main__':
    IsAvailable('127.0.0.1',8080)#input here
