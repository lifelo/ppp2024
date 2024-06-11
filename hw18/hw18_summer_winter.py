import csv
import sys
import os
import requests
import termcolor

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


def summer_forecast(filename):
    forecast = []
    with open(filename, encoding='UTF-8-sig') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            month = int(tokens[0])
            temperature = float(tokens[1])

def winter_forecast(filename):
    forecast = []
    with open(filename, encoding='UTF-8-sig') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            month = int(tokens[0])
            temperature = float(tokens[1])

import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.ylabel("Temperature(℃)")
    plt.legend()
# plt.show()
    plt.savefig("./line_temp.png")
    print(f"겨울철,여름철 온도분포:")

    plt.rcParams['font.family'] = ['NanumGothic',  'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(color="b", label="겨울철,여름철 온도분포")
    plt.ylabel("기온(℃)")
    plt.legend()
    plt.savefig("./line_temp_hangul.png")

if __name__ == '__main__':
    main()