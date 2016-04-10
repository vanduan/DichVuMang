__author__ = 'VanDuan'
count=0
sum=0
max=-9999999999999999999
min=9999999999999999999
def average(sum, count):
    if count==0:
        return 0
    return sum/count
while True:
    try:
        num=raw_input("Enter a number: ")
        if num=='done': break
        num=float(num)
        sum=sum+num
        count=count+1
        if max<num:
            max=num
        if min>num:
            min = num
    except:
        print 'Invalid input'

print 'Sum:', sum, '\nCount:',count, '\nAverage:',average(sum,count), '\nMax:',max, '\nMin:',min


