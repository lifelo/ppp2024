import requests

url = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"

filename = "hw13/weather_146_2020.csv"

if path.exists(filename):
    with open(filename, "w") as f:
        res = request.get(url)
        f.write(res.text)

with open(filename, "w") as f:
    res = request.get(url)
    f.write(res.text)