time_mins = int(input())
start_hours = int(input())
start_mins = int(input())

time_mins = (start_hours * 60) + start_mins + time_mins
time_hours, time_mins = (time_mins // 60), (time_mins % 60)


if time_hours <= 24:
    print(time_hours, time_mins)
else:
    print((time_hours - 24), time_mins)
