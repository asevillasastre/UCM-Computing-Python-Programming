año=2400
a=año%4
b=año%100
c=año%400
if (a==0 and b!=0) or (b==0 and c==0):
    print ("bisiesto")
if a!=0 or (b==0 and c!=0):
    print ("no bisiesto")