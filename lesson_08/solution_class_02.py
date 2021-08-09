import time
from solution_class_01 import filter_car_by_year


# find work time function filter_car_by_year
def my_decorator_2(func):
    def time_counter(listing):
        start_time = time.time()  # time start function
        result = func(listing)  # start function
        return result, time.time() - start_time - 2  # time implementations
    return time_counter


# create function with decorator
my_func = my_decorator_2(filter_car_by_year)
#print(my_func(car_list))
