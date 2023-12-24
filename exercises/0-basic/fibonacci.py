def fibonacci(x):

    n,m=0,1
    p=x
    
    while p>2:
        p=p-1
        q=m
        m=m+n
        n=q
        x=m
    return x