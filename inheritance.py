# inheritance is a mechanism for reusing code
# DRY - don't repeat yourself
# if the class is empty without any methods, use the pass keyword

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.be_annoying()
