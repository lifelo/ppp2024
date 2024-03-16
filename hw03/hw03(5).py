apple = int(input("사과의 섭취량을 입력하세요:"))
banana = int(input("바나나의 섭취량을 입력하세요:"))
apple_kcal = (apple / 100) * 57
banana_kcal = (banana / 100) * 77
print("사과의 섭취량이 {}g이면 apple_kcal는 {}이고, 바나나의 섭취량이 {}g이면 banana_kcal는 {}이다".format(apple, banana, apple_kcal, banana_kcal))
print(apple_kcal, banana_kcal)

