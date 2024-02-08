def factorial(n):
    if not isinstance(n, int) or n < 0 or n >12:
        raise ValueError("Factorial is only defined for non-negative integers")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
