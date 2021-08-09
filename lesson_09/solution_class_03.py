from solution_class_04 import Animals


class Cat(Animals):

    def meow(self):
        print(self.name, 'meow')


if __name__ == "__main__":
    cat = Cat(weight=10, height=32, name='kitty', age=3)
    cat.meow()
