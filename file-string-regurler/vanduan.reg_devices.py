__author__ = 'VanDuan - 13037321 - DHCNTT9A'

import re
file_name='list-of-computer-devices.htm'
list_devices = []
try:
    f=open(file_name)
    data=f.read()
    data.strip()
    pattern='[0-9]\.\s+(.*)'
    data = re.findall(pattern,data)
    print '>>> Both Input OutPut Devices: '
    for temp in data:
        while ('<' in list(temp) and '>' in list(temp)):
            begin=temp.find('<')
            end=temp.find('>')+1
            temp=temp[:begin]+temp[end:]

        if temp!='':
            list_devices.append(temp)
    for device in list_devices:
        print '>>>  ',device
    f.close()
except:
    print 'Error!!!'