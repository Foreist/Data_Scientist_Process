weight = float(input("체중(kg)은 ? "))
height = float(input("키(cm)는 ? "))

# BMI 계산
height = height / 100
bmi = weight / (height * height)

if bmi < 18.5:
    result = "마름"

elif bmi < 25:
    result = "보통"
elif bmi < 30:
    result = "가벼운 비만"
else:
    result = "심한 비만"

print("BMI: ", bmi)
print("판정: ", result)