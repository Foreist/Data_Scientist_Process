# \을 쓰면 줄이 길어도 줄이 연결 가능
solarsys = ['태양', '수성', '금성', '지구', '화성', \
           '목성', '토성', '천왕성', '해왕성', '지구']

# 지구는 몇 번째 행성에 있는가?
print(solarsys.index('지구'))

# 화성을 영어로 바꾸기
solarsys[solarsys.index('화성')] = 'mars'
solarsys

# mars 앞에 mars1 입력
solarsys.insert(solarsys.index('mars'), 'mars1')
solarsys

# 지구의 위치를 알려면?
print(solarsys.index('지구'))