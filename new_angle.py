def find_bigger(begin_div,over_div):
    duplicate_begin = begin_div
    duplicate_over = over_div
    if begin_div < over_div:
        begin_div = duplicate_over
        over_div = duplicate_begin
        return begin_div
    else:
        return begin_div
def overnd_interval(interval):
    if interval %2 != 0:
        interval+=1
        print(interval)
        return interval
    else:
        return interval


def new_angle(min_interval,interval_servo,begin_div,over_div,key):
    intervals_servo  = overnd_interval(interval_servo)
    interval_div =round(intervals_servo )/round(min_interval)
    bigger_angle_for_div = find_bigger(begin_div,over_div)
    angle_div = round(int(bigger_angle_for_div)) / round(int(interval_div))
    safe = round(angle_div)
    execute = [round(angle_div)]
    for i in range(key):
        angle_div += safe
        if angle_div == over_div:
            angle_div-= safe
            safe*= -1
        if angle_div <= 0:
            angle_div += angle_div
            safe*= -1
        execute.append(round(angle_div))
    print(len(execute))
    return execute



print(new_angle(1,5,2,180,40))
print(new_angle(1,5,2,180,40))
