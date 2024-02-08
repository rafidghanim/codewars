def encrypt_this(text):
    if len(text)!=0:
        solved = []
        words = text.split()
        for i in words:
            if len(i)>2:
                enc =  str(ord(i[0])) + i[-1] + i[2:-1] + i[1]
            elif len(i) == 2:
                enc = str(ord(i[0])) + i[1]
            else:
                enc = str(ord(i))
            solved.append(enc)
        clear = " ".join(solved)
        return clear
    else:
        return text
