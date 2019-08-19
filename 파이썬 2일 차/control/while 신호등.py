boo = 'False'
while boo == 'False':
    signal_color = input('신호등의 색을 두 개 중 하나만 선택해서 입력해/'
                         '주세요.(B/R): ')
    if signal_color == 'B':
        print("신호등이 파란색입니다. 길을 건너도 됩니다.")
        boo = 'True'
    elif signal_color == 'R':
        print("신호등이 빨간색입니다. 건너시면 안 됩니다.")
        boo = 'True'
    else:
        print("없는 색입니다.")
        continue

