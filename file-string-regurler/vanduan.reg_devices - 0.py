
import re
file_name='list-of-computer-devices.htm'
list_devices = []
try:
    f=open(file_name)
    data=f.read()
    pattern_1='Input Devices.*:'
    pattern_2='OUTPUT DEVICES.*:+'

    #find text
    text_begin = re.findall(pattern_1,data)
    #>>>['Input Devices</span></strong>:', 'Input D...']
    text_end = re.findall(pattern_2,data)
    #>>>['OUTPUT DEVICES</strong>:']

    # get index of text
    index_begin = data.find(text_begin[0])
    index_end = data.find(text_end[0])
    # get data content OUTPUT DEVICES
    data = data[index_begin:index_end]
    #print data
    data = re.findall('<p>[a-z].*',data)
    #print data
    for line in data:
        temp=re.findall('\s([a-zA-Z].*)<',line)
        list_devices.append(temp[0])

    print '>>>Input Devices:'
    for device in list_devices:
        print '>>>  ',device
    f.close()
except:
    print 'Error!!!'