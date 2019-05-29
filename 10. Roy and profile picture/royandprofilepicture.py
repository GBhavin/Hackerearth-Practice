base = int(input())
counter = int(input())

for i in range(0, counter):
    data = input().split()
    data1 = int(data[0])
    data2 = int(data[1])

    if data1 < base or data2 < base:
        print("UPLOAD ANOTHER")
    elif data1 == data2:
            print("ACCEPTED")
    else:
        print("CROP IT")