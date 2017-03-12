#create a function Factors that generates a dictionary with all of the factors until n
factDict = {}
n = int(input('enter an integer'))
for number in range(1,n+1):
    factorList = []
    for x in range(1,number+1):
        if number % x == 0:
            factorList.append(x)
    factDict[number] = factorList
print(factDict)
