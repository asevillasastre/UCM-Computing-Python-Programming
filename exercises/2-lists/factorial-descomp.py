def desc(n):

    lista=[]
    while n!=1:
        divisor=2        
        while n%divisor!=0:
            divisor = divisor + 1    
        lista.append(divisor)
        n=n/divisor    
    return (lista)

def es_par(x):
    return x % 2 == 0

def conjunto_potencia(s):
    n = len(s)

    # crear lista con 2^n conjuntos vacios
    subconjuntos = []
    for i in range(2 ** n):
        subconjuntos.append(set())

    # convierto a lista para poder ir recorriendo
    # los elementos por su indice i
    elementos = list(s)

    for i in range(n):
        x = elementos[i]
        for j in range(2 ** n):
            if es_par(j / (2 ** i)):
                subconjuntos[j].add(x)

    return subconjuntos