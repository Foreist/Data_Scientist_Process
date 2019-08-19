# 실습2. (김재경, 김태웅)
import random as r


class Lotto:
    # count = 0
    # lotto_list = []
    # lo_num = []
    def __init__(self):
        self.count = count
        self.Lotto_list = Lotto_list
        self.Lo_num = Lo_num

    # 로또주문
    def buy(self):
        count = int(input("몇개 사시겠습니까?"))
        self.count = count
        # return count

    # 로또번호 1세트 생성 (오름차순 정렬)
    def lotto_gen(self):
        num = []
        for i in range(6):
            num.append(r.randrange(1, 11))
        return sorted(num)

    # 로또 주문수만큼 로또생성
    def genrate_list(self):
        # lotto_list = []
        for i in range(self.count):
            self.lotto_list.append(self.lotto_gen())

    # 일련번호 생성
    def lotto_num(self):
        num = r.randrange(100000, 999999)
        for i in range(self.count):
            while num in self.lo_num:
                num = r.randrange(100000, 999999)
            self.lo_num.append(num)

    # 일련번호랑 로또랑 한개씩 가져오기
    def idx(self):
        lotto_list = self.lotto_list
        lo_num = self.lo_num
        for lo_numm in range(len(lotto_list)):
            print(" 일련번호는 {0}번, 로또 번호는 {1}입니다.".format(lo_num[lo_numm], lotto_list[lo_numm]))

    def main(self):
        self.__init__()
        # 로또 주문
        self.buy()

        # 주문한 갯수만큼 로또번호 생성
        self.genrate_list()

        self.lotto_num()

        # 로또번호 출력
        self.idx()


lotto = Lotto()
lotto.main()



