from solution_home_01 import Point, Circle, Square, Triangle


def main():
    triangle = Triangle(Point(2, 2).point_axis, Point(1, 5).point_axis, Point(3, 4).point_axis)

    square = Square(Point(2, 2).point_axis, Point(2, 4).point_axis)

    circle = Circle(Point(3, 3).point_axis, Point(1, 3).point_axis)
    for figure in [triangle, circle, square]:
        print(figure.area())


if __name__ == '__main__':
    main()


