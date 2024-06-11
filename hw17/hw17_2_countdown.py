import time

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time = f'{mins:00}:{secs:00}'
        print(f'\r{time}', end='', flush=True)
        time.sleep(1)
        seconds -= 1
    print("\r00:00", end='', flush=True)

def main():
    seconds = int(input("시간을 입력하세요:"))
    countdown(seconds)


if __name__ == "__main__":
    main()
