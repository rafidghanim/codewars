def sum_array(arr):
    return 0 if arr is None or len(arr) <=1 else sum(arr) - max(arr, default=0) - min(arr, default=0)
