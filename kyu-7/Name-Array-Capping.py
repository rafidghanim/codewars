def cap_me(arr):
    return [i[0].upper() + i[1:].lower() if i.isalnum() else i for i in arr]
