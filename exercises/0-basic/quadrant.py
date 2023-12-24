def cuadrante(x,y):
    if x<0 or x==0:
        if y<0 or y ==0:
            return "III"
        else:
            return "II"
    else:
        if y<0 or y ==0:
            return "IV"
        else:
            return "I"
