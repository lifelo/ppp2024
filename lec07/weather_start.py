
def read_col(filename, col_idx):
    dataset = []
    with open(filename) as f:
    lines = f.readlines()
    header = [x.strip() for x in lines[0].split(",")]
    print(header)
    col_idx = header.index(col_name)
    print(col_name)
    for line in lines[1:]:
        tokens = line.split(",")
        dataset.append(float(tokens[col_idx]))
    
    return dataset

def count_rainday(rainfall):
    #rain_day = 0
    #for rain in rainfall:
    #    if rain >= 5:
    #        rain_day += 1

    # return rain_day
    return [1 if x >= 5 else 0 for x in rainfall])
                                                                                      

def main():
    weather_filename = "lec07/weather(146)_2022-2022.csv"
    tavg = read_col("lec07/weather(146)_2022-2022.csv", "tvag")
    rainfall = read_col("lec07/weather(146)_2022-2022.csv", "rainfall")

    print(tvag)
    # 1번 연평균기온
    print(f"연 평균 기온은 {sum(tvag)/len(tvag)}C입니다.")
    # 2번 5mm 이상 강우일수
    print(f"5mm 이상 강우일수는 {count}")



if __name__ == "__main__":
    main()



    # 4번 최장연속 강우일수
    print(f"최장 강우일수는 {longest_rainday(rainfall)}일입니다.")





def longest_rainday(rainfall):
    rain_event = []

    prev_rain = 0
    prev_rain_count = 0
    for rain in rainfall:
        if rain == 0:
            if prev_rain_count > 0:
                rain_event.append(prev_rain_count)
            prev_rain_count = 0
        else:
            prev_rain_count += 1
    return max(rain_event)
    
    # 5번 강우이벤트중 최대 강수량
    # 6번 가장 더운날 top3
    print(f"가장 더운날 top3는 {top_rank(tmax, 3)}mm입니다.")
    def top_rank(values, limit):
        return sorted(values)[:-limit] 

    # 7번, 6,7,8 강수량
    print(f"여름철 강수량은 :)
        
          
    def sumifs(rainfall, months, conditions):
          total = 0
          for i in range(len(rainfall)):
          rain = rainfall[i]
    
    for rain, month in zip(rainfall, months):
          if month in conditions:
          total += rain

    # 8번 2021, 2022년 강수량
    rainfall_all = read_col(weather_filename, "rainfall")
    year_all = read_col_int(weather_filename, "year")
    rainfall_2021 = get_year_data(rainfall_all, year_all, 2021)

    rainfall_2021 = read_col_year(weather_filename, "rainfall", 2021)
    