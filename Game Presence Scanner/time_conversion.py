from time import time
def since_ms(ms):
    
    seconds_in_minute = 60
    seconds_in_hour = 3600
    seconds_in_day = 86400
    seconds_in_month = 30 * seconds_in_day

    total_seconds = (time() - ms)
    print(time() - ms)

    months = total_seconds // seconds_in_month
    print(total_seconds//(86400*30))
    remaining_seconds = total_seconds % seconds_in_month

    days = remaining_seconds // seconds_in_day
    remaining_seconds %= seconds_in_day

    hours = remaining_seconds // seconds_in_hour
    remaining_seconds %= seconds_in_hour

    minutes = remaining_seconds // seconds_in_minute
    seconds = remaining_seconds % seconds_in_minute

    return int(months), int(days), int(hours), int(minutes), int(seconds)
