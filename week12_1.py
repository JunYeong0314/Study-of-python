def weekday_to_digit(day1):
    for i in range(7):
        if(weekdays[i] == day1):
            return i

def date_to_day_difference(month, day):
    sum = 0
    for i in range(month-1):
        sum += daysinmonth[i]
    return (sum + day)-1

def digit_to_weekday(num):
    result = (day1+difDay)%7
    return weekdays[result]


weekdays=["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"]
daysinmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day1 = weekday_to_digit(input("올해 1월1일의 요일 : "))
birthMonth = int(input("생일의 월 : "))
birthDay = int(input("생일의 일 : "))

difDay = date_to_day_difference(birthMonth, birthDay)
myBirthDay = digit_to_weekday(difDay)

print(f'1월1일부터 생일까지 일수차 : {difDay}')
print(f'내 생일의 요일 : {myBirthDay}')