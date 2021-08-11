import math
from math import pi


class Point:
    def __init__(self, axis_x, axis_y):
        self.axis_x = axis_x
        self.axis_y = axis_y
        self.point_axis = [self.axis_x, self.axis_y]


class Figure:

    def __init__(self):
        self.second_point = None
        self.first_point = None

    def line_length(self):
        return math.sqrt(pow(self.first_point[0] - self.second_point[0], 2) +
                         pow(self.first_point[1] - self.second_point[1], 2))


class Circle(Figure):
    def __init__(self, first_point, second_point):
        super().__init__()
        self.second_point = second_point
        self.first_point = first_point
        self.radius = self.line_length()

    def area(self):
        return pi * pow(self.radius, 2)

    def perimeter(self):
        return pi * 2 * self.radius


class Triangle(Figure):
    def __init__(self, point_A, point_B, point_C):
        super().__init__()
        self.point_C = point_C
        self.point_B = point_B
        self.point_A = point_A
        self.side_a = math.sqrt(pow(self.point_A[0] - self.point_B[0], 2) +
                                pow(self.point_A[1] - self.point_B[1], 2))
        self.side_b = math.sqrt(pow(self.point_B[0] - self.point_C[0], 2) +
                                pow(self.point_B[1] - self.point_C[1], 2))
        self.side_c = math.sqrt(pow(self.point_C[0] - self.point_A[0], 2) +
                                pow(self.point_C[1] - self.point_A[1], 2))

    def area(self):
        half_per = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(half_per * (half_per - self.side_a) * (half_per - self.side_b) * (half_per - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


class Square(Figure):

    def __init__(self, first_point, second_point):
        super().__init__()
        self.second_point = second_point
        self.first_point = first_point
        self.side = self.line_length()

    def area(self):
        return pow(self.side, 2)

    def perimeter(self):
        return self.side * 4

