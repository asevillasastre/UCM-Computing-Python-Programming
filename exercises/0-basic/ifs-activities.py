def actividad(T):
    if T>30:
        return "natacion"
    if T>20 and T<30 or T==30:
        return "tenis"
    if T>10 and T<20 or T==20:
        return "golf"
    if T>5 and T<10 or T==10:
        return "esqui"
    if T<5 or T==5:
        return "parchis"
     