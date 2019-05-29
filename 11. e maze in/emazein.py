data = input()
lData = data.count("L")
rData = data.count("R")

uData = data.count("U")
dData = data.count("D")

print(rData - lData, uData - dData)
