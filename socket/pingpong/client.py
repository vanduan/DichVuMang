__author__ = 'VanDuan'
import socket
import sys
s = socket.socket()
host = socket.gethostname()
try:
	port = sys.argv[1:] #get port from commandline
	port.reverse()
	port = int(''.join(port)) #convert to integer
except:
	print '>>>>>>>>>>>>>>>>>used: python server.py <port>'
s.connect((host,port))
while True:
    buffer = 1024
    data_server = s.recv(buffer)
    print 'Server:',data_server
    data_client=raw_input('Client: ')
    s.send(data_client)
    if (data_client == 'bye' or data_client == 'Bye'):
        print s.recv(buffer)
        s.close()
        break