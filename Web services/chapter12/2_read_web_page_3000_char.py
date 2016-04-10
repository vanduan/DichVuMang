__author__ = 'VanDuan'
import socket
import re

count_char = 3000
count_temp = 0

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

        first = True
        buffer = 1024
        while 1:
            data = mysock.recv(buffer)
            if count_temp+len(data) <= 3000:
                # tach rieng phan header ra o phan data dau tien nhan duoc
                if first:
                    data = data.split('\r\n\r\n')
                    # neu data co hai phan {'header','text content'}
                    if len(data)==2:
                        print data[1]
                        count_temp += len(data[1])
                    # neu data chi co 1 phan {'header'}
                    else:
                        #print data[0]
                        count_temp += len(data[0])
                    first = False
                else:
                    if len(data) < 1:
                        break
                    print data
                    count_temp += len(data)
            else:
                temp = count_char - count_temp
                print data[0:temp]
                count_temp += temp
                break

        print '============================================================'
        print '============================================================'
        print '==> Tong so ki tu: ',count_temp
        mysock.close()
    except:
        print '==> Error!!! Xui thoi, hen thi quen di.....'
