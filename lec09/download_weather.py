import requests

url = "https://flight.naver.com/flights/international/ICN-BKI-20240718/BKI-ICN-20240722?adult=1&fareType=Y"

filename = "lec09/weather_146_2022.csv"

if os.path.exists(filename):
    with open(filename, "w") as f:
        res = request.get(url)
        f.write(res.text)

with open(filename, "w") as f:
    res = request.get(url)
    f.write(res.text)