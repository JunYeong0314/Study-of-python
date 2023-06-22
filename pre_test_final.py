dept = 300

day=0
while(dept > 0):
    dept -= 42
    if(dept < 0):
        day -= 1
    day += 1
    
print(day,'일')
