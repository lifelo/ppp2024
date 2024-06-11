import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)

import random
#구구단 문제를 제출
def question():
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    answer = number1 * number2
    return number1, number2, answer

#정답 개수 체크
def answer_check(number1, number2, answer):
    answer = number1 * number2
    return user_answer == correct_answer

#점수 출력
def main():
    number_questions = int(input("숫자를 입력하세요:"))
    correct_answer = 0

    for i in range(number_questions):
        number1, number2, answer = question()
        user_answer = int(input(f"{number1} * {number2} = "))

        if answer_check(number1, number2, answer):
            correct_answer += 1
            print("정답입니다")
        else:
            print("오답입니다")

    score = (correct_answer / number_questions) * 100
    print(f"점수: {score:.2f}")

if __name__ == "__main__":
    main()