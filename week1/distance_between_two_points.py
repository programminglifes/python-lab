# Distance between two points

class Point:
    def __init__(self, x, y):
        self.x: int
        self.y: int

def distance(p1: Point, p2: Point):
    return ( (p1.x-p2.x) ** 2 + (p1.y-p2.y) ** 2 ) ** .5

print("Enter any point coordinates")
p1 = Point(0,0)
p1.x = int(input("x1: "))
p1.y = int(input("y1: "))

print("Enter the second point")
p2 = Point(0,0)
p2.x = int(input("x2: "))
p2.y = int(input("y2: "))

print("The distance between the two points is: ", distance(p1, p2))

