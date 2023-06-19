import turtle
import random

def draw_to_point(x, y):
    # 코드 작성
    turtle.pencolor((r, g, b))  # 선의 색 설정
    turtle.pendown()  # 선 그리기 설정
    turtle.goto(x, y)  # (x, y)까지 선 그리기

def move_without_drawing(x, y):
    # 코드 작성
    turtle.penup()  # 선 그리지 않기 설정
    turtle.goto(x, y)  # 커서 이동

def change_setting(x, y):
    # 코드 작성
    global r, g, b
    turtle.pensize(random.randrange(1, 10))  # 선의 굵기 설정
    r, g, b = random.random(), random.random(), random.random()  # 랜덤한 색 설정

r, g, b = 0.0, 0.0, 0.0
turtle.title("코딩입문 turtle")
turtle.shape("turtle")
turtle.pensize(10)
turtle.onscreenclick(draw_to_point, 1)
turtle.onscreenclick(change_setting, 2)
turtle.onscreenclick(move_without_drawing, 3)
turtle.done()
