n=-1
while (n==-1):
    try:
        n=raw_input('   Nhap n = ')
        n=int(n)
    except:
        print '     Chi nhap so!!!'
        n=-1
if n<2:
    print '    SNT: null'
elif n==2:
    print '    SNT: 2'
else:
    flag=1
    for i in range(n):
        if i>2:
            k=2
            for k in range(i/2):
                if k!=0:
                    if (i%k)==0:
                        flag=0
            if flag==1:
                print '     ',i
        flag=1
       