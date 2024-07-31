

class Animal:
    age = 0
    def __init__(self, age):
        self.age = age

    def eat(self):
        print("eating")

    def play(self):
        print("playing")

class Dog(Animal):
    max_age = 16
    def __init__(self, age):
        super().__init__(age)

    def e(self):
        print("only dog food")

    def d(self):
        print("barking")

class Cat(Animal):
    max_age = 17
    def __init__(self, age):
        super().__init__(age)

    def e(self):
        print("only cat food")

class Lion(Cat, Dog):
    def __init__(self, age):
        super().__init__(age)

dog = Dog(5)
cat = Cat(5)

print(dog.age)
print(cat.age)
dog.play()
cat.play()
dog.e()
cat.e()
lion = Lion(1)
lion.e()
lion.d()
lion.play()
print("max age of lion is ", lion.max_age)
