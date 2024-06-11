import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)

def toggle_text():
    result = []
        if 'A' <= text <= 'Z':
            result.append(chr(ord(text) + 32))
        elif 'a' <= text <= 'z':
            result.append(chr(ord(text) - 32))
    return ''.join(result)

def main():
    text = input("문자열을 입력하세요:")
    print("변환된 문자열:", toggle_text)


if __name__ == "__main__":
    main()
