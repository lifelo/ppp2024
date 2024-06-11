import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)

import random
def chosung_game(text):
    for gulja in text:
        print(gulja, (ord(gulja) - ord('가')) // 588, (ord(gulja) - ord('가')) % 588)
    return random.choice(text)

def main():
    hidden_answer = "아이스티샷추가"
    problem = get_chosung_game(hidden_answer)
    print(f"문제입니다. 주어진 초성은 '{problem}'입니다.")

    answer = input("답은=>?")
    if answer == hidden_answer:
        print("정답입니다.")

    else:
        print("틀렸습니다.")


if __name__ == "__main__":
    main()