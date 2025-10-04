def encode(s:str) -> str:
    result = []
    n = len(s)
    for i in range(n // 2):
        result.append(s[i])
        result.append(s[n - 1 - i])
    if n % 2 == 1:
        result.append(s[n // 2])
    return ''.join(result)
def decode(s:str) -> str:
    n = len(s)
    result = [''] * n
    left = 0
    right = n - 1
    idx = 0

    for i in range(n // 2):
        result[left] = s[idx]
        result[right] = s[idx + 1]
        idx += 2
        left += 1
        right -= 1

    if n % 2 == 1:
        result[left] = s[idx]
    
    return ''.join(result)
