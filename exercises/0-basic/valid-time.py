def hora_correcta(h,m,s):
    return not( s!=int(s) or s<0 or s>60 or m!=int(m) or m<0 or m>60 or h!=int(h) or h<0 or h>24)