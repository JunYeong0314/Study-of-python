import random

seat = [["□" for j in range(10)] for i in range(10)]
reservePeople = [] # 예매 고객 번호 데이터
reserveSeat = [] # 예매 고객 좌석 데이터
peopleCnt = 0 # 예매 인원

def isRight(i, j):
    if i < 0 or i >= 10 or j < 0 or j >= 10:
        return False
    else:
        return True

def statusSeat():
    print("===== screen =====")
    for i in range(10):
        for j in range(10):
            print(seat[i][j], end=" ")
        print()

def reserve(i, j):
    if isRight(i, j):
        if seat[i][j] == "■":
            print("이미 예약된 자리입니다.")
            return False
        else:
            seat[i][j] = "■"
            print(f'{i+1}, {j+1} 좌석 예매완료!')
            return True
    else:
        print("좌석 범위에 벗어난 수입니다.")
        return False

def deleteSeat(i, j):
    if isRight(i, j):
        seat[i][j] = "□"
        print(f'{i+1}, {j+1} 좌석 취소완료!')
    else:
        print("좌석 범위에 벗어난 수입니다.")

def myMovie(num):
    for i in range(peopleCnt):
        if num == reservePeople[i]:
            check = reserveSeat[i]
            print(f"예매 번호: {num}")
            print(f"예매 좌석: {int(check[0])+1}, {int(check[1])+1}")
            return
    print("해당 예매 번호가 없습니다.")

while True:
    pick = int(input("1. 예매 2. 예매 취소 3. 좌석 현황 4. 예매 내역 5. 종료: "))

    if pick == 5:
        break

    if pick == 1:
        j, k = map(int, input("(총 10행10열 좌석) 좌석을 선택하세요(ex. 1행 1열 자리 입력 = 1 1): ").split())
        j -= 1
        k -= 1
        if reserve(j, k):
            reserveSeat.append([j, k])
            num = random.randint(1000000, 9999999)
            reservePeople.append(num)
            print(f"예매 번호: {num}")
            peopleCnt += 1

    elif pick == 2:
        n = int(input("예매 번호를 입력하세요: "))
        for i in range(peopleCnt):
            if reservePeople[i] == n:
                check = reserveSeat[i]
                deleteSeat(check[0], check[1])
                del reservePeople[i]
                del reserveSeat[i]
                peopleCnt -= 1
                break
        else:
            print("해당 예매 번호가 없습니다.")

    elif pick == 3:
        statusSeat()

    elif pick == 4:
        n = int(input("예매 번호를 입력하세요: "))
        myMovie(n)
    else:
        print("잘못된 번호를 입력하셨습니다.")
