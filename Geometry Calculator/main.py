
class rec:
    def __init__(self, length, height, perimeter, area):
        self.length = length
        self.height = height
        self.perimeter = perimeter
        self.area = area
    def perimeter_get(self):
        self.perimeter = (self.length + self.height) * 2
    def area_get(self):
        self.area = self.length * self.height

class tri:
    def __init__(self, height, side_one, side_two, side_three, perimeter, area):
        self.height = height
        self.side_one = side_one
        self.side_two = side_two
        self.side_three = side_three
        self.perimeter = perimeter
        self.area = area
    def perimeter_get(self):
        self.perimeter = self.side_one + self.side_two + self.side_three
    def area_get(self):
        self.area = (self.side_one * self.height) / 2

class cir:
    def __init__(self, radius, perimeter, area):
        self.radius = radius
        self.perimeter = perimeter
        self.area = area
    def perimeter_get(self):
        self.perimeter = (2 * self.radius) * 3.14159
    def area_get(self):
        self.area = (self.radius * self.radius) * 3.14159