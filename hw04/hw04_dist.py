import math
x = int(input("첫 번째 값을 입력하세요:"))
y = int(input("두 번째 값을 입력하세요:"))
print()
if x > 0 and y > 0 :
    print("제 1사분면입니다.")
elif x > 0 and y < 0 :
    print("제 4사분면입니다.")
elif x < 0 and y > 0 :
    print("제 2사분면입니다.")
elif x < 0 and y < 0 :
    print("제 3사분면입니다.")
else :
    print("원점입니다.")

