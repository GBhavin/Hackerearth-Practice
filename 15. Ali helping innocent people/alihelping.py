def isOdd(num1, num2):
    return ((int(num1) + int(num2)) % 2) == 0


data = input()
vowel = ["A", "E", "I", "O", "U", "Y"]

if data[2] in vowel:
    print("invalid")
elif not isOdd(data[0], data[1]):
    print("invalid")
elif not isOdd(data[3], data[4]):
    print("invalid")
elif not isOdd(data[4], data[5]):
    print("invalid")
elif not isOdd(data[7], data[8]):
    print("invalid")
else:
    print("valid")
