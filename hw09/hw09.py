def main():
    file_name = input("파일 이름을 입력하세요: ")

        with open(file_name, 'r') as file:
            numbers = []
            for line in file:
                line_numbers = line.strip().split()
                numbers.extend(map(int, line_numbers))

            if numbers:
                total_count = len(numbers)
                average = sum(numbers) / total_count
                maximum = max(numbers)
                minimum = min(numbers)
                sorted_numbers = sorted(numbers)
                if total_count % 2 == 0:
                    median = (sorted_numbers[median_index - 1] + sorted_numbers[median_index]) / 2
                print("총 숫자의 개수:", total_count)
                print("주어진 숫자의 평균:", average)
                print("주어진 숫자의 최댓값:", maximum)
                print("주어진 숫자의 최솟값:", minimum)
                print("중앙값:", median)
            else:
                print("파일에 숫자가 없습니다.")
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

if __name__ == "__main__":
    main()
