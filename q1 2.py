score = [66,80,92,70,55]

def getScore(s):
    result = ""
    if(s >= 90 and s <= 100):
        result = 'A'
    elif(s >= 80 and s < 90):
        result = 'B'
    elif(s >= 70 and s < 80):
        result = 'C'
    else:
        result = 'D'
    return result

passCnt = 0
nonPass = 0

for i in range(5):
    print(f'{i+1} 번 학생의 시험점수: {score[i]} 학점: {getScore(score[i])}\n')
    if(getScore(score[i]) == 'D'):
        nonPass += 1
    else:
        passCnt += 1
print(f'패스한 학생 수: {passCnt}')
print(f'패스하지 못한 학생 수: {nonPass}')
    
    
        
