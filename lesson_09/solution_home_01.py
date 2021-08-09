class Car:
    def __init__(self, mark, model, year, speed):
        self.mark = mark
        self.model = model
        self.year = year
        self.speed = 0

    def speed_up(self):
        self.speed += 5
        return self.print_speed()

    def speed_down(self):
        self.speed -= 5
        return self.print_speed()

    def stop(self):
        self.speed = 0
        return self.print_speed()

    def print_speed(self):
        print(f'speed now: {self.speed}')

    def reverse_speed(self):
        self.stop()
        self.speed_down()


car = Car('Mercedes', 'GLE', 2018, 0)

car.reverse_speed()
