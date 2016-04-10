__author__ = 'VanDuan - 13037321 - DHCNTT9A'

list=[]
while True:
    try:
        num=raw_input("Enter a number: ")
        if num=='done': break
        num=float(num)
        list.append(num)
    except:
        print 'Invalid input'

print '>>>Max:',max(list), '\n>>>Min:',min(list)

