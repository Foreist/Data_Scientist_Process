# break vs. continue vs. pass
scope = list(range(1, 100))

for num in scope:

    if num <= 10:
        # 패스는 그냥 넘어가는 거
        if num % 2 == 0:
            pass
            print(num, 'is even number.')

        # 컨티뉴는 밑으로 안 내려가고 다시 위의 첫 if로
        else:
            continue
            print(num, 'is odd number.')
    # break는 바로 빠져 나옴
    else:
        print(num, 'is bigger than ten')
        break
        print('after break')

print('프로그램을 종료합니다.')
