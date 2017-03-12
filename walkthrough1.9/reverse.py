#create a function that reverses a dictionary
initialDict = {4:'yes', 'hello': 2, "no": [2,3,4]}
newDict = {}
for (k,v) in initialDict.items():
    newDict[str(v)] = k
print(newDict)    
