def hello():
    print('Hello world!')
hello()

def add_sub(a, b):
    return a+b, a-b
x, y = add_sub(10, 20)
print(x, y)

a = [10, 10, 10, 10, 10]
x = 0
for i in a:
    x += i
print(x)

def sum(num_list):
    sum_result = 0
    for num in num_list:
        sum_result += num
    return sum_result
sum(a)

def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)
print_numbers(10, 20, 30)
