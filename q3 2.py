def getMaxIndex(numList):
    max = 0
    index = 0
    for i in range(len(numList)):
        if(numList[i] > max):
            max = numList[i]
            index = i
    return index

print(getMaxIndex([30, 2, 88, 33, 73, 91, 34, 56, 18, 47]))
