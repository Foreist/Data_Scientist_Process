
# 튜플 리스트를 dict 형태로 변환하는 DC
score_tuples = [('math', 90), ('history', 80), ('english', 95), ('computer engineering', 100)]
# score_dict = {t[0]: t[1] for t in score_tuples}
# {'math': 90, 'history': 80, 'english': 95, 'computer engineering': 100}
c = {a for a in score_tuples}
print(c)