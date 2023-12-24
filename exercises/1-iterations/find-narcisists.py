def f(n):
    suma=0
    m=n
    ñ=n
    cifras =0
    while ñ>0:
        ñ = ñ//10
        cifras = cifras +1
    while n>0:
        polla = (n%10)**cifras
        suma= suma + polla
        n= n//10
    return suma == m

def g(n):
    while f(n) == False:
        n=n+1
    return n
