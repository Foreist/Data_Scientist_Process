import turtle as t

print('다각형을 그리는 예제입니다.')
var1 = input('변의 수를 입력해주세요? [3-8] ')
var2 = input('한변의 길이를 입력해주세요? [100-200] ')
# var2 = str(150)

# 변의 수를 변수에 저장
num_of_side = int(var1)
# 변의 길이를 변수에 저장
len_of_side = int(var2)

# 변을 그리고 몇 도를 틀어야 하는지 계산
angle = 360.0 / num_of_side
# 변의 길이에 따른 색 분류
c_mod = num_of_side % 3
color = 'red' if c_mod==0 else 'green' if c_mod==1 else 'blue'

# 시작
t.begin_fill()
# 변의 길이에 따른 색 분류를 한 것을 토대로 색을 설정
t.color(color)
# 펜 사이즈 설정
t.pensize(5)

# 변의 갯수만큼 i에 넣어줌
for i in range(num_of_side):
    # 한 변의 길이를 forward에 넣어줌
    t.forward(len_of_side)
    # 각도 변환
    t.left(angle)
# 값 채우기
t.end_fill()
# 끝
t.done()