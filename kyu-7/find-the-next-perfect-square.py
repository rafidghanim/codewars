import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    return -1 if round(math.sqrt(sq))**2!=sq else (round(math.sqrt(sq))+1)**2
