import csv
import os
import requests

def read_weather_db(filename):
    weather_data = []
    if os.path.exists(filename):
        with open(filename, newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for line in reader:
                weather_data.append(line)
    return weather_data

def find_max_rainfall(weather_data):
    max_rainfall = 0
    max_rainfall_date = ""
    for data in weather_data:
        if float(data['강수량(mm)']) > max_rainfall:
            max_rainfall = float(data['강수량(mm)'])
            max_rainfall_date = data['일시']
    return max_rainfall, max_rainfall_date

def find_max_temperature_difference(weather_data):
    max_difference = 0
    max_difference_date = ""
    for data in weather_data:
        temp_difference = float(data['최고기온(°C)']) - float(data['최저기온(°C)'])
        if temp_difference > max_difference:
            max_difference = temp_difference
            max_difference_date = data['일시']
    return max_difference, max_difference_date

def main():
    filename = 'jeonju_weather_data.csv'
    if not os.path.exists(filename):
        url = 'https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=1904&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize='
        response = requests.get(url)
        with open(filename, 'wb') as file:
            file.write(response.content)

    weather_data = read_weather_db(filename)
    max_rainfall, max_rainfall_date = find_max_rainfall(weather_data)
    max_difference, max_difference_date = find_max_temperature_difference(weather_data)

    print(f"가장 많은 강수량: {max_rainfall} mm, 날짜: {max_rainfall_date}")
    print(f"가장 큰 일교차: {max_difference} °C, 날짜: {max_difference_date}")

if __name__ == "__main__":
    main()
