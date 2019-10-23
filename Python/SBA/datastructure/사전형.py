# # 사전형 생성
#bans = { '잎새반':'찬영이',
#          '열매반':'예영이',
#          '햇살반':'준영이',
#          '열매반':'채영이', }
#
# # 타입 확인
# type(bans)
# print(bans)
# # 키값이 중복된 거는 지워짐.
# print('반의 갯수:', len(bans))
#
# # 추가
# bans['반반반'] = '이이이'
# print(bans)
#
# # 변경
# bans['잎새반'] = '서영이'
# print(bans)
#
#
# bans['잎새반'] = ['잎잎잎']
# print(bans)

# 어떻게 하면 키 값을 변경할 수 있을까?


customer = {
    "name"    : "김진수",
    'gender'  : '남자',
    "email"   : "bigpycraft@gmail.com",
    "company" : "빅파이크래프트",
    "address" : "서울시 중구 청파로"
}
# 전체 키가 다 나옴
print('customer.keys()   \t= ', customer.keys())
# 전체 값이 다 나옴
print('customer.values() \t= ', customer.values())
# 둘 다 나옴
print('customer.items()  \t= ', customer.items())
print('-'*50)

#아이템으로 나눠서 키와 밸류에 양쪽 다 넣어주고 프린트에 출력
for key, value in customer.items():
    print('%s\t : %s' %(key, value))