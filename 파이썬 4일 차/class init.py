# 아래와 같은 방식으로 하면 객체를 생성하고 name을 호출해서 또 추가적으로 변수 안에 값을 집어넣어줭야 함

# class MyClass:
#     name = str()
#
#     def sayHello(self):
#         hello = "Hello, " + self.name + "\t It's Good day !"
#         print(hello)
#
# # 객체 생성, 인스턴스화
# myClass = MyClass()
# myClass.name = '준영'
# myClass.sayHello()

# 클래스 초기화 함수, __init__() 재정의
class MyClass:
    def __init__(self, name):     # 초기화 함수 재정의
        self.name = name

    def sayHello(self):
        hello = "Hello, " + self.name + "\t It's Good day !"
        print(hello)

# 객체 생성, 인스턴스화
# myClass = MyClass()
myClass = MyClass('채영')
myClass.sayHello()