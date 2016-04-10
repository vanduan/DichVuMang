import math
novalue=-0.834987284351
a=novalue
b=novalue
c=novalue
delta=-1
print '     ++++ Giai phuong trinh bac 2 ++++'
print '    Nhap he so:'
while (a==novalue):
    try:
        a=raw_input('    a = ')
        a=float(a)
    except:
        print '     Chi nhap so!!!'
        a=novalue
while (b==novalue):
    try:
        b=raw_input('    b = ')
        b=float(b)
    except:
        print '     Chi nhap so!!!'
        b=novalue
while (c==novalue):
    try:
        c=raw_input('    c = ')
        c=float(c)
    except:
        print '     Chi nhap so!!!'
        c=novalue
# in phuong trinh
print '\n    >>>PT: (',a,')x^2 + (',b,')x + (',c,') = 0'
# tinh toan

if a==0:
    if b==0:
        if c==0:
            print '     Phuong trinh co vo so nghiem'
else:
    delta = b*b - (4*a*c)
    print '     Delta =',delta
    if delta<0:
        print '     Phuong trinh vo nghiem:'
    elif delta ==0:
        print '     Phuong trinh co 2 nghiem kep:'
        print '     x1 = x2 =',-(b/(2*a))
    else:
        print '     Phuong trinh co 2 nghiem:'
        print '     x1 =',(-b + sqrt(delta))/(2*a)
        print '     x2 =',(-b - sqrt(delta))/(2*a)
