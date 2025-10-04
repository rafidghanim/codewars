def even_odd(arr):
    if not arr:
        return 0
    res = arr[0]
    i = 1
    while i < len(arr):
        res *= arr[i]
        i += 1
        if i < len(arr):
            res += arr[i]
            i += 1
    return res
