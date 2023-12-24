def rectangle_center(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Function which returns the center of a rectangle
    
    Parameters
    ----------
    xn : int
        x coordinate of vertex n
    yn : int
        y coordinate of vertex n
    
    Return
    ------
    int
        Coordenates x, y of the center of the rectacgle
        
    Example
    -------
    >>> rectangle_center(1,1,1,6,4,1,4,6)
    (2.5, 3.5)
    
    """
    return (x1 + x2 + x3 + x4) /4, (y1 + y2 + y3 + y4) /4