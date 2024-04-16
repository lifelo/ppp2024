import pandas as pd

data_2022 = pd.read_csv('weather_data_2022.csv')

data_2001_2022 = pd.read_csv('https://github.com/taegon/JBNU_PPP_2024/raw/main/hw11/weather(146)_2001-2022.csv')

data_2022['Date'] = pd.to_datetime(data_2022['Date'])
data_2001_2022['Date'] = pd.to_datetime(data_2001_2022['Date'])

print(data_2022.head())
print(data_2001_2022.head())

max_rain_event = data_2022[data_2022['Rainy']].groupby('Rain_Group')['Rainfall'].sum().max()

print(f"Maximum rainfall during a single rain event in 2022: {max_rain_event}")
