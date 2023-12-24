"""
5. SIMPLIFICACIÓN DE FRACCIONES
"""

def s(a, b):
    """
    a numerador, b denominador
    este programa realiza el algoritmo de Euclides con un while
    
    usamos z, una variable auxiliar para no perder ninguno de los valores
    """
    y=max(a, b)
    x=min(a, b)
    
    while y%x!=0:
        z=x
        x=y%x
        y=z
    
    return a//x, b//x