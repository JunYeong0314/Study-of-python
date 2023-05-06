s_len = 1
x=0
y=0

s = input('뱀의 이동방향을 입력하시오: ')

for i in s:
    if(i == 'L'):
        x -= 1
    elif(i == 'R'):
        x += 1
    elif(i == 'U'):
        y += 1
    elif(i == 'D'):
        y -= 1
    if(x == y and x!=0 and y != 0):
        s_len += 1

print(f'뱀의 길이는 {s_len} 입니다.')
