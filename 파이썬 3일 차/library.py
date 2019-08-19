books = list()      # 책 목록 선언
# many_page = []
# recommends = []
# all_pages = 0
# pub_companies = []

# 책 목록 만들기
books.append({'제목':'파이썬 프로그램', '출판연도':'2016', '출판사':'A', '쪽수':200, '추천유무':False})
books.append({'제목':'플랫폼 비즈니스', '출판연도':'2013', '출판사':'B', '쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014', '출판사':'A', '쪽수':296, '추천유무':True})
books.append({'제목':'외식경영 전문가', '출판연도':'2010', '출판사':'B', '쪽수':526, '추천유무':False})
books.append({'제목':'십억만 벌어보자', '출판연도':'2013', '출판사':'A', '쪽수':248, '추천유무':True})

#for book in books:
    # if book["쪽수"] >= 250:
    #     many_page.append(book["제목"])
    #
    # if book["추천유무"] >= True:
    #     recommends.append(book["제목"])
    #
    # all_pages += book["쪽수"]
    #
    # if book["출판사"] in pub_companies:
    #     pass
    # else:
    #     pub_companies.append(book["출판사"])

# 파이썬스러운 코드
many_page = [book["제목"] for book in books if book["쪽수"] >= 250]
recommends = [book["제목"] for book in books if book["추천유무"]]
all_pages = sum([book["쪽수"] for book in books])
pub_companies = {book["출판사"] for book in books}


print("쪽수가 250쪽 넘는 책 리스트: {0}\n" \
      "내가 추천하는 책 리스트: {1}\n" \
      "내가 읽은 책 전체 쪽수: {2}\n" \
      "내가 읽은 책의 출판사 목록: {3}\n".format(many_page, recommends, all_pages, pub_companies))

