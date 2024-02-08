def collinearity(x1, y1, x2, y2):
    return True if (x1 == 0 and x2 == 0) or (y1 == 0 and y2 == 0) or (x2 * y1 == x1 * y2) else False
