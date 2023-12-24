def diofantica_xmásy(n):
    x=1
    y=n-1
    sol = []
    while y>=x:
        sol.append((x,y))
        if x!=y:
            sol.append((y,x))
        x += 1
        y -= 1
    return sol

