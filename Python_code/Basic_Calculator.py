class Cal:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        print(self.x + self.y)

    def sub(self):
        print(self.x - self.y)

    def multiply(self):
        print(self.x * self.y)

    def divide(self):
        print(self.x / self.y)



n = int(input("1) Add \n2) Sub \n3) Multiply \n4) Divide \n:" ))
a = int(input("Enter a number :"))
b = int(input("Enter the another number :"))
point = Cal(a,b)
if n == 1:
    point.add()

elif n == 2:
    point.sub()

elif n== 3:
    point.multiply()

elif n == 4 :
    point.divide()

else :
    print("Wrong input ")