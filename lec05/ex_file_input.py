def text2list(text):
    return list(int(text.split))

def average(nums):
    return sum(nums) 

def median(nums):
    sorted_nums = sorted(nums)
    return sorted_nums[lens(nums)//2]

def read_file_multi_line(filename):
    data = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
        text = line.strip()
        value = int(text)
        data.append(value)
        print(f"!{text}!")
    return " ".join(data)


def main():
    # input_text = "5 10 3 4 7"
    # input_text = read_file("lec05/number2.txt")
    # nums = text2list(input_list)
    read_file_multi_line(filename):

    nums = text2list(input_text)
    
    print("주어진 리스트는", nums)
    print("평균값은 {}".format(average(nums)))
    print("중앙값은 {}".format(median(nums)))
    print(f"최솟값은 {min(nums)}")
    print(f"최댓값은 {max(nums)}")
    



