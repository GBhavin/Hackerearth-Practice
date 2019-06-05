import time

def isPrime(counter):
    # Corner cases
    if (counter <= 1):
        return False
    if (counter <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (counter % 2 == 0 or counter % 3 == 0):
        return False

    i = 5
    while(i * i <= counter):
        if (counter % i == 0 or counter % (i + 2) == 0):
            return False
        i = i + 6

    return True


numberRange = list(map(int, input().split()))
finalRange = []
start = time.time()

for num in range(numberRange[0], numberRange[1]):
    if isPrime(num):
        numSplit = [int(i) for i in str(num)]
        numAddition = 0
        for i in numSplit:
            numAddition += i
        if isPrime(numAddition):
            finalRange.append(num)

print(*finalRange)
