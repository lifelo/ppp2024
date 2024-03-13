# temp_c = 30

# temp_c = input("온도를 입력하세요")
# temp_c = int(temp_c)

temp_c = int(input("온도를 입력하세요"))
temp_f = temp_c * 1.8 + 32
print("{}C => {}F".format(temp_c, temp_f))
print(temp_f)

# height = 1.70
# weight = 60

# bmi = input("bmi를 입력하세요")
# bmi = int(bmi)

bmi = int(input("bmi를 입력하세요"))
bmi = weight / (height ** 2)
print("키가 {}cm, 몸무게가 {}kg이면, bmi는 {}입니다.".format(height, weight, bmi))
print(bmi)
