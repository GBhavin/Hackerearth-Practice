def RemoveSameChar(a, b):
    subStringa = ""
    subStringb = ""
    ii = 0
    for i in range(len(a)):
        ii = i
        index = b.find(a[i])
        if index != -1:
            subStringa = a[:index] + a[index + 1:]
            subStringb = b[:i] + b[i + 1:]
            break

    if ii == len(a):
        return len(a) + len(b)

    return RemoveSameChar(subStringa, subStringb)


counter = int(input())
for x in range(counter):
    a = input()
    b = input()
    print(RemoveSameChar(a, b))
