import turtle
# as t처럼 해주는 문구
t = turtle.Turtle()
# 거북이가 그려줌
t.shape('turtle')

# 점의 거리는  50
dot_distance = 50
# 가로
width  = 5
# 세로
height = 4

# 펜을 든 상태에서 시작
t.penup()

# 5개씩 4번 반복
for y in range(height):
    for i in range(width):

        # 점을 찍음
        t.dot()
        # dot_distance만큼 앞으로 감
        t.forward(dot_distance)

    # 상단 for문을 다 실행 후, 왔던 만큼 다시 감
    t.backward(dot_distance * width)
    # 우측으로 90도만큼 회전
    t.right(90)
    # 50만큼 앞으로 이동
    t.forward(dot_distance)
    # 왼쪽으로 90도만큼 회전
    t.left(90)

turtle.done()