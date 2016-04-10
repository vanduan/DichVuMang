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
	print '>>>>>>>>>>>>>>>>>>>used: python server.py <port>'
#print port
s.bind((host,port))
s.listen(5) #connection 0-5
print 'Server is running'
while True:
    print 'Waitting connect from client...'
    c, addr = s.accept()
    print 'Connect from:',addr
    c.send('<<< You connected to Server -- Type "bye" to Disconnect>>>')
    buffer = 1024
    while True:
        data_client = c.recv(buffer)
        print 'Client: ',data_client
        if (data_client=='bye' or data_client=='Bye'):
            c.send('Disconnected')
            c.close()
            break
        data_ser = raw_input('Server: ')
        c.send(data_ser)