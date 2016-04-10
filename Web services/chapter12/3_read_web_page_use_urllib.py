__author__ = 'VanDuan'
import re
import urllib

count_char = 3000
count_temp = 0

# lay url
print 'Nhap URL: Vd:  http://www.py4inf.com/code/romeo.txt'
print '               http://allendowney.com/'
print '               http://www.lib.umich.edu/espresso-book-machine'
url = raw_input('==>: ')

print '============================================================'
print '============================================================'
# kiem tra url
check_http = re.findall('http://.*',url)
if len(check_http)==0:
    print '==> Thieu http://'
    exit()
else:
    try:
        # ket noi
        connect = urllib.urlopen(url)
        # lay du lieu
        data = connect.fp
        # xu li
        for line in data:
            if count_temp <= count_char:
                count_temp += len(line)
                print line.replace('\n','')
            else:
                temp = count_char - count_temp
                count_temp += temp
                print line[0:temp].replace('\n','')
                break

        print '============================================================'
        print '============================================================'
        print '==> Tong so ki tu: ',count_temp
        connect.close()
    except:
        print '==> Error!!! Xui thoi, hen thi quen di.....'
