def alarm_clock(day, vacation):
    if 1 <= day <= 5:
        if vacation:
            return "10:00"
        else:
            return "7:00"
    if vacation:
        return "off"
    return "10:00"
