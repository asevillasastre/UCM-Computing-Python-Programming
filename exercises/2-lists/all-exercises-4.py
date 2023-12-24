"""
HOJA 4
"""

"""
ejercicio 1
"""

"""
las funciones que se llaman "facil" crean una lista nueva que se transforma hasta dar el
resultado

las funciones que se llaman "dificil" modifican el parámetro lista dado
"""

def eliminar_iesimo_dificil(lista,i):
    while i<len(lista)-1:
        lista[i]=lista[i+1]
        i+=1
    lista.pop(len(lista)-1)
    return lista

def eliminar_iesimo_facil(lista,i):
    result,j=[],0
    while j<len(lista):
        if i!=j:
            result.append(lista[j])
        j+=1
    return result

def saturar_facil(lista,x):
    new=[]
    for element in lista:
        new.append(max(element,x))
    return new 

def saturar_dificil(lista,x):
    i=0
    while i<len(lista)-1:
        lista[i]=max(lista[i],x)
        i+=1
    return lista

def eliminar_apariciones_facil(lista,cosa):
    new=[]    
    for element in lista:
        if element!=cosa:
            new.append(element)
    return new   

def eliminar_apariciones_dificil(lista,cosa):
    i,eliminar=0,0
    while i<len(lista)-1:
        if cosa==lista[i]:
            j=i
            eliminar+=1
            while j<len(lista)-1:
                lista[j]=lista[j+1]
                j+=1
        else:
            i+=1
    while eliminar>0:
        lista.pop()
        eliminar-=1
    return lista

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

def primos_facil(lista):
    new=[]
    for element in lista:
        if isprime(element):
            new.append(element)
    return new

def primos_dificil(lista):
    i=0
    apartirde=0
    borrar=0
    while i<len(lista):
        if not isprime(lista[i]):
            apartirde=i
            while apartirde<len(lista)-1:
                lista[apartirde]=lista[apartirde+1]
                apartirde+=1
            borrar+=1
        else:
            i+=1
    while borrar>0:
        borrar-=1
        lista.pop()
    return lista          

def insertar_facil(lista,posicion,elemento):
    new=[]
    i=0
    while i<len(lista):
        if i==posicion:
            new.append(elemento)
            new.append(lista[i])
        else:
            new.append(lista[i])
        i+=1
    return new

def insertar_dificil(lista,posicion,elemento):
    auxiliar=[]
    eliminar=len(lista)-posicion
    while posicion<len(lista):
        auxiliar.append(lista[posicion])
        posicion+=1
    while eliminar>0:
        eliminar-=1
        lista.pop()
    lista.append(elemento)
    for cosica in auxiliar:
        lista.append(cosica)
    return lista
            
def rotacion_dificil(lista):

    ultimo=lista[0]
    
    for i in range(0,len(lista)-1):
        lista[i]=lista[i+1]
    
    lista.pop()
    lista.append(ultimo)
    return lista

def rotacion_facil(lista):
    new=[]
    for i in range(1,len(lista)):
        new.append(lista[i])
    new.append(lista[0])
    return new

def paridad_dificil(lista):
    """
    solo funciona con listas de longitud par
    """
    i=0
    while i<len(lista):
        lista[i],lista[i+1]=lista[i+1],lista[i]
        i+=2
    return lista

def paridad_facil(lista):
    """
    solo funciona con listas de longitud par
    """
    new=[]
    for element in range(0,len(lista)-1):
        if (element+1)%2!=0:
            new.append(lista[element+1])
            new.append(lista[element])
    return new

""""
ejercicio 2
"""

def cifras(n):
    """
    auxiliar
    """
    cifras=[]
    while n>0:
        cifras.append(n%10)
        n=n//10
    return rotasió(cifras)

def rotasió(lista):
    """
    auxiliar
    """
    i=0
    while i<len(lista)//2:
        lista[i],lista[len(lista)-1-i]=lista[len(lista)-1-i],lista[i]
        i+=1
    return lista

