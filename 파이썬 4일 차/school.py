# 클래스 변수와 인스턴스 변수

class MyChildren:

    def __init__(self, name, school):     # 초기화 함수 재정의
        self.name   = name        # 인스턴스 변수 name 선언
        self.school = school

    def go_to_school(self):
        print(self.name + '이는 ' + self.school + '에 다닙니다.')


q = MyChildren("이름", "학교")

q.go_to_school()

