__author__ = 'VanDuan-13037321-DHCNTT9A'

file_name = raw_input('Enter a file name: ')

def addWord(line, listWord):
    temp = line.replace('\n','').split(' ')
    for word in temp:
        if word not in listWord:
            listWord.append(word)
try:
    list = []
    data = open(file_name)
    for line in data:
        addWord(line, list)
    #sap xep
    list.sort()
    print list
    data.close()
except:
    print 'Error!!!'