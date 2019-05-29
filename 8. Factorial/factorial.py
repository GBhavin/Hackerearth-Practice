def recurion(start, end):
    start = start % end 

data = input().split()
data1 = int(data[0])
data2 = int(data[1])

data3 = int(data[2])
finalCounter = 0
for counter in range(data1, data2 + 1):
    if counter % data3 == 0:
        finalCounter += 1

print(finalCounter)