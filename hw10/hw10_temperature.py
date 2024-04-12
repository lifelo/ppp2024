import pandas as pd

weather_data = pd.read_csv("https://github.com/taegon/JBNU_PPP_2024/raw/main/hw10/weather(146)_2022-2022.csv")

print("\n기상자료 데이터:\n", weather_data.head())

annual_mean_temperature = weather_data['Temperature'].mean()

rainy_days_over_5mm = weather_data[weather_data['Precipitation'] >= 5]['Date'].count()

total_rainfall = weather_data['Precipitation'].sum()

print("\n연 평균 기온(°C):", round(annual_mean_temperature, 2))
print("5mm 이상 강우일수:", rainy_days_over_5mm)
print("총 강우량(mm):", total_rainfall)

