# 안녕하세요, 저는 진수 입니다.
# -----------------------------------
# 제 가족들의 이름은 아래와 같아요.
# * 희영 	* 찬영 	* 준영 	* 채영
# -----------------------------------
# - 주소 : 롯데캐슬
# - 가훈 : 극기상진
# - 소망 : 세계일주

def i(my_name, *family_names, **family_info):
    print("안녕하세요, 저는 {0}입니다.\n{1}\n"\
          "제 가족들의 이름은 아래와 같아요".format(my_name, "*" * 40))

    for name in family_names:
        print("{0} {1}".format("*", name), end = '\t')

    else:
        print('\n', '*' * 40)

    for info in family_info.keys():
        print("- {0} : {1}".format(info, family_info[info]))

i("진수", "희영", "찬영", "준영", "채영", 주소 = "롯데캐슬", 가훈 = "극기상진", 소망 = "세계일주")




