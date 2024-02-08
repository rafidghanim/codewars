def get_num(n):
    z = 0
    k = [0, 6, 9]
    j = [8]
    for i in str(n): 
        for l in k:
            if int(i) == l:
                z += 1
        if int(i) == 8:
            z += 2 
    return z
