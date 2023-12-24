def n(rey):
    cab=rey
    noche=rey
    t=1
    
    while ((cab!=rey) or (rey==noche)) and(cab>0) and(t==1):
        rey = rey+1
        cab=cab-1.5
        
    while cab==0 or cab<0:
        rey= rey+1
        cab=abs(cab)+1.5
        t=2
    
    while (cab!=rey) and (cab>0) and (t==2):
        rey = rey+1
        cab=cab+1.5
      
    return rey