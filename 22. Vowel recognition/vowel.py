def splitSubstring(data):
    splitArray = []
    for i in range(len(data)):
        splitArray.append(data[0:i+1])

    return splitArray
    
def countOfVowels(split):
    count = 0
    for item in split:
        for subItem in item:
            if subItem in vowels:
                count += 1

    return count

counter = int(input())
for c in range(counter):
    data = input()
    vowels = "AaEeIiOoUu"
    vowelsCout = 0

    for i in range(len(data)):
        subArray = splitSubstring(data[i:])
        vowelsCout += countOfVowels(subArray)

    print(vowelsCout)