a = 0
b = 7
counter = int(input())
for i in range(counter):
    floor = int(input())
    half = (b + a)/2
    if floor <= half:
        a = floor
        print("A")
    else:
        b = floor
        print("B")
