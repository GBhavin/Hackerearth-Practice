isn = input()
total = 0
if len(isn) == 10:
    for i in range(1, 11):
        total += i * int(isn[i-1])

    if total % 11 == 0:
        print("Legal ISBN")
    else:
        print("Illegal ISBN")
else:
    print("Illegal ISBN")
