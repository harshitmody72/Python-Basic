import random
class Dice:
    def roll(self):
        a= random.randint(1,6)
        b= random.randint(1,6)
        return a,b   #it will return a tupple by default in python


piont = Dice()
print(piont.roll())