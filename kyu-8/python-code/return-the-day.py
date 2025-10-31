def whatday(num):
    z = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if num>7 or num<1:
        return "Wrong, please enter a number between 1 and 7"
    for i in range(1,8):
        if num==i:
            return z[i-1]
