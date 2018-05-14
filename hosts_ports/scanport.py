import os
import socket
def ScanPort(address, start_port, end_port):
	available_ports=[]
	for port in range(start_port,end_port):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		try:
			s.connect((address,int(port)))
			s.shutdown(2)
			print("%d available!" %port)
		except:
			# print("%d is busy" %port)
			pass
	if not available_ports:
		print("Ports are all freaking busy")

if __name__ == '__main__':
	ScanPort("127.0.0.1",7776,7778)