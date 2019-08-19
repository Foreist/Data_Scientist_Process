# 지역변수와 전역변수
param   = 10
strdata = '전역변수'

# 변수 안에서 생성했으므로 바깥의 strdata와 다른 주소값을 가짐
def func1():
    strdata = '지역변수'
    print('func1.strdata = %s, id = %d' % (strdata, id(strdata)))

# 변수 안에서 생성했으므로 바깥의 strdata와 다른 주소값을 가짐
def func2(param):
    param = 20
    print('func2.param = %d, id = %d' % (param, id(param)))

# 바깥의 param을 불러왔기 때문에 param의 값이 30으로 변경됨
def func3():
    global param
    param = 30
    print('func3.param = %d, id = %d' % (param, id(param)))

func1()
# 위 값과 다르게 나옴
print('main1.strdata = %s, id = %d' % (strdata, id(strdata)))
# func1.strdata = 지역변수, id = 2249228591776
# main1.strdata = 전역변수, id = 2249228591880

func2(param)

#위 값과 다르게 나옴
print('main2.param = %d, id = %d' % (param, id(param)))
# func2.param = 20, id = 140719810983344
# main2.param = 10, id = 140719810983024
func3()

#위 값과 같음
print('main3.param = %d, id = %d' % (param, id(param)))
# func3.param = 30, id = 140719810983664
# main3.param = 30, id = 140719810983664
