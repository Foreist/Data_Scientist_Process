# 결과 표시

price = int(input("책의 정가는?"))
sales = int(input("발행 부수는?"))
per = float(input("인세율(퍼센트)은?"))

# 디폴트 값을 넣으려면 오른쪽 최우측부터 넣어야 함(안 적으면 어느 곳의 값을 안 적었는지 모르기 때문에)
def royalty(price, sales, per = 3):
    rate = per / 100
    rt = int(price * sales * rate)
    return print("인세는 {0}원입니다.".format(rt))

royalty(price, sales, per)


