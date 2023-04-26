while(True):
    dan = int(input('0이 아닌 숫자를 넣으세요, 끝내려면 0을 입력하세요:'))

    if(dan == 0):
        break

    for i in range(1,10):
        print(dan,'X',i,'=',dan*i)
