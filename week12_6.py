def isSame(str):
    list_reverse = []

    for i in range(len(str)-1, -1, -1):
        list_reverse.append(str[i])
    list_reverse = ''.join(list_reverse)

    return list_reverse == str 

print(isSame('abcba'))
print(isSame('abcde'))
print(isSame('기러기'))