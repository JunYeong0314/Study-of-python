def checkLen(str):
    if(len(str) > 15):
        return True
    else:
        return False

while(1):
    s = input('문자열을 입력하세요: ')
    if(checkLen(s) == True):
        print('통과되었습니다')
        break
    else:
        print('다시 입력하세요')
