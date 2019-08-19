count = input("숫자를 입력해 주세요. [1 ~ 100] => ")
numbers = list("1234567890")
dummy = 0
for i in range(1, int(count)):
    dummy += i
print(dummy)