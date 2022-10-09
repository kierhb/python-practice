import re


def add_time(start, duration, day = False):
    # For Start Time:
    start_time, meridiem = start.split()
    start_hour, start_minute = start_time.split(":")

    # For Duration Time:
    duration_hour, duration_minute = duration.split(":")
    
    '''
    # Covert Start Hour:
    if meridiem == "PM":
        cnvrt_start = ((int(start_hour) + 12) * 60) + int(start_minute)
    else:
        cnvrt_start = (int(start_hour) * 60) + int(start_minute)
    print(cnvrt_start)

    # Convert Duration Hour:
    cnvrt_duration = (int(duration_hour) * 60) + int(duration_minute)
    print(cnvrt_duration)

    # Combine:
    lapse = cnvrt_start + cnvrt_duration
    '''
    



add_time("11:43 PM", "24:20")