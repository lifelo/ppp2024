import csv
import sys
import os
import requests

if "./" not in sys.path:
    sys.path.append("./")
def weather_db(filename, URL):
    if not os.path.exists(filename):
        res = requests.get(URL)
        with open(filename, "w", encoding='UTF-8-sig') as f:
            reader = csv.DictReader(file)
            for line in reader:
                weather_db.append(line)
        return weather_db


def forty_four_year_forecast(filename):
    forecast = []
    with open(filename, encoding='UTF-8-sig') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            date = tokens[0]
            year = int(tokens[1])
            month = int(tokens[2])
            day = int(tokens[3])
            temperature = float(tokens[4])
            snow = float(tokens[5])
            sunshine = float(tokens[6])
            wind = float(tokens[7])
            rainfall = float(tokens[8])
            humid = float(tokens[9])
            cloud = float(tokens[10])
            tavg = float(tokens[11])
            tmin = float(tokens[12])
            tmax = float(tokens[13])
            station_id = tokens[14]

import matplotlib.pyplot as plt
import numpy as np

def main():
    tmax = np.random.rand(30) * 15 + 15
    tmin = tmax - (np.random.rand(30) * 5 + 5)
    plt.plot(tmax, color="r", label="TMAX")
    plt.plot(tmin, color="b", label="TMIN")
    plt.ylabel("Temperature(℃)")
    plt.legend()
# plt.show()
    plt.savefig("./line_temp.png")
    print(f"1980-2023년 44년치 기상자료:")

    plt.rcParams['font.family'] = ['NanumGothic',  'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False
    tmax = np.random.rand(30) * 15 + 15
    tmin = tmax - (np.random.rand(30) * 5 + 5)
    plt.plot(tmax, color="r", label="44년치 기상자료")
    plt.ylabel("기온(℃)")
    plt.legend()
    plt.savefig("./line_temp_hangul.png")


if __name__ == '__main__':
    main()
