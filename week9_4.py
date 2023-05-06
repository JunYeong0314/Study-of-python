a, b, c = input('a, b, c를 입력하시오: ').split()
a = int(a)
b = int(b)
c = int(c)
for i in range(1,a+1):
    if(i%b == 0):
        print(i, end=' ')
print()
for i in range(1,a+1):
    if(i%c == 0):
        print(i, end=' ')
    
