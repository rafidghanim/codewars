def no_of_digits(num):
    i = 0
    while num > 0:
        num //= 10
        i += 1
    return i

def narcissistic(num):
    i = no_of_digits(num)
    original_num = num
    s = 0
    
    while num > 0:
        digit = num % 10
        num //= 10
        s += pow(digit, i)
    
    return s == original_num
