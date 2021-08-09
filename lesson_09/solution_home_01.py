class Car:
    def __init__(self, mark, model, year, speed=0):
        self.mark = mark
        self.model = model
        self.year = year
        self.speed = 0

    def speed_up(self):
        self.speed += 5

    def speed_down(self):
        self.speed -= 5

    def stop(self):
        self.speed = 0

    def print_speed(self):
        print(f'speed now: {self.speed}')

    def reverse_speed(self):
        self.stop()
        self.speed_down()


def main():
    car = Car('Mercedes', 'GLE', 2018, 0)
    car.reverse_speed()


if __name__ == "__main__":
    main()
