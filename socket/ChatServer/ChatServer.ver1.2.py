__author__ = 'VanDuan'
#use telnet localhost 9999
import socket
import select

class ChatServer:

    def __init__(self, port):
        self.port = port
        # recv line message
        self.msg=''

        self.srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srvsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srvsock.bind(("", port))
        self.srvsock.listen(5)

        self.descriptors = [self.srvsock]
        print 'ChatServer started on port ',port

    def run(self):
        while True:
            (sread, swrite, sexc) = select.select(self.descriptors, [], [])
            for sock in sread:
                if sock == self.srvsock:
                    self.accept_new_connection()
                else:
                    # recv character
                    str = sock.recv(100)
                    self.msg=self.msg+str
                    if str == '':
                        host,port = sock.getpeername()
                        str = 'Client left %s:%s\r\n' % (host, port)
                        self.broadcast_string( str, sock )
                        sock.close
                        self.descriptors.remove(sock)
                    elif self.msg[len(self.msg)-1:len(self.msg)] =='\n':
                        host,port = sock.getpeername()
                        newstr = '[%s:%s] %s' % (host, port, self.msg)
                        # to get new message
                        self.msg=''
                        self.broadcast_string(newstr, sock)
    def accept_new_connection( self ):
        newsock, (remhost, remport) = self.srvsock.accept()
        self.descriptors.append( newsock )
        newsock.send("You're connected to the Python chatserver\r\n")
        str = 'Client joined %s:%s\r\n' % (remhost, remport)
        self.broadcast_string( str, newsock )
    def broadcast_string(self, str, omit_sock ):
        for sock in self.descriptors:
            if sock != self.srvsock and sock != omit_sock:
                sock.send(str)
        print str

myServer = ChatServer(9999).run()