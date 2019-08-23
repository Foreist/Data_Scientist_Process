count = input("숫자를 입력해 주세요. [1 ~ 100] => ")

numbers = list("1234567890")

dummy = 0

fac = [1]


for check_count in range(len(list(count))):

    if (len(list(count)) - 1) >= check_count:

        if count[check_count] not in numbers:
            dummy += 1
            break
        # 숫자라면 해당 시퀀스는 넘어감
        else:
            pass

# dummy에 값이 하나라도 있으면 숫자가 아니라고 출력
if dummy != 0:
    print("입력한 값이 숫자가 아닙니다.")
# dummy에 값이 없으면 전부 숫자이니까 factorial 계산
else:
    # for문으로 dummy에 숫자값을 계속 더해서 해당 숫자값까지의 합계를 구함
    for i in range(1, int(count)):
        dummy += i

    # 출력해줄 문자열이랑 해서 이쁘게 정리
    print("입력한 숫자 : {0}\n{1}\n" \
          "{0}까지의 합계 및 팩토리얼 테이블 구하기!!\n{1}\n" \
          "{0}까지의 합계는 {2}입니다.\n" \
          "아래는 팩토리얼 테이블입니다.".format(count, '-' * 50, dummy))

    # factorial 계산
    for j in range(int(count) + 1):
        # 0이라면 그냥 1 출력(규칙성이 없는 라인)
        if j == 0:
            print("{0}!\t\t = {0}".format(fac[j]))
        # 1 이상이면 해당 숫자 -1한 fac index에 현 숫자를 곱하고 append로 fac에 넘겨줌
        else:
            fac.append(fac[j - 1] * j)
            print("{0}!\t\t = {1}".format(j, fac[j]))