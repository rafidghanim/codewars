def to24hourtime(hour, minute, period):
    # hour will always range from 1 to 12 (inclusive)
    # minute will always range from 0 to 59 (inclusive)
    # period will always be either "am" or "pm"
    hours = ('0' + str(hour))[-2::]
    minutes = ('0' + str(minute))[-2::]
    hourss = ('0'+str(hour+12))[-2::]
    period = period
    if period=='pm' and int(hourss) < 24:
        return hourss+minutes
    elif period=='am' and int(hours) < 12:
        return hours+minutes
    elif int(hourss)==24 and period=='am':
        return '00'+minutes
    elif int(hours)==12 and period=='pm':
        return '12'+minutes
#     elif hourss=='24' and period=='pm':
#         return '12'+minutess
#     elif hours=='12' and period=='am':
#         return '00'+minutess
#     else:
#         return hourss+minutess
