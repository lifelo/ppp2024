def sum_n():
    n = int(input('n값을 입력하세요.: '))
    sum = 0
    for i in range(1, n+1):
        sum += i # sum에 i를 더함
        print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

sum_n()