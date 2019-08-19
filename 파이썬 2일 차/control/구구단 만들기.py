num = int(input("출력할 단을 입력해주세요. [2~9]  "))
print("{0} 단 출 력".format(num)); print('-' * 19);
for count in range(1, 10):
    print("{0} * {1} = {2}".format(num, count, num * count))