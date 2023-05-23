import random

def randNum_sum(start, end, num):
    randList = []
    sum = 0

    for i in range(num):
        randList.append(random.randint(start, end))
        sum += randList[i]

    return f'({randList}, {sum})'

print(randNum_sum(1, 5, 3))
print(randNum_sum(1, 100, 5))
print(randNum_sum(1, 100, 5))