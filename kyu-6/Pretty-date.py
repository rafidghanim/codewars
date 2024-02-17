def to_pretty(seconds):
    #1-59 convert into seconds have 1 until 2 len
    #60-3599 convert into  minutes
    #3600-86399  convert into hours
    #86400-604799 convert into days
    #>604800 convert into weeks
    if seconds==0:
        return "just now"
    elif seconds==1:
        return "a second ago"
    elif seconds<60:
        return f"{seconds} seconds ago"
    
    min = seconds//60
    if min==1:
        return "a minute ago"
    elif min<60:
        return f"{min} minutes ago"
    
    
    hor = seconds//3600
    if hor==1:
        return "an hour ago"
    elif hor<24:
        return f"{hor} hours ago"
    
    day = seconds//86400
    if day==1:
        return "a day ago"
    elif day<7:
        return f"{day} days ago"
    
    week = seconds//604800
    if week==1:
        return "a week ago"
    elif week>1:
        return f"{week} weeks ago"
