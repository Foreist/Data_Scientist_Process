class MyClass:
    name = '희영'

# 클래스 내 자체적으로 생성한 지역 변수를 사용하려면 self를 아래와 같이 사용해야 한다.
    def sayHello(self):
        hello = "Hello, " + self.name + "\t It's Good day !"
        return hello

# 클래스를 생성할 떄는 괄호가 필요 없지만 호출할 때는 클래스 명 뒤에 괄호를 붙여준다.
myClass = MyClass()
# 클래스 내 지역변수를 호출할 때는 그냥 클래스명.지역변수 하고 적어준다.
obj_name = myClass.name
# 함수를 호출할 때는 원래 호출하는 것처럼 호출을 해준다.
obj_method = myClass.sayHello()

print('Object name   :', obj_name)
print('Object method :', obj_method)