password = ""

def getPassword(p):
    result= ""
    for i in p:
        if(i == 'A'):
            result += '1!'
        elif(i == 'B'):
            result += '2@'
        elif(i == 'C'):
            result += '3#'
        elif(i == 'D'):
            result += '4$'
        else:
            result += '5%'
    return result
            
while(1):
    password = input("A, B, C, D, E로 구성된 문자열 입력(종료: 0): ")

    if(password == '0'):
        break
    print(f'문자열: {password}, 암호화: {getPassword(password)}\n')
    
