from solution_class_01 import Dog
from solution_class_03 import Cat


class Animals(Cat, Dog):
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = 'cat'
        self.age = age

    def jump(self):
        print(self.height - self.weight - self.age * 2)

    def run(self):
        print(self.weight - self.age)