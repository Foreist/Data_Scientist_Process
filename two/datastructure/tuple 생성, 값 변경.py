# 튜플 생성
girl_group = ('트와이스', '레드벨벳', '에이핑크', '걸스데이', '우주소녀')

# 에러가 떠요.
girl_group[1] = '블루벨벳'

# 변경하는 방법은 리스트로 변경 후 튜플로 다시 변경
list(girl_group)

#위의 식으로는 하면 안 되고 주솟값을 적어줘야 함
type(girl_group)

girl_group = list(girl_group)

# 레드벨벳을 블루벨벳으로 바꿔보자
list_girl_group[list_girl_group.index('레드벨벳')] = '블루벨벳'

list_girl_group

# 다시 튜플로 변경

girl_group = tuple(list_girl_group)
type(girl_group)