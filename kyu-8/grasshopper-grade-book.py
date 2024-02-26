def get_grade(s1, s2, s3):
    # Code here
    val = (s1+s2+s3)//3
    if val>=90:
        return "A"
    elif val>=80:
        return "B"
    elif val>=70:
        return "C"
    elif val>=60:
        return "D"
    elif val<60:
        return "F"
