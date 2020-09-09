import os
import socket
def IsAvailable(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        # print '%d available~' % port #py2
        print ('%d available~' % port) #py3
        return True
    except:
        # print '%d is busy!' % port #py2
        print ('%d is busy!' % port) #py3
        return False
if __name__ == '__main__':
    IsAvailable('167.99.74.88',80)#input here
