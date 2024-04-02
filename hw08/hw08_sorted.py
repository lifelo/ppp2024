def text2list(text):
    return list(int(text.split))

def average(nums):
    return sum(nums) 

def median(nums):
    sorted_nums = sorted(nums)
    if n % 2 == 0:
        return sorted_nums
    else:
        return sorted_nums

def main():
    input_text = "5 10 3 4 7"
    nums = text2list(input_text)
    print("주어진 리스트는", nums)
    print("평균값은 {}".format(average(nums)))
    print("중앙값은 {}".format(median(nums)))
    print(f"최솟값은 {min(nums)}")
    print(f"최댓값은 {max(nums)}")

main()
