def suma_polinomios(pol1, pol2):
    
    result=[]
    
    for mon1 in pol1:
        for mon2 in pol2:
            if mon1[0] == mon2[0]:
                result.append((mon1[0],mon1[1]+mon2[1]))
    
    print(result)
    
    for mon1 in pol1:
        anadir=True
        for element in result:
            if mon1[0] == element[0]:
                anadir=False
        if anadir:
            result.append(mon1)
    
    for mon2 in pol2:
        anadir=True
        for element in result:
            if mon2[0] == element[0]:
                anadir=False
        if anadir:
            result.append(mon2)
    
    return result

def multi_polinomios(pol1,pol2):
    
    result=[]
    
    for mon1 in pol1:
        for mon2 in pol2:
            result.append((mon1[0]+mon2[0],mon1[1]*mon2[1]))
    
    cosa=[]
    
    for element in result:
        anadir=True
        for e in cosa:
            if element[0]==e:
                anadir=False
        if anadir:
            cosa.append(element[0])
        
    final=[]
    
    for grado in cosa:
        cociente=0
        for element in result:
            if element[0]==grado:
                cociente+=element[1]
        final.append((grado,cociente))
    
    return final

def evaluar(pol,x0):
    
    valor=0
    
    for mon in pol:
        valor+=mon[1]*x0**mon[0]
        
    return valor





























