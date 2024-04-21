def main():
    filename = "lec07/weather(146)_2001-2022.csv"
    t_temp = read_col(filename, "t_temp")
    # years = read_col_int(filename, "year")
    # months = read_col_int(filename, "months")
    # days = read_col_int(filename, "days")
    for line in file:
            data = line.strip().split(',')
          
            weather_data[date] = (t_temp)
    return weather_data



if __name__ == "__main__":
    main()