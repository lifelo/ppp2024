import random

def lotto_numbers():
    return random.randint(range(1,46), 6)

def main():
    numbers = int(input("횟수를 입력하세요:"))
    lotto = lotto_numbers()

    for i in range(1, numbers+1):
        numbers= lotto_numbers()
        print(f"게임 {i}: {sorted(numbers)}")

if __name__ == "__main__":
    main()
