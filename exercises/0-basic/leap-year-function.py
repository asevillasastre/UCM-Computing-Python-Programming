def de4(y):
    return y%4==0
def de100(y):
    return y%100==0
def de400(y):
    return y%400==0

def bis(y):
    return (de4(y)==True and not de100(y)==True) or de400(y)==True