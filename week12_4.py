import random


def randNum(start, end, num):
    randList = []
    for i in range(num):
        randList.append(random.randint(start, end))
    return randList
def mySum(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

rand1 = randNum(1, 5, 3)
rand2 = randNum(1, 100, 5)
rand3 = randNum(1, 100, 5)

print(f'({rand1},{mySum(rand1)})')
print(f'({rand2},{mySum(rand2)})')
print(f'({rand3},{mySum(rand3)})')
