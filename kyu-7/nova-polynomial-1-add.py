# return the sum of the two polynomials p1 and p2.  
def poly_add(p1, p2):
    # TODO: complete
    z = []
    for i in range(max(len(p1),len(p2))):
        k = p1[i] if i < len(p1) else 0
        f = p2[i] if i < len(p2) else 0
        z.append(k+f)
    return z
