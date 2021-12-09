from point import Point
import math

# struct Rectangle
# {
    # struct Point p1;
    # struct Point p2;
# }

class Rectangle:
    def __init__(self, p1,p2):
        self.P1=p1
        self.P2=p2
    
    def height(self):
        return abs(self.P1.X - self.P2.X)
    
    def width(self):
        return abs(self.P1.Y - self.P2.Y)
            
    def borderlength(self):
        return (self.height() + self.width())*2
    
    def area(self):
        return self.height() * self.width()
    
    def diagonal(self):
        return math.sqrt(self.height() ** 2 + self.width() **2)
    
    