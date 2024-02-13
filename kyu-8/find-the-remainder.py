def remainder(n, m):
    try:
        return max(n, m) % min(n, m)
    except ZeroDivisionError:
        return None
    #your code here
