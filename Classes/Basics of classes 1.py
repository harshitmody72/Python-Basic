class new:
    def move(self):
        print("new")
        return 0



point = new()
point.move()
print(type(point))
print(point.move())
point.x= 10
print(point.x)
point2 = new()
point2.ty = "draw"
point2.x2= [3,4,3]
point2.x3 = dict()
print(point2.ty)
print(point2.x2)
print(point2.x3)
print(point.x2)
print ("last")
