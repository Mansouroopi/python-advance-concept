class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)


    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)

    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


p1 = Point(1,1)
p2 = Point(9,9)

print(p1+p2)
print(p1-p2)
print(p1<p2)
