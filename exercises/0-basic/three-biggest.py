def los_putos_3_mayores_para_mi_brouston_favorito(lista):
    
    max1 = max(lista)
    
    seguir_eliminando = 1
    lista2 = []
    while seguir_eliminando == 1:
        for element in lista:   
            if element != max1:
                lista2.append(element)
                seguir_eliminando = 0
    max2 = max(lista2)
    
    seguir_eliminando = 1
    lista3 = []
    while seguir_eliminando == 1:
        for element in lista2:   
            if element != max2:
                lista3.append(element)
                seguir_eliminando = 0
    max3 = max(lista3)
    
    return max1, max2, max3