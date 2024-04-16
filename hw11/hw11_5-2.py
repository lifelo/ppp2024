import pandas as pd

data_2022 = pd.read_csv('weather_data_2022.csv')

data_2001_2022 = pd.read_csv('https://github.com/taegon/JBNU_PPP_2024/raw/main/hw11/weather(146)_2001-2022.csv')

data_2022['Date'] = pd.to_datetime(data_2022['Date'])
data_2001_2022['Date'] = pd.to_datetime(data_2001_2022['Date'])

print(data_2022.head())
print(data_2001_2022.head())

total_rainfall_2021_2022 = data_2001_2022[data_2001_2022['Date'].dt.year.isin([2021, 2022])]['Rainfall'].sum()

print(f"Total rainfall in 2021 and 2022: {total_rainfall_2021_2022}")




