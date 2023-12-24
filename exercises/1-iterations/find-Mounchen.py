
def f(n):
    suma=0
    m=n
    while n>0:
        polla = (n%10)**(n%10)
        if (n%10) == 0:
            polla = 0
        suma= suma + polla
        n= n//10
    return suma == m

def g(n):
    while f(n) == False:
        n=n+1
    return n
