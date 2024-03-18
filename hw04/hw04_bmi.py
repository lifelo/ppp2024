import math
height = int(input("키를 입력하세요(cm):"))
weight = int(input("몸무게를 입력하세요(kg):"))
bmi =math.sqrt(weight / (height ** 2))
print()
if 23 <= bmi <= 24.9 :
    print("비만 전단계입니다.")
elif 25 <= bmi <= 29.9 :
    print("1단계 비만입니다.")
elif 30 <= bmi <= 34.9 :
    print("2단계 비만입니다.")
elif 35 <= bmi :
    print("3단계 비만입니다.")
else:
    print("정상입니다.")



