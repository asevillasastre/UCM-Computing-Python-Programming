(x1,y1)=2,3
(x2,y2)=2,5
(x3,y3)=8,3
(x4,y4)=8,5

if x1>=x2:
    mx1=x2
else:
    mx1=x1
    
if y1>=y2:
    yx1=y2
else:
    my1=y1

if x3>=x4:
    mx2=x4
else:
    mx2=x2
    
if y3>=y4:
    my2=y4
else:
    my2=y2


(c1,c2)=abs(x1-x2)/2+mx1,abs(y1-y2)/2+my1
(c3,c4)=abs(x3-x4)/2+mx2,abs(y3-y4)/2+my2

print (c1,c2,c3,c4)