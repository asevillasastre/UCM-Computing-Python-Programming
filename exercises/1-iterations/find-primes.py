def isprime(n):
    """
    auxiliar
    """
    if n==1:
        return False
    t=2
    while n%t!=0 and n!=t:
        t=t+1
    return n==t

def unpuñaodeprimos(lista,cuantos):
    while cuantos>0:
        i=0
        n=lista[len(lista)-1]+1
        eureka=False
        while not eureka:
            while i<len(lista)-1 and n%lista[i]!=0:
                i+=1
            if i==len(lista)-1:
                eureka=True
            i=0
            n+=1
        lista.append(n-1)
        if isprime(2**(n-1)-1):
            print("Pero si resulta que2**",n-1,"=",(2**(n-1)-1),"es un primo de Mersenne")
        cuantos-=1
    return lista[len(lista)-1]