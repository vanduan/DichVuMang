__author__ = 'VanDuan - 13037321 - DHCNTT9A'

import re
file_name='list-of-computer-devices.htm'
list_devices = []
try:
    f=open(file_name)
    data=f.read()
    pattern_1='OUTPUT.*:'
    pattern_2='Both Input OutPut Devices.*:'

    #find text
    text_begin = re.findall(pattern_1,data)
    #>>>['OUTPUT DEVICES</strong>:']
    text_end = re.findall(pattern_2,data)
    #>>>['Both Input OutPut Devices</strong>:']

    # get index of text
    index_begin = data.find(text_begin[0])
    index_end = data.find(text_end[0])
    # get data content OUTPUT DEVICES
    data = data[index_begin:index_end]
    #print data
    data = re.findall('<li>.*',data)
    for line in data:
        line = line[4:len(line)-5]
        list_devices.append(line)

    print '>>>OUTPUT  DEVICES:'
    for device in list_devices:
        print '>>>  ',device
    f.close()
except:
    print 'Error!!!'