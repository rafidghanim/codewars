def better_than_average(class_points, your_points):
    return True if your_points > (sum(class_points))/len(class_points) else False
    # Your code here
