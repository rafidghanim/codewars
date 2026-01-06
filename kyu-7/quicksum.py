import string
def quicksum(packet):
    asup = string.ascii_uppercase
    data = {}
    for i in range(len(asup)):
        data.update({asup[i]:i+1})
    chcksum = 0
    for i in range(len(packet)):
        try:
            if packet[i]==' ':
                chcksum+=0
            else:
                chcksum += (i+1) * data.get(packet[i])
        except:
            return 0
    return chcksum