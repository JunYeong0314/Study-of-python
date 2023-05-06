a = int(input('입력:'))
s = 0
for i in range(a+1):
    if(i%2 != 0):
        s += i
        print(s)
