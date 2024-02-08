def pythagorean_triple(integers):
    return [integers.sort(),integers[0]**2+integers[1]**2==integers[2]**2][1]
