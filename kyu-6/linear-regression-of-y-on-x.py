def regression_line(x, y):
    """ Return the a (intercept)
        and b (slope) of Regression Line 
        (Y on X).
    """
    n = len(x)
    sigma_x = sum(x)
    sigma_y = sum(y)
    sigma_xy = sum([i * j for i, j in zip(x, y)])
    sigma_xx = sum([i ** 2 for i in x])

    b = (n * sigma_xy - sigma_x * sigma_y) / (n * sigma_xx - sigma_x ** 2)
    a = (sigma_y - b * sigma_x) / n
    
    return round(a, 4), round(b, 4)
