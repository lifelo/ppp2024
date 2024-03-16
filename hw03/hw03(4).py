lower = int(input("밑변을 입력하세요:"))
upper = int(input("윗변을 입력하세요:"))
height = int(input("높이를 입력하세요:"))
trapezoid_area = (lower + upper) / 2 * height
print("밑변이 {}이고, 윗변이 {}이고, 높이가 {}이면 trapezoid_area는 {}입니다".format(lower,upper,height,trapezoid_area))
print(trapezoid_area)

