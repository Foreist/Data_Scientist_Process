# 실습1. (김재경, 김태웅)

box = list(str(2 ** 1000))
counts = 0

for i in box:
    counts += int(i)
print(counts)