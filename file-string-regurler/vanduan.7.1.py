__author__ = 'VanDuan-13037321-DHCNTT9A'

file_name = raw_input('Enter a file name: ')

try:
    data = open(file_name)
    for line in data:
        print line.upper().replace('\n','')
    data.close()
except:
    print 'Error!!!'