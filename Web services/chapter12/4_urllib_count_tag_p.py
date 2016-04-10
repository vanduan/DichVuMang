__author__ = 'VanDuan'

import re
import urllib

# lay url
print 'Nhap URL: Vd:  http://www.py4inf.com/code/romeo.txt'
print '               http://allendowney.com/'
print '               http://www.lib.umich.edu/espresso-book-machine'
url = raw_input('==>: ')

print '========================='
print '========================='
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
        count_tag_p = 0
        pattern = '<p>.[^\^&nbsp;$].+?'
        for line in data:
            list_tag_p = re.findall(pattern,line)
            count_tag_p += len(list_tag_p)
        print '==> So doan van ban: ', count_tag_p
        connect.close()
    except:
        print '==> Error!!! Xui thoi, hen thi quen di.....'
