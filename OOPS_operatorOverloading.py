class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    def sum(self,p):
        return Point((self.x + p.x),(self.y + p.y))
    
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}") 
    
p1 = Point(3,7)
p2 = Point(2,9)

p = p1.sum(p2)
p.print_point()