def sum_two_smallest_numbers(numbers):
    z = min(numbers)
    numbers.remove(min(numbers))
    return z+min(numbers)
    #your code here
