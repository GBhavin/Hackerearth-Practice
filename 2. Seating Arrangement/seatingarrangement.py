counter = input()
try:
    count = int(counter)
except:
    pass

for i in range(1, count + 1):
    seats = input()
    try:
        seat = int(seats)
    except:
        pass

    module = seat % 12
    oppositeSeat = 0
    if module == 0 or module >= 7:
        module = 12 if module == 0 else module
        oppositeSeat = (seat - (module - (13 - module)))
    elif module <= 6:
        oppositeSeat = (seat + (13 - module) - module)

    if module == 1 or module == 6 or module == 7 or module == 12:
        print(oppositeSeat, end=" WS")
    elif module == 2 or module == 5 or module == 8 or module == 11:
        print(oppositeSeat, end=" MS")
    elif module == 3 or module == 4 or module == 9 or module == 10:
        print(oppositeSeat, end=" AS")
