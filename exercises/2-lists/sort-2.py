
def good_ordenar(lst):
    ordenadas = 0
    while ordenadas < len(lst) - 1:
        comparar = ordenadas
        while comparar < len(lst):
            char = 0
            while char < min(len(lst[ordenadas + 1][0]), len(lst[comparar][0])):
                if ord(lst[comparar][0][char]) > ord(lst[ordenadas + 1][0][char]):
                    lst[comparar], lst[ordenadas + 1] = lst[ordenadas + 1], lst[comparar]
                char += 1
            """
            if lst[comparar][1] > lst[ordenadas + 1][1]:
                lst[comparar], lst[ordenadas + 1] = lst[ordenadas + 1], lst[comparar]
            """
            comparar += 1
        ordenadas += 1
    return lst