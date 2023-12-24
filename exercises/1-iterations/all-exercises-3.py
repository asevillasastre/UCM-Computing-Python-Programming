"""----------------HOJA 3 DE EJERCICIOS-----------------------"""

"""
1. CIFRAS EN BASE
"""

def cifras(n, base):
    """
    como se hace en el algoritmo clásico de cambio de base:
    se divide iterativamente el número n entre la base y se acumulan los restos en "cifras"
    
    el número de cifras es simplemente la longitud de esa lista
    """
    cifras=[]
    while n>0:
        cifras.append(n%base)
        n=n//base
    return len(cifras)

"""
2. REVERSO DE UN NÚMERO
"""

def reverso(n):
    """
    recurrimos a la función "cifras", que nos da la lista de las cifras.
    simplemente tenemos que tomarlas al revés y meterlos con un while en result
    """
    cifras=[]
    while n>0:
        cifras.append(n%10)
        n=n//10
    result=[]
    j=1
    while j<len(cifras):
        result.append(cifras[j-1])
        j+=1
    result.append(cifras[len(cifras)-1])
    return result

"""
3. SUMA MARCIANA

no tengo la función hecha pero tengo una foto de un ejemplo de código (un tanto farragoso)
que lo resuelve
"""

""""
4. LISTAS
"""

def lista_aleatoria(longitud, rango):
    import random
    lista = []    
    while longitud>0:
        lista.append(random.randint(1,rango))
        longitud=longitud-1
    return lista

def media(lista):
    """
    sumar todos los elementos y dividirlos entre la longitud de la lista
    (puede hacerse con un for)
    """
    j=len(lista)    
    n=0    
    suma=0    
    while j>0:
        j=j-1
        suma += lista[n]
        n+=1
    return suma/len(lista)
    
def desviacion_tipica(lista): 
    """
    aplicar de forma similar la fórmula de desviación típica
    (puede hacerse con un for)
    """
    j=len(lista)
    n=0    
    result=0    
    while j>0:
        result= result+ ((lista[n]-media(lista)))**2
        n=n+1
        j=j-1
    return (result/(len(lista)-1))**(1/2)
    
def cantidad_pares(lista):
    """
    "resultao" es un contador al que se suma 1 cada vez que se encuentra un elemento par recorriendo
    toda la lista
    (puede hacerse con un for)
    """
    j= len(lista)    
    resultao=0
    n=0    
    while j>0:
        if lista[n]%2==0:
            resultao=resultao+1
        n+=1
        j=j-1
    return resultao
    
def cantidad_cuadra2(lista):
    """
    procedimiento análogo
    (puede hacerse con un for)
    """
    j= len(lista)    
    resultao=0
    n=0    
    while j>0:
        if int(lista[n]**(1/2))==lista[n]**(1/2):
            resultao=resultao+1
        n+=1
        j=j-1
    return resultao
    
def cantidad_log(lista,numero):
    """
    procedimiento análogo
    (puede hacerse con un for)
    """
    import math    
    j= len(lista)    
    resultao=0
    n=0    
    while j>0:
        if math.log2(lista[n])>math.log2(numero):
            resultao=resultao+1
        n+=1
        j=j-1
    return resultao
    
def ordenado(lista):
    """
    se va comprobando si cada elemento es mayor que el anterior.
    si se encuentra uno que no lo cumple return False
    """
    j=len(lista)
    n=0    
    while j>1:
        j=j-1
        if (lista[n+1]<=lista[n]):
            return False
        n=n+1
    return True

def picos(lista):
    """
    picos es un contador al que se le añade una unidad cada vez que se el elemento anterior y siguiente
    son menores que el evaluado
    ha de empezarse en el segundo elemento de la lista, que es el que tiene uno anterior,
    así como acabarse en el penúltimo por tener uno posterior.
    """
    j=len(lista)
    picos=0    
    n=0    
    while j>1:
        j=j-1
        if lista[n]>lista[n+1] and lista[n-1]<lista[n]:
            picos=picos+1
        n=n+1
    return picos

def potencia_de_2(lista):
    """
    procedimiento análogo
    (puede hacerse con un for)
    """
    import math
    result=0
    j=0
    while j<len(lista):
        if math.log2(lista[j])==int(math.log2(lista[j])):
            result=result+1
        if lista[j]==1:
            result = result-1
        j=j+1
    return result

def primo(n):
    """
    función auxiliar para buscar si n es primo
    """
    if n==1:
        return False
    t=2
    while n%t!=0 and n!=t:
        t=t+1
    return (n==t)

def primos(lista):
    """
    se recurre a la función "primo"
    procedimiento análogo
    (puede hacerse con un for)
    """
    result=0
    j=0
    while j<len(lista):
        if primo(lista[j])==True:
            result +=1
        j=j+1
    return result

def palindroma(lista):
    """
    con un while se toman los elementos del principio y del final para luego ir recorriendo la lista
    hacia el centro
    si en algún momento no coinciden la lista devolverá False
    """
    n=0
    while n<len(lista):
        if (lista[n]-lista[len(lista)-n-1])!=0:
            return False
        n+=1
    return True

"""
5. SIMPLIFICACIÓN DE FRACCIONES
"""

def s(a, b):
    """
    a numerador, b denominador
    
    este programa realiza el algoritmo de Euclides con un while
    
    usamos z, una variable auxiliar para no perder ninguno de los valores
    """
    y=max(a, b)
    x=min(a, b)
    
    while y%x!=0:
        z=x
        x=y%x
        y=z
    
    return a//x, b//x

"""
6. DESCOMPOSICIÓN FACTORIAL
"""

def desc(n):
    """
    este módulo prueba iterativamente desde 2 distintos valores de divisor para ver si dividen a n
    
    si se encuentra un divisor se añade a la lista y se divide n entre él, tal y como hacemos cuando
    descomponemos manualmente
    
    la descomposición acaba evidentemente cuando n ya no se puede descomponer más, esto es n=1
    """
    lista=[]
    while n!=1:
        divisor=2        
        while n%divisor!=0:
            divisor = divisor + 1    
        lista.append(divisor)
        n=n/divisor    
    return (lista)

"""
7. CUBOS DE NIMONACO
"""

def nimonaco(n):
    """
    (está hecha un poco cutre, espero que se entienda porque no sé explicarlo demasiado bien :/ )
    """
    m=0
    lista=[]
    j=0
    while m<n+1:
        listo=[]
        while len(listo)<m:
            listo.append(1+2*j)
            j+=1
            p=0
        cubo=0
        while p<len(listo):
            cubo+=listo[p]
            p+=1
        if cubo!=0:
            lista.append(cubo)
        m+=1
    return lista

"""
8. DIOFÁNTICAS
"""

def diofantica_xmásy(n):
    """
    un programa iterativo que prueba para valores crecientes de x e y hasta que satisfagan la 
    ecuación diofántica de la siguiente forma:
        
    los valores de y van creciendo primero de 1 en 1 y se prueban todos los x menores que él
    """
    x=1
    y=n-1
    sol = []
    while y>=x:
        sol.append((x,y))
        if x!=y:
            sol.append((y,x))
        x += 1
        y -= 1
    return sol

"""
no lo tengo hecho pero el proceso es análogo para el resto de apartados,
"que quedan como ejercicio para el lector" xD
"""

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

"""
los ejercicios 10 y 11 aun no he sido capaz de resolverlos por mi cuenta, aunque son  mucho más difíciles
que lo que puede pedir en el examen, así que tampoco me preocuparía :D
"""

"""
12. CRIBA DE ERATÓSTENES
"""

def criba(x):
    """
    n es cada número de 0 a x, y gracias al for los evalúa todos para descubrir cuales son primos
    
    divisor es cada número de 2 a n, y gracias al while los evalúa todos para descubrir cuales
    dividen a n. n no tiene divisores <=> n es primo
    
    (pueden usarse indistintamente for y while para la evaluación de los n, así como dar los
    resultados en forma de lista, definiendo una lista vacía al principio y llenándola con los
    n sin divisores)
    """
    for n in range(x):
        divisor =2
        while n%divisor!=0 and n>divisor:
            divisor=divisor+1
        if n==divisor:
            print (n)
