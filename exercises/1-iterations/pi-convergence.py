"""
9. CONVERGENCIAS A PI
"""

def phi(ite):
    """
    aplicando la fórmula dada, consideramos una fracción que empieza arriba 3*3*5*5...
    y abajo 4*4*6*6... 
    multiplicándose todos los elementos
    
    finalmente se añade el 2 y se elimina el último factor del producto en el denominador
    
    el resultado es 4/esa fracción
    
    se añaden elementos hasta que se han realizado "ite" repeticiones
    """
    n=3
    m=4
    j=1
    k=2
    p=1
    j *= n**2
    k *= m**2
    while ite>p:
        n +=2
        m +=2
        j *= n**2
        k *= m**2
        p +=1      
    pi=4/(j/(k/m))
    return pi

def phi2(precision): 
    """
    mismo proceso que en "phi", pero se detiene cuando se aproxima al valor real de pi en una 
    "precision" dada
    """
    import math
    n=3
    m=4
    j=1
    k=2
    pi=1
    j *= n**2
    k *= m**2
    while pi-math.pi>precision:
        n +=2
        m +=2
        j *= n**2
        k *= m**2
        pi=4/(j/(k/m))
    return pi


def pito(precision):
    """
    (-1)**par >0, (-1)**impar <0
    se suman los elementos de la forma que indica la fórmula
    """
    n=1
    suma=0
    while precision>n:
        if n%2==1:
            suma+=1/(2*n-1)
        if n%2==0:
            suma-=1/(2*n-1)
        n+=1
    return 4*suma

def pipi(precision):
    """
    el siguiente término va en función del siguiente, siendo xn+1 = la raíz de (1/2 + 1/2(xn))
    """
    import math
    pi=math.sqrt(1/2)
    while precision>0:        
        pi=pi*(math.sqrt(1/2 + (1/2)*pi))
        precision-=1
    return 2/pi

def piiiii(ite):    
    """
    #1 se define también cada término en función del siguiente, pero han de empezar en x1,y1,pi1
    
    #2 y definirse siempre en orden xn,yn,pin porque van en función del anterior en ese orden
    """
    import math    
    
    x0= math.sqrt(2)
    sigx=x0    
    
    y1=2**(1/4)
    sigy=y1
    
    pi0=2+math.sqrt(2)
    sigpi=pi0            
    
    #1
    sigx=(1/2)*(math.sqrt(sigx)+math.sqrt(sigx)**-1)  
    sigpi=sigpi*(sigx+1)/(sigy+1)
    
    while ite>0:
        
        #2
        sigx=(1/2)*(math.sqrt(sigx)+math.sqrt(sigx)**-1)
        sigy=(sigy*math.sqrt(sigx)+math.sqrt(sigx)**-1)/(sigy+1)
        sigpi=sigpi*(sigx+1)/(sigy+1)
        
        ite-=1
    
    return sigpi