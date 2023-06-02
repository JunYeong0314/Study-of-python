score = [66,80,92,70,55]

def getSort(s):
    tmp = ""
    for i in range(len(s)):
        j = i
        for j in range(len(s)):
            if(s[i] > s[j]):
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp 
    return s

def getSt(s):
    result = 0
    if(s == 66):
            result = 1
    elif(s == 80):
            result = 2
    elif(s == 92):
            result = 3
    elif(s == 70):
            result = 4
    else:
            result = 5
    return result

sortScore = getSort(score)
def getSt2(s):
    result = 0
    print(s)
    for i in range(len(sortScore)):
        if(sortScore[i] == s):
            result = i+1
            return result
        else:
            return 0


for i in range(len(score)):
    print(f'{i+1} 등 학생 번호: {getSt(sortScore[i])}번\n')


    
    
        
