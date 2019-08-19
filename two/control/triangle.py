for i in range(1, 10, 2):
    print("{0:^10}".format(i * '*'))

#우측 정렬 삼각형
for i in range(1, 10, 2):
    print("{0:>10}".format(i * '*'))

# 선생님 방법으로 만든 삼각형
for i in range(1, 10, 2):
    mark = " " * int((10 - i) / 2) + "*" * i
    print(mark)