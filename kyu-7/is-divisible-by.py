def is_divisible(*x):
    return all(x[0] %num == 0 for num in x[1:])
