from solution_home_01 import Car


def main():
    new_car = Car('Mercedes', 'E500', 2000, 0)
    if new_car.speed < 100:
        while new_car.speed < 100:
            new_car.speed_up()
    elif new_car.speed > 100:
        while new_car.speed > 100:
            new_car.speed_down()
    return print(f'the car accelerated to {new_car.speed} km per hour')


if __name__ == "__main__":
    main()
