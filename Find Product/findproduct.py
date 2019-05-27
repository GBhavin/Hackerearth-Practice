inputs = int(input())
answer = 1
data = input()
array = data.split()
for i in range(inputs):
    answer = (answer * int(array[i])) % (10**9 +7)

print(answer)