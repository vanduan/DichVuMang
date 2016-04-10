hours=-1
rate=-1
def pay(hours, rate):
    if hours>40:
        return (40*rate+(hours-40)*rate*1.5)
    else:
        return 40*rate
while (hours == -1):
    try:
        hours=raw_input('Enter Hours: ')
        hours=int(hours)
    except:
        print 'Error, please enter numberic input'
        hours=-1
while (rate==-1):
    try:
        rate=raw_input('Enter Rate: ')
        rate=float(rate)
    except:
        print 'Error, please enter numberic input'
        rate=-1
print 'Pay: ', pay(hours,rate)