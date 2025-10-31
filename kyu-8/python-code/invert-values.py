def invert(lst):
    return [i*-1 if i>0 else abs(i) for i in lst]
