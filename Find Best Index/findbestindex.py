def normalNumber(number):
    return (number * (number + 1) / 2)


def getSum(index, array, arrayLength):
    element = 1
    sum = 1
    temp = 1
    for i in range(1, int((arrayLength - index) / 2)):
        sum = normalNumber(i)
        if sum == (arrayLength - index):
            element = sum
            break
        elif sum > (arrayLength - index):
            element = temp
            break
        else:
            pass

        temp = sum

    total = 0
    for i in range(0, int(element)):
        total += int(array[i + index])

    return total


counter = int(input())
data = input()
array = data.split()

tempsum = 0
sum = 0
index = 0
for i in range(counter):
    tempsum = getSum(i, array, counter)
    if tempsum > sum:
        sum = tempsum
    else:
        pass

print(sum)
