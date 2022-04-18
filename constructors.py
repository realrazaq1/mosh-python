# constructor: a function that gets called at the time of creating an object
# the constructor in python is def __init__(self)
# self refers to the current object
# each object is a different instance of the Person class

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)


# Exercise
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I'm {self.name}")


person1 = Person("Razaq")
person1.talk()
person2 = Person("Zainab")
person2.talk()
