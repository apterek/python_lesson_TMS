class Point:
    def __init__(self, point_x, point_y):
        self.point_x = point_x
        self.point_y = point_y
        self.point = (point_x, point_y)


class Figure:
    pass


class Circle(Point):

    def radius_circle(self):
        pass

    def perimeter_of_the_circle(self):
        pass

    def area_of_the_circle(self):
        return self.point_x(self.point_x) - self.point_y(self.point_y)


point_1 = Circle(1, 3)
point_2 = Circle(3, 6)

area = Circle(point_1, point_2)
print(area.area_of_the_circle())