def enesimacifra(num,n):
    return cifras(num)[n-1]

def mas_significativas(num,n):
    new=[]
    n-=1
    while n>=0:
        new.append(cifras(num)[n])
        n-=1
    return new

def menos_significativas(num,n):
    new=[]
    while n<len(cifras(num)):
        new.append(cifras(num)[n])
        n+=1
    return new

def cifrasbase(n,base):
    """
    auxiliar.
    para que el resto de funciones usen cualquier otra base sustituimos cifras(n) por esta
    """
    cifras=[]
    while n>0:
        cifras.append(n%base)
        n=n//base
    return rotasió(cifras)

"""
ejercicio 3
"""

def montecarlo(dar2):
    """
    suponemos un círculo dentro de un cuadrado 1x1.
    damos valores de x,y aleatorios dentro del mismo ( que es lo que hace random.random() )
    y comprobamos su módulo ( math.sqrt(x**2+y**2) ) para ver si está contenido en el círculo
    """
    import random
    import math
    dar3=dar2
    dentro=0
    while dar2>0:
        dar2-=1
        x=random.random()
        y=random.random()
        if math.sqrt(x**2+y**2)<=1:
            dentro+=1
    return 4*dentro/dar3

"""
ejercicio 4
"""

def descomponer(num):
    """
    funciona para números a partir del 4, inclusive
    """
    summ,sumM=2,2
    while True:
        while summ<sumM:
            summ+=1
            while not isprime(summ):
                summ+=1
            if summ+sumM==num:
                return summ,sumM
        sumM+=1
        while not isprime(sumM):
            sumM+=1
        if summ+sumM==num:
            return summ,sumM
        summ=2
        if summ+sumM==num:
            return summ,sumM

def goldbach(hasta):
    num=4
    result=True
    while num<hasta:
        result= result or descomponer(hasta)[0]+descomponer(hasta)[1]==hasta
        print(result)
        num+=2
    return result

"""
ejercicio 5
"""

def primomayorque(lista):
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
    return n-1

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
        cuantos-=1
        print(lista[len(lista)-1])
    return lista,lista[len(lista)-1]

"""
me falta la del fichero porque no hemos usado ficheros aun :(
"""

"""
ejercicio 6
"""

def newton(arriba,abajo):
    """
    auxiliar
    """
    from math import factorial
    return factorial(arriba)//(factorial(abajo)*factorial(arriba-abajo))
    
def pascal(lado):
    llenar1=0
    result=[]
    while llenar1<lado:
        result.append([])
        llenar1+=1
    llenar1=0
    while llenar1<lado:
        llenar2=0
        while llenar2<lado:
            result[llenar2].append(1)
            llenar2+=1
        llenar1+=1
    """
    hasta aquí hemos generado una matriz vacía
    """
    maximo=0
    while maximo<lado:        
        eldeabajo=0
        eldearriba=maximo
        columna=0
        fila=maximo
        
        while eldeabajo<maximo:
            result[fila][columna]=newton(eldearriba,eldeabajo)
            eldeabajo+=1
            fila-=1
            columna+=1
        maximo+=1
    """
    y hasta aquí se llena con los números pertinentes
    """
    return result

def dibujo(lado):
    """
    hasta lado=18 el dibujo queda cuadrado
    """
    
    cadena=""
    for fila in pascal(lado):
        print("")
        cadena=""
        for element in fila:
            if element%2==0:
                cadena+="   卐"
            else:
                cadena+="    O"
        print(cadena)
    
"""
ejercicio 7
"""
    
def array(lista,k):
    eureka=False
    i=0
    while i<len(lista)-1 and not eureka:
        j=0
        counter=0
        while j<len(lista):
            if lista[j]==lista[i]:
                counter+=1
            j+=1
        if counter==k:
            eureka=True
        i+=1
    if eureka==True:
        return lista[i-1]
    return "No se ha encontrado ninguno D:"    
    
"""
ejercicio 8
"""

def espiral(matrix):
    """
    básicamente, vamos recorriendo todos los elementos de la primera fila de izda a dcha,
    luego los de la columna de arriba abajo, fila de dcha a izda, columna de abajo arriba.
    tenemos que usar los valores //arriba,abajo,izda,dcha=0,0,0,0// para que ese recorrido
    no llegue al final de la línea y así recorra la matriz en espiral
    """
    result=[]
    fila,columna=0,0
    arriba,abajo,izda,dcha=0,0,0,0
    seguir=True
    while len(result)<len(matrix)**2 and seguir:
        while columna<len(matrix[0])-dcha:
            result.append(matrix[fila][columna])
            columna+=1
        arriba+=1
        columna-=1
        fila+=1
        while fila<len(matrix)-abajo:
            result.append(matrix[fila][columna])
            fila+=1
        abajo+=1
        columna-=1
        fila-=1
        while columna>=izda:
            result.append(matrix[fila][columna])
            columna-=1
        izda+=1
        columna+=1
        fila-=1
        while fila>=arriba:
            result.append(matrix[fila][columna])
            fila-=1
        dcha+=1
        fila+=1
    return result

"""
ejercicio 9
"""

def rotacion(lista):
    i=0
    while i<len(lista)//2:
        lista[i],lista[len(lista)-1-i]=lista[len(lista)-1-i],lista[i]
        i+=1
    return lista

def ispalindromo(lista):
    return lista==rotacion(lista)

def reversodeunnumero(num):
    w=0
    result=0
    while w<len(cifras(num)):
        result+=10**(w-1)*cifras(num)[w]
        w+=1
    return int(result*10)

def ispalinromonumero(num):
    return cifras(num)==rotacion(cifras(num))

"""
ejercicio 10
"""

def conjetura(num):
    while not ispalinromonumero(num):
        num+=reversodeunnumero(num)
    return num

def conjetura_con_iteraciones(num,iteraciones):
    while not ispalinromonumero(num) and iteraciones>0:
        num+=reversodeunnumero(num)
        iteraciones-=1
    if ispalinromonumero(num):
        return "Se ha encontrado un palíndromo:",num
    return "No se ha encontrado ningún palíndromo :("

"""
ejercicio 11
"""

def suma_acumulada(lista):
    operamos_apartir_de=1
    while operamos_apartir_de<len(lista):
        j=operamos_apartir_de
        
        """
        si ponemos auxiliar=lista, auxiliar va cambiando a la vez que lista. 
        por ello debemos generar auxiliar de la siguente manera:
        """
        auxiliar=[]
        for element in lista:
            auxiliar.append(element)
        
        while j<len(lista):
            lista[j]+=auxiliar[j-1]
            j+=1
        operamos_apartir_de+=1
    return lista

"""
ejercicio 12
"""

def entropia(lista):
    evaluar_a_partir_de=0
    suma=0
    while evaluar_a_partir_de<len(lista):
        j=evaluar_a_partir_de
        while j<len(lista):
            if lista[j]<lista[evaluar_a_partir_de]:
                suma+=1
            j+=1
        evaluar_a_partir_de+=1
    return suma

"""
ejercicio 13
"""

def filtro_mod_24(n):
    return n**2%24==1

def filtro_divisores(n):
    """
    >>>filtro_divisores(524287)
    True
    
    es útil para primos grandes porque acaba pronto, en raíz de n
    """
    if n==1:
        return False
    import math
    eureka=False
    t=2
    while not eureka and t<math.sqrt(n):
        t=t+1
        if n%t==0:
            eureka=True
    return not eureka


def filtro_primos(n):
    """
    >>>filtro_primos(2147483647)
    True
    
    es tan eficiente que puede comprobar esta cosa
    """
    if n==2 or n==3:
        return True
    if n==1 or n%2==0:
        return False
    
    import math
    t=3
    eureka=False
    while not eureka and t<math.sqrt(n):
        if n%t==0:
            eureka=True
        t=t+2
    return not eureka

    
    










