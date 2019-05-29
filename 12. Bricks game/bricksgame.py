totalBricks = int(input())

patlu = 0
motu = 0
totalCounter = 0

for counter in range(1, totalBricks):
    patlu = counter
    motu = (counter * 2)

    totalCounter += patlu

    if totalCounter >= totalBricks:
        print("Patlu")
        break
    
    totalCounter += motu

    if totalCounter >= totalBricks:
        print("Motu")
        break
    