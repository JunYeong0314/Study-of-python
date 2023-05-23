def reverseStr(str):
    list_reverse = []

    for i in range(len(str)-1, -1, -1):
        list_reverse.append(str[i])
        
    return ''.join(list_reverse)

print(reverseStr('ABCD'))
        

