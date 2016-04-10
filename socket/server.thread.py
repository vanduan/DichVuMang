__author__ = 'VanDuan'
import SocketServer
from SocketServer import ThreadingTCPServer
import sys
host = SocketServer.gethostname()
port = sys.argv[1:] #get port from commandline
port.reverse()
port = int(''.join(port)) #convert to integer
#print port
server = ThreadingTCPServer((''))
