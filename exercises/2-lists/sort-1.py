def sort(tupla):
    ordenadas = 0
    long=len(tupla[0])
    while ordenadas < long:
        comparando = ordenadas + 1
        while comparando < long:
            char = 0
            seguir=True
            while char < min(len(tupla[0][comparando]), len(tupla[0][ordenadas])) and seguir:
                if tupla[0][comparando][char] < tupla[0][ordenadas][char]:
                    tupla[0][comparando], tupla[0][ordenadas] = tupla[0][ordenadas], tupla[0][comparando]
                    tupla[1][comparando], tupla[1][ordenadas] = tupla[1][ordenadas], tupla[1][comparando]
                    seguir=False
                elif tupla[0][comparando][char] > tupla[0][ordenadas][char]:
                    seguir=False
                else:
                    char += 1
            comparando += 1
        ordenadas += 1
    return tupla
