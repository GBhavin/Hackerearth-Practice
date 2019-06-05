counter = int(input())

for i in range(counter):
    matchstick = 0
    inputNumber = input()
    for num in inputNumber:
        number = int(num)
        if number == 1:
            matchstick += 2
        elif number == 2 or number == 3 or number == 5:
            matchstick += 5
        elif number == 4:
            matchstick += 4
        elif number == 6 or number == 9 or number == 0:
            matchstick += 6
        elif number == 7:
            matchstick += 3
        elif number == 8:
            matchstick += 7

    if matchstick % 2 == 0:
        matchstick = matchstick // 2
        print("1" * matchstick)
    else:
        matchstick = (matchstick-3) // 2
        print("7" + "1" * matchstick)
