counter = int(input())
toffee = 0
for i in range(counter):
    data = input().split()
    data1 = int(data[0])
    data2 = int(data[1])
    if (data2 > data1) and (((22/7)*(data1)*2) <= (data2*100)):
        toffee += 1

print(toffee)
