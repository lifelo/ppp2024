import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)

import random

def choose_word():
    words = ["love", "phone", "cup"]
    return random.choice(words)

def display_word(word, guessed_letters):
    result = []
    for letter in word:
        if letter in guessed_letters:
            result.append(letter)
        else:
            result.append("_")
    return " ".join(result)

def main():
    word = choose_word()
    guessed_letters = set()
    trial = 5

    print("숨겨진 단어를 맞춰보세요!")

    while trial > 0:
        print(display_word(word, guessed_letters), f"(trial={trial})")
        user_input = input("답을 입력하세요:")

        if len(user_input) != 1:
            print("한 글자만 입력하세요:")
            continue

        if user_input in guessed_letters:
            print("이미 시도한 글자입니다.")
            continue

        guessed_letters.add(user_input)

        if user_input not in word:
            trial -= 1
            print("틀렸습니다.")
        else:
            if all(letter in guessed_letters for letter in word):
                print("정답입니다.")
                break
            else:
                print("정답입니다.")

    if trial == 0:
        print("게임 종료. 기회가 모두 소진되었습니다.")
        print("정답은:", word)

if __name__ == "__main__":
    main()