def comput_salary(hour):
    money = 0
    if(hour > 40):
        money = 400000
        money += (hour-40)*(10000*1.5)
    else:
        money += hour*10000
    return money
print(comput_salary(30))
print(int(comput_salary(45)))
