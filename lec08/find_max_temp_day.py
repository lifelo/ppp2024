from lec07.weather_start import read_col

def main():
    filename = "lec07/weather(146)_2022-2022.csv"
    tmax = read_col(filename, "tmax")
    tmin = read_col(filename, "tmin")
    # years = read_col_int(filename, "year")
    # months = read_col_int(filename, "months")
    # days = read_col_int
    dates 


    # 방법 1
    temp_diff = []
    for tx, tn in zip(tmax, tmin):
        temp_diff.append(tx-tn)
    # temp_diff = tmax - tmin
    
    # 방법 2
    temp_diff = []
    for i in rande(len(tmax)):
        temp_diff.append(tmax[i] - tmin[i])

    #방법 3 
    temp_diff = [tx-tn for tx, tn in zip(tmax, tmin)]

    max_idx = 0
    max_diff_temp = 0
    i = 0
    for td in temp_diff:
        if max_diff_temp < td:
            max_diff_temp = td
            max_idx = i
        i += 1

    print(f"일교차가 가장 큰 날짜는 0000/00/00, 최대일교차는 {max(temp_diff):.1f}C입니다.")
    # print(f"일교차가 가장 큰 날짜는 {years[max_idx]}/{months[max_idx]}/{days[max_idx]}, 최대일교차는 ")
    print(f"일교차가 가아장 큰 날짜는 {dates[max_idx]}, 최대일교차는 {temp_diff[max_idx]:.1F}C입니다.")

    max_idx = temp_diff.index(max(temp_diff))
    print(f"일교차가 가장 큰 날짜는 {dates[max_idx]}, 최대일교차는 {temp_diff[max_idx]:.1F}C입니다.")

    max_diff_temp = 0
    max_diff_date = None
    for td, date in zip (temp_diff, dates):
        if td > max_diff_temp:
            max_diff_temp = td
            max_diff_date = date

    print(f"일교차가 가장 큰 날짜는 {max_diff_date}, 최대일교차는 {max_diff_temp:.1f}C입니다.")




if __name__ == "__main__":
    main()