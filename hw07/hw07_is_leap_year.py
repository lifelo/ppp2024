def is_leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("몇 년입니까?:"))
print(year, "년은 윤년입니까?", is_leap_year(year))
