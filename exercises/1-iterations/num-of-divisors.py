def dx(n):
    lista=[]
    exp=0
    while n>1:
        d=2
        while n%d!=0 and n!=d:
            d+=1
        n=n/d
        a=d        
        if a==d:
            exp+=1
        else:
            lista.append(d,exp)
            exp=0
    return exp