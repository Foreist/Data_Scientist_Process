dummy = "The BigpyCraft find the information to design valuable society with Technology & Craft."

#print("모두 대문자로 출력 \n {0}".format(dummy.upper()))
#print("모두 소문자로 출력 \n {0}".format(dummy.lower()))

# for i in dummy:
#     if i.islower():
#         box += i.upper()
#     else:
#         box += i.lower()
#
# print("대소문자 바꿔서 출력 \n{0}".format(box))

# 파이썬스러운 코드

box = [i.upper() if i.islower() else i.lower() for i in dummy]
print("대소문자 바꿔서 출력 \n{0}".format(''.join(box)))


