# 숫자를 입력받고 리스트를 출력
def numbers_list_generater():
    numbers_list = []
    while True:
        number = int(input("숫자를 입력하세요(-1 입력 시 종료):"))
        if number == -1:
            break
        numbers_list.append(number)
    return numbers_list


def count_numbers(numbers_list):
    return len(numbers_list)

def average_numbers(numbers_list):
    average = sum(numbers_list) / len(numbers_list)
    return average

def main():
    numbers_list = numbers_list_generater()
    print("입력한 숫자들:", numbers_list)
    print("숫자들의 개수:", count_numbers(numbers_list))
    print("숫자들의 평균:", average_numbers(numbers_list))

if __name__ == "__main__":
    main()