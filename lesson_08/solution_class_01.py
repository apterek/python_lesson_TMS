import time


# list of cars
car_list = [
    {
        'mercedes': ['512412', 'red', '2014']
    },
    {
        'opel': ['23ra2412', 'blue', '2012']
    },
    {
        'ford': ['5124215df22', 'yellow', '2019']
    }
]


# find car younger 2013
def filter_car_by_year(car_dicts):
    new_list = []
    time.sleep(2)  # crutch
    for dict_car in car_dicts:
        for key, value in dict_car.items():  # take mark car and his information
            if int(value[2]) > 2013:  # find cars younger 2013
                new_list.append(key)  # add cars younger 2013
    return new_list  # return result


#print(filter_car_by_year(car_list))
