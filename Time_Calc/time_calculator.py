def add_time(start, duration, day=''):
    start_h, start_m = start.split(':')
    start_m, meridiem = start_m.split(' ')
    dur_h, dur_m = duration.split(':')

    start_h = int(start_h)
    start_m = int(start_m)
    dur_h = int(dur_h)
    dur_m = int(dur_m)

    end_h = start_h
    end_m = start_m + dur_m
    days_count = 0

    new_time = ""

    if dur_h > 24:
        days_count += int(dur_h / 24)
        dur_h -= 24 * days_count

    if end_m >= 60:
        dur_h += int(end_m / 60)
        end_m -= 60

    
    for h in range(dur_h):
        if end_h == 12:
            end_h = 1
        
        else:
            end_h += 1

            if end_h == 12:
                if meridiem == 'PM':
                    meridiem = 'AM'
                    days_count += 1
                else:
                    meridiem = 'PM'


    new_time = "{}:{} {}".format(str(end_h), str(end_m).zfill(2), meridiem)

    if days_count == 1:
        new_time += " (next day)"
    elif days_count > 1:
        new_time += " ({} days later)".format(days_count)

    return new_time