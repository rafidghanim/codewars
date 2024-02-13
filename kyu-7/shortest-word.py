def find_short(s):
    # your code here
    return len(min(s.split(), key=len))
        
#     return len(l) # l: shortest word length
