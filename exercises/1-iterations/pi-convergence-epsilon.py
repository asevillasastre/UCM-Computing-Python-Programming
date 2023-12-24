def phi(precision): 
    import math
    n=3
    m=4
    j=1
    k=2
    pi=1
    j *= n**2
    k *= m**2
    while pi-math.pi>precision:
        n +=2
        m +=2
        j *= n**2
        k *= m**2
        pi=4/(j/(k/m))
    return pi
