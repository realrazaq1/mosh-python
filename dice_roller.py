import random


# wen u want to return a tuple from a function, you dont have to add ()
# PEP: python enhancement proposal. best practices for formatting our code
# static methods don't take self 
class Dice:
    @staticmethod
    def roll():
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


print(Dice.roll())
