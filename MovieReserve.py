seat = [[0 for col in range(10)] for row in range(10)]

def printScreen():
    print("      screen         ")
    for i in seat:
        for j in i:
            print(j, end = " ")
        print()
    

while(1):
    printScreen()
    seat_row, seat_col = input("좌석을 선택하세요 (ex: 0행1열 = 0 1 , 1로 표기된 좌석은 선택불가) : ").split()
    seat_row = int(seat_row)
    seat_col = int(seat_col)

    if(seat_row >= 10 or seat_col >= 10):
        print("범위를 초과한 좌석입니다.")
    elif(seat[seat_row][seat_col] == 1):
        print("이미 예매된 좌석입니다.")
    else:
        seat[seat_row][seat_col] = 1
        print(f'{seat_row} {seat_col} 좌석 예매 완료 !')
        
    choice = input('계속해서 예매하시겠습니까 ? (Y / N) : ')
    if(choice == 'N'):
        print("프로그램 종료")
        print("최종 좌석 현황")
        printScreen()
        break
    else:
        print("잘못된 입력 방식입니다. 다시 시도해주세요")

    
    


