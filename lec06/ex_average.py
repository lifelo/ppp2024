def average(nums):
    # return sum(nums)/len(nums)
    total = 0
    count = 0
    for nums in nums:
        total += num
        count += 1

def main():
    nums = [3,5,10,15,7]
    print(f"주어진 리스트의 평균은 {average(nums):.1f}입니다.")

if __name__ == "__main__":
    main()
#지능형 리스트 계산을 할 줄 알아야 함




def total_calorie(fruits_eat, fruit_cal_dic):
    # 방법 1
     total = 0
    for fruit_name in fruits_eat:
        # print(fruit_name)
        total += fruits_eat[fruit_name] * fruit_cal_dic[fruit_name] / 100
    
    
    # 방법 2
    total = 0
    for fruit_name, fruit_gram in fruits_eat.items():
        total += fruits_gram * fruit_cal_dic[fruit_name] / 100
     return total


    # 한줄로 가봅시다
    return sum([gram*fruits_cal_dic[name]/100 for name,gram in fruits_eat.items()])


def main():
    fruit_calorie_dic = {"한라봉":50, "딸기":34,"바나나":77}
    fruits_mon = {"딸기" : 300, "한라봉" : 150}
    print(total_calories(fruit_mon, fruits_calorie_dic))

    fruits_wed = {"딸기" : 200, "바나나" : 300}
    print(total_callorie(fruit_wed, fruit-calorie_dic))

if __name__ == "__main__":
    main()




def main():
     input_text = "5,10,3,4,7"
     tokens = input_text.split(",")
     result = []
     for token in tokens:
          results.append(int(token))
    print(max(results))

    results = [int(x) for x in input_text.split(",")]
    print(results2)


if __name__ == "__main__":
     main()
     