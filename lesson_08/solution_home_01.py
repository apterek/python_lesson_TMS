def distance(full_distance, first_run):
    day = 0
    while True:
        day += 1
        full_distance -= first_run
        first_run_2 = first_run * 1.1
        first_run += first_run_2
        print(first_run)
        if full_distance <= 0:
            return print(day)


def main():
    full_dist = float(input('Enter full distance: '))
    distance_first_day = float(input('Enter distance first day: '))
    distance(full_dist, distance_first_day)


if __name__ == '__main__':
    main()
