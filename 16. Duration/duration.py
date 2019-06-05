from datetime import timedelta

counter = int(input())
for i in range(counter):
    data = input().split()
    t1 = timedelta(hours=int(data[0]), minutes=int(data[1]), days=0,
                   seconds=0, microseconds=0, milliseconds=0, weeks=0)
    t2 = timedelta(hours=int(data[2]), minutes=int(data[3]), days=0,
                   seconds=0, microseconds=0, milliseconds=0, weeks=0)
    difference = str(t2-t1).split(":")
    hour = difference[0]
    minute = difference[1]
    if minute.startswith("0"):
        minute = minute.replace("0", "", 1)
    print(hour, minute)
