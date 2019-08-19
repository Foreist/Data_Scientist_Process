# 실습1. (김재경, 김태웅)

import random as r

buy = int(input("몇 개 구매하시겠습니까?"))

class lotto:

    def gen(self, count):
        lotto_box = []
        lottos_box = []
        for j in range(int(count)):
            for i in range(6):
                lotto_box.append(r.randrange(1, 11))
            lottos_box.append(sorted(lotto_box))
            lotto_box = []
        return lottos_box

count = 0

for i in lotto().gen(buy):
    count += 1
    print(""""" 일련번호는 {0}번, 로또 번호는{1}입니다.""".format(count, i))