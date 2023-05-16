list = []

def make_order():
    order_list = []
    while(1):
        num = int(input('품목번호 입력 : '))
        if num == -1:
            print('선택 종료')
            break

        if num == 1:
            order_list += [1, 1000]
        elif num == 2:
            order_list += [2, 1500]
        elif num == 3:
            order_list += [3, 1500]
        elif num == 4:
            order_list += [4, 2000]
    return order_list

def compute_item(list):
    sum = 0
    for i in range(len(list)):
        if(i%2 != 0):
            sum += list[i]
    return sum

item_list = make_order()
print('총합:',compute_item(item_list))




