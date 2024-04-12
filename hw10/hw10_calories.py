import pandas as pd

calorie_data = pd.read_csv("https://github.com/taegon/JBNU_PPP_2024/raw/main/hw10/calorie_db.csv")

print("칼로리 데이터:\n", calorie_data.head())

def calculate_calories(food, amount):
    try:
        calorie = calorie_data.loc[calorie_data['Food'] == food, 'Calorie'].values[0]
        total_calories = calorie * amount
        return total_calories
    except IndexError:
        return "식품을 찾을 수 없습니다."
        
food_name = "Apple"
food_amount = 2  # Apple 2개의 칼로리를 계산
calories = calculate_calories(food_name, food_amount)
print(f"\n{food_amount}개의 {food_name}의 총 칼로리:", calories)
