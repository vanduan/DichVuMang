__author__ = 'VanDuan'
#use telnet localhost <port>

import socket
import select
import sys

class ChatServer:
    #constructor
    def __init__(self, port):
        self.port = port
        # dung de lay tin nhan tren mot dong tu client
        self.msg_temp = ''
        # tu dien luu socket:username
        self.username = {'':''}

        self.srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srvsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srvsock.bind(("", port))
        self.srvsock.listen(5)

        self.descriptors = [self.srvsock]
        print 'ChatServer started on port ',port
    #phan xu li o day
    def run(self):
        while True:
            (sread, swrite, sexc) = select.select(self.descriptors, [], [])
            for sock in sread:
                if sock == self.srvsock:
                    self.accept_new_connection()
                else:
                    # recv character

                    my_str = sock.recv(100)
                    self.msg_temp=self.msg_temp+my_str
                    if my_str == '':
                        host,port = sock.getpeername()
                        my_str = '<%s left >\r\n' % (self.username[host+str(port)])
                        self.broadcast_string(my_str, sock )
                        sock.close
                        self.descriptors.remove(sock)
                    elif self.msg_temp[len(self.msg_temp)-1:len(self.msg_temp)] =='\n':
                        host, port = sock.getpeername()
                        newstr = '%s : %s\r\n' % (self.username[host+str(port)], self.msg_temp[0:len(self.msg_temp)-2])
                        # xoa tin nhan tam
                        self.msg_temp =''
                        self.broadcast_string(newstr, sock)
    def accept_new_connection( self ):
        newsock, (remhost, remport) = self.srvsock.accept()
        self.descriptors.append( newsock )
        newsock.send("You're connected to the Python chatserver\r\n")
        # yeu cau client nhap username
        newsock.send("Enter your username: ")
        username = ''
        # nhan tung ki tu cho toi khi gap dau enter
        while True:
            username += newsock.recv(100)
            if username[len(username)-1:len(username)]=='\n':
                # kiem tra neu client khong nhap username
                if len(username)==2:
                    newsock.send('Enter username, please!  => ')
                    username = ''
                else:
                    break
        
        # them socket:username vao tu dien username
        host_1, port_1 = newsock.getpeername()
        self.username[host_1+str(port_1)]= username[0:len(username)-2]
        # lay username tuong ung voi sockname => self.username[newsock.getsockname]
        my_str = '[%s joined]\r\n' % (self.username[host_1+str(port_1)])
        self.broadcast_string( my_str, newsock )
    def broadcast_string(self, str, omit_sock ):
        for sock in self.descriptors:
            if sock != self.srvsock and sock != omit_sock:
                sock.send(str)
        print str
try:
    my_port = sys.argv[1:] #get port from commandline
    my_port.reverse()
    my_port = int(''.join(my_port)) #convert to integer
except:
    my_port=9999
myServer = ChatServer(my_port).run()