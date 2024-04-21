def main():
    filename = "lec07/weather(146)_2001-2022.csv"
    tmax = read_col(filename, "tmax")
    tmin = read_col(filename, "tmin")
    # years = read_col_int(filename, "year")
    # months = read_col_int(filename, "months")
    # days = read_col_int(filename, "days")
    for line in file:
            data = line.strip().split(',')
            max_temp = float(data[1])
            min_temp = float(data[2])
            weather_data[date] = (max_temp, min_temp)
    return weather_data

print(f"가장 큰 최대일교차: {max_temp_range}℃")
    print(f"해당 날짜: {max_temp_range_date}")

if __name__ == "__main__":
    main()