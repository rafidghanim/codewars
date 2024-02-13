import math
def sensor_analysis(sensor_data):
    s = 0
    ls = []
    for i in sensor_data:
        p = float(i[1])
        s+=p
        ls.append(p)
    mean = round(s/len(sensor_data),4)
    for i in range(len(sensor_data)):
        z = round(math.sqrt((sum((x-mean)**2 for x in ls)/(len(sensor_data)-1))),4)
    return (mean,z)
