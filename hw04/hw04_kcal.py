import math
apple = int(input("사과의 섭취량을 입력하세요(g):"))
apple_kcal = (apple / 100) * 57
print(apple_kcal)
banana = int(input("바나나의 섭취량을 입력하세요(g):"))
banana_kcal = (banana / 100) * 77
print(banana_kcal)
kcal = [57,77]
total_kcal = kcal[0] * apple + kcal[1] * banana