def solution(*x):
    return any(x.count(i) > 1 for i in x)
#     # Iterate through each element i in the input x
#     # Check if the count of i in x is greater than 1
#     # If it is, return True, indicating at least one element occurs more than once
#     for i in x:
#         if x.count(i) > 1:
#             return True
#     # If no element occurs more than once, return False
#     return False
