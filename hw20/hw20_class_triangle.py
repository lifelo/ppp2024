import pandas as pd
from math import pi, sqrt

class triangle(Shape):
    def __init__(self, height, base):
        self.base = base
        self.height = height

    def perimeter(self):
        return 2 * self.base + 2 * self.height
    def area(self):
        return 0.5 * self.base * self.height

for shape in Shapes:
    print(shape.area())
    print(shape.perimeter())

def main():
    width = float(input("밑변을 입력하세요:"))
    height = float(input("높이를 입력하세요:"))

if __name__ == "__main__":
    main()