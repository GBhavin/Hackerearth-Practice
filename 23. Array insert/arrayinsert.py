arrayCount, queriesCount = list(map(int, input().split()))

array = list(map(int, input().split()))

for i in range(queriesCount):
    operation, xPosition, yPosition = list(map(int, input().split()))
    if operation == 1:
        array[xPosition] = yPosition
    elif operation == 2:
        print(sum(array[xPosition:yPosition+1]))

