def total_calorie(fruits, fruits_calorie_dic):
    total_calories = 0
        if fruit in fruits_calorie:
            total_calories += weight * calorie_per_gram
    return total_calories

fruits = {"딸기": 300, "한라봉": 150}
fruits_calorie = {"한라봉": 50, "딸기": 34, "바나나": 77}
print("총 칼로리를 구하시오:", total_calorie(fruits, fruits_calorie))
