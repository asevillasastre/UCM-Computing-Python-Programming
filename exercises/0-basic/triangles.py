#ordenar 3 elemenos#
a,b,c = 2,3,5**(1/2)
if (a>= b):
    if (a>= c):
        d=a
        if b>=c:
            e=b
            f=c
        if c>=b:
            e=c
            f=b
if (b>= a):
    if (b>=c):
        d=b
        if a>=c:
            e=a
            f=c
        if c>=a:
            e=c
            f=a
if (c>= a):
    if (c>=b):
        d=c
        if a>=b:
            e=a
            f=b
        if b>=a:
            e=b
            f=a
#tipo de triángulo#
if (d> e+f):
    print ("no triángulo")
else:
    print ("triángulo")
    if (d==e==f):
        print ("equilátero")
    if (d==e):
        if (e>f):
           print ("isósceles")
    if (d>e):
        if (e==f):
            print ("isósceles")
        if (e>f):
            print ("escaleno")
