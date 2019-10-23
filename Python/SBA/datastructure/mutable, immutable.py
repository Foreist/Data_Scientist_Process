# Immutable 예제
hello = '안녕하세요!'    # hello 문자열형 변수 선언

print(hello)             # hello 값 확인
print(id(hello))         # hello 객체 식별자 확인

hello = '반값습니다!'    # hello 값 변경

print(hello)             # hello 값 확인
print(id(hello))         # hello 객체 식별자 확인


# Mutable 예제
hello_list = ['안녕하세요!']    # 리스트형 선언

print(hello_list)               # 리스트 값 확인
print(id(hello_list))           # 리스트 객체 식별자 확인

hello_list[0] = '반갑습니다!'   # 리스트 첫번째 항목 값 변경하기

print(hello_list)               # 리스트 값 확인
print(id(hello_list))           # 리스트 객체 식별자 확인