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
