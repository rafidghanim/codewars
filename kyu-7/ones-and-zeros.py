def binary_array_to_number(arr):
    return sum([arr[i] * 2**(len(arr)-1-i) for i in range(len(arr))])
