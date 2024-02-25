def alphabet_position(text):
    z = []
    for i in text:
        if i.isupper():
            t = ord(i)-64
            z.append(t)
        elif i.islower():
            t = ord(i)-96
            z.append(t)
        else:
            pass
    return str(z).replace("[","").replace("]","").replace(",","")
