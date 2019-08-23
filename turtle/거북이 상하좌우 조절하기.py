import  turtle as t
print('거북이를 키보드로 움직일 수 있는 프로그램입니다.')
print('/t A : 좌측 이동')
print('/t D : 우측 이동')
print('/t W : 상단 이동')
print('/t S : 하단 이동')

input("이동하고 싶은 방향으로 키보드를 누르고 엔터 해 주세요.")

t.shape("turtle")
t.pensize(5)
t.color('black')
t.speed(100)

while True:
    direction = input('[A, D, W, S]: ')
    if 'X' == direction.upper():
        break
    elif 'D' == direction.upper():
        t.setheading(0)
    elif 'W' == direction.upper():
        t.setheading(90)
    elif 'A' == direction.upper():
        t.setheading(180)
    elif 'S' == direction.upper():
        t.setheading(270)
    else:
        continue

    t.forward(50)

print("\n 프로그램을 종료하였습니다!")
t.done()