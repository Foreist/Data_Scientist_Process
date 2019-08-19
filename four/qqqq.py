# init과 no init 연습
# 반에 사람은 3명에 1번 진선, 2번 효인, 3번 라애가 있음.
class room:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def Numbers(self):
        print("안녕하세요. {0}번,".format(self.number), end = '')

    def Names(self):
        print("{0}입니다. 잘 부탁드립니다.".format(self.name))

room(2, "리루").Numbers()
room(2, "리루").Names()


#     def main(self):
#         self.__init__()
#         # 로또 주문
#         self.buy()
#
#         # 주문한 갯수만큼 로또번호 생성
#         self.genrate_list()
#
#         self.lotto_num()
#
#         # 로또번호 출력
#         self.idx()
#
#
# lotto = Lotto()
# lotto.main()