from solution_class_04 import Animals


class Dogs(Animals):
    def bark(self):
        print(self.weight - self.age + self.height)


if __name__ == "__main__":
    far = Dogs(height=100, weight=20, name='GAlo', age=5)
    far.change_name('Timea')
