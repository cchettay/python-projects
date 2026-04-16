class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")

# child class


class Dog(Animal):
    def bark(self):
        print(self.name, "says whoof")


class Cat(Animal):
    def cry(self):
        print(self.name, "says meow")


# objects creation
dog = Dog("german")
cat = Cat("Australian")

dog.eat()
dog.bark()

cat.eat()
cat.cry()
