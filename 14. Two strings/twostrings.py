counter = int(input())

for i in range(counter):
    inputs = input().split()
    if sorted(inputs[0]) == sorted(inputs[1]):
        print("YES")
    else:
        print("NO")
