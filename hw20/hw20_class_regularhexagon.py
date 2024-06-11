import pandas as pd
from math import pi, sqrt

class RegularHexagon(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def perimeter(self):
        return 2 * pi * self.side_length
    def area(self):
        return pi * self.side_length

for shape in Shapes:
    print(shape.area())
    print(shape.perimeter())

def main():
    side_length = float(input("길이를 입력하세요:"))


if __name__ == "__main__":
    main()