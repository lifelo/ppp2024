def largest(a, b, c):
    largest_num = a

    if a > b:
       if a > c:
           return a
       else:
           return c
    else: # a <= b
        if b > c:
            return b
        else:
            return c
    return largest_num

def main():
    x1 = 5
    x2 = 7
    x3 = 3

    largest_num = largest(x1,x2,x3)

    print(f"가장 큰수는 {largest_num}입니다.")

if __name__ == "__name__":
    main()




def largest(nums):
    largest_nums = nums[0]
    for num in nums:
        if largest_num < num:
            largest_num = num
        return largest_num

def main():
    x = [3,7,5,6,3]

    print(f"최대값은 {largest(x)입니다.")

if __name__ == "__main__":
    main()



def minmax(nums):
    max_num = max(nums)
    min_num = min(nums)
    return min_num, max_num

def main():
    nums = [3,5,7,4,10,2]
    mn,mx = minmax(nums)

    print(f"최솟값은 {mn}, 최댓값은 {mn}")

if __name__ == "__main__":
    main()
