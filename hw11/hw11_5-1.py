import pandas as pd

data_2022 = pd.read_csv('weather_data_2022.csv')

data_2001_2022 = pd.read_csv('https://github.com/taegon/JBNU_PPP_2024/raw/main/hw11/weather(146)_2001-2022.csv')

data_2022['Date'] = pd.to_datetime(data_2022['Date'])
data_2001_2022['Date'] = pd.to_datetime(data_2001_2022['Date'])

print(data_2022.head())
print(data_2001_2022.head())

summer_rainfall = data_2022[(data_2022['Date'].dt.month.isin([6, 7, 8]))]['Rainfall'].sum()

print(f"Total rainfall during summer 2022: {summer_rainfall}")
