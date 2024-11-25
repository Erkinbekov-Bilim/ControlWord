
# 1
class Person:
    def __init__(self, age = 0):
        self._age = age

    def set_age(self, new_age):
        if new_age > 0:
            self._age = new_age
            return self._age
        else:
            print("Возраст не может быть ниже нуля")

    def get_age(self):
        return self._age



p = Person()

p.set_age(25)
p.set_age(-12)
print(p.get_age())



# 2

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am an animal")


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"



dog = Dog("Buddy")
dog.speak()

cat = Cat("Kitty")
cat.speak()

print(dog.name, dog.speak())
print(cat.name, cat.speak())


# 3
class Vehicle:
    def move(self):
        return "Vehicle is moving"


class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bycycle(Vehicle):
    def move(self):
        return "Bycycle is pedaling"


def move(vehicle):
    return vehicle.move()

car = Car()
bike = Bycycle()

print(move(car))
print(move(bike))


# 4
from abc import ABC, abstractmethod
from math import pi
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)


rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())
print(circle.area())