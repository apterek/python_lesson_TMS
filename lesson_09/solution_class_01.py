class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = 'cat'
        self.age = age

    def jump(self):
        print(self.height - self.weight - self.age * 2)

    def run(self):
        print(self.weight - self.age)

    def bark(self):
        print(self.weight - self.age + self.height)


if __name__ == "__main__":
    dog = Dog(height=100, weight=12, name='Takao', age=2)
    dog.jump()
    dog.run()
    dog.bark()
