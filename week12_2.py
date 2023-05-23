def weekday_to_digit(day1):
    for i in range(7):
        if(weekdays[i] == day1):
            return i

def date_to_day_difference(month, day):
    sum = 0
    for i in range(month, birth_month-1):
        sum += daysinmonth[i]
    return sum+(daysinmonth[month-1]-day)+birth_day

def digit_to_weekday(num):
    result = (today+difDay)%7
    return weekdays[result]


weekdays=["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"]
daysinmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

today = weekday_to_digit(input("오늘 날짜의 요일 : "))
today_month = int(input("오늘 날짜의 월 : "))
today_day = int(input("오늘 날짜의 일 : "))
birth_month = int(input("생일의 월 : "))
birth_day = int(input("생일의 일 : "))

difDay = date_to_day_difference(today_month, today_day)
myBirthDay = digit_to_weekday(difDay)

print(f'오늘부터 생일까지 일수차 : {difDay}')
print(f'내 생일의 요일 : {myBirthDay}')