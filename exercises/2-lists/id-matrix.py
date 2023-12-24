def i(n):
    result=[]
    fila=[]
    i=0
    j=0
    while len(result)<n:
        while len(fila)<n:
            if i==j:                
                fila.append(1)
            else:
                fila.append(0)
            i+=1
        i=0
        result.append(fila)
        fila=[]
        j+=1
    return result
