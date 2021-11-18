#point.py

#p1 = (3,5)
# p1 =[3,5]
# p1 = {'x':3,'y':5}

class Point:
    def __init__(self, x=0,y=0):
        self.x =x
        self.y =y
    def __str__(self):
        return f"({self.x},{self.y})"
    def left(self,offset):
        self.x -= offset
        if self.x <0:
            self.x = 0
    def right(self,offset):
        self.x += offset
        if self.x>100:
            self.x = 100


p1 = Point(); p2=Point(10,10)
print(p1); print(p2)
p2.left(20)
p2.right(5)
print(p2)