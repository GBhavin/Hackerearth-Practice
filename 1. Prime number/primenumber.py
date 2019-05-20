def isPrime(counter):
    if counter <= 1:
        return False

    for x in range(2, counter):
        if counter % x == 0:
            return False
    else:
        return True


counts = input("Give count for prime number. ")
start = 1
try:
    count = int(counts)
except:
    pass

while start <= count:
    if isPrime(start):
        print(start, end=" ")
    start += 1
