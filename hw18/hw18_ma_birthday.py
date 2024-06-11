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


def ma_birthday(filename):
    forecast = []
    birth_year = 2004
    birth_month = 5
    birth_day = 11
    with open(filename, encoding='UTF-8-sig') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            year = int(tokens[0])
            temperature = float(tokens[1])

import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.ylabel("Temperature(℃)")
    plt.legend()
# plt.show()
    plt.savefig("./line_temp.png")
    print(f"내 생일날 기온, 몇살 생일때가 춥고 더웠나:")
    print(termcolor.colored('Hello,World!', 'red', attrs=['reverse','blink']))

    plt.rcParams['font.family'] = ['NanumGothic',  'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False
    plt.ylabel("기온(℃)")
    plt.legend()
    plt.savefig("./line_temp_hangul.png")


if __name__ == '__main__':
    main()