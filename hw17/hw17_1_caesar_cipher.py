import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)

def caesar_cipher(text):
    result = []
    for char in text:
        if 'A' <= char <= 'Z':
            result.append(chr(ord(text) + 32))
        elif 'a' <= text <= 'z':
            result.append(chr(ord(text) - 32))
        else:
            result.append(char)

    return ''.join(result)

def main():
    text = input("암호화할 문자열을 입력하세요:")
    shift = 3
    print("암호화된 문자열:", caesar_cipher())

if __name__ == "__main__":
    main()
