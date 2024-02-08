def distances_from_average(test_list):
    arr = []
    sum = 0
    for i,a in enumerate(test_list):
        sum+=a
    avg = sum/len(test_list)
    for j in range(len(test_list)):
        dist = avg - test_list[j] 
        arr.append(round(dist,2))
    return arr
        
