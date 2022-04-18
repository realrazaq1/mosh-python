# we use classes to define new types
# class is a blueprint for an object
# an object is an instance of a class
# object are the actual instances based on that blueprint
# we can also add attributes to objects, which are like variables.
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y =20
print(point1.x)
point1.move()

point2 = Point()
point2.x = 1
print(point2.x)
