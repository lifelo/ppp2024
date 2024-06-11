import pandas as pd
from math import pi, sqrt

class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius
    def area(self):
        return pi * self.radius

for shape in Shapes:
    print(shape.area())
    print(shape.perimeter())

def main():
    radius = float(input("반지름을 입력하세요:"))


if __name__ == "__main__":
    main()