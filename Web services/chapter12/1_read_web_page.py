__author__ = 'VanDuan'
import socket
import re

# lay url
print 'Nhap URL: Vd:  http://www.py4inf.com/code/romeo.txt'
print '               http://allendowney.com/'
print '               http://www.lib.umich.edu/espresso-book-machine'

url = raw_input('==>: ')

# kiem tra url
check_http = re.findall('http://.*',url)
if len(check_http)==0:
    print '==> Thieu http://'
    exit()
else:
    # tach host, path
    urls = url.split('/')
    host = urls[2]
    print '==> Host: ', host
    path = ''
    for i in range(3, len(urls)):
        path +='/' + urls[i]
    print '==> Path: ', path

    try:
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host,80))
        get = 'GET http://' + host + path + ' HTTP/1.0\n\n'
        print '==>', get
        print '============================================================'
        print '============================================================'
        mysock.send(get)

        while 1:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            print data
        mysock.close()

        print '============================================================'
        print '============================================================'
    except:
        print '==> Error!!! Xui thoi, hen thi quen di.....'

