import pandas as pd
from math import pi, sqrt

class Rectangle(Shape):
    def __init__(self, height, width):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)
    def area(self):
        return self.width * self.height

for shape in Shapes:
    print(shape.area())
    print(shape.perimeter())

def main():
    width = float(input("밑변을 입력하세요:"))
    height = float(input("높이를 입력하세요:"))

if __name__ == "__main__":
    main()