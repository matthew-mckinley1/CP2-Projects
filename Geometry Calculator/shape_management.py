#makes sure the input is possible to use
def number_input(message):
    while True:
        try:
            value = float(input(message + '\n'))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")
#makes the class for rectangles
class rect:
    def __init__(self, length, width, perimeter=0, area=0):
        self.length = length
        self.width = width
        self.perimeter = perimeter
        self.area = area

    def __str__(self):
        return f'Rectangle\nLength: {self.length}\nWidth: {self.width}\nPerimeter: {self.perimeter}\nArea: {self.area}'

    def perim_calc(self):
        return round(2 * (self.length + self.width), 4)

    def area_calc(self):
        return round(self.length * self.width, 4)
#makes subclass forsquare
class square(rect):
    def __init__(self, length):
        super().__init__(length, length)

    def __str__(self):
        return f'Square\nSide: {self.length}\nPerimeter: {self.perim_calc()}\nArea: {self.area_calc()}'

    def perim_calc(self):
        return round(4 * self.length, 4)

    def area_calc(self):
        return round(self.length * self.length, 4)
#makes class for traingangagnagnalge
class tri:
    def __init__(self, height, side_one, side_two, side_three, perimeter=0, area=0):
        self.side_one = side_one
        self.side_two = side_two
        self.side_three = side_three
        self.height = height
        self.perimeter = perimeter
        self.area = area

    def __str__(self):
        return f'Triangle\nSides: {self.side_one}, {self.side_two}, {self.side_three}\nHeight: {self.height}\nPerimeter: {self.perimeter}\nArea: {self.area}'

    def perim_calc(self):
        return round(self.side_one + self.side_two + self.side_three, 4)

    def area_calc(self):
        return round((self.side_one * self.height) / 2, 4)
#makes class for circle
class circl:
    def __init__(self, radius, perimeter=0, area=0):
        self.radius = radius
        self.perimeter = perimeter
        self.area = area

    def __str__(self):
        return f'Circle\nRadius: {self.radius}\nCircumference: {self.perimeter}\nArea: {self.area}'

    def perim_calc(self):
        return round(2 * 3.141592 * self.radius, 4)

    def area_calc(self):
        return round(3.141592 * self.radius * self.radius, 4)
#makes the rectangle
def make_rect():
    length = number_input("Enter the rectangle's length:")
    width = number_input("Enter the rectangle's width:")
    if length == width:
        rectangle = square(length)
    else:
        rectangle = rect(length, width)
    rectangle.perimeter = rectangle.perim_calc()
    rectangle.area = rectangle.area_calc()
    print(rectangle)
    return rectangle
#makes the triangle
def make_tri():
    side_one = number_input("Enter the base of the triangle:")
    height = number_input("Enter the height of the triangle:")
    side_two = number_input("Enter the second side:")
    side_three = number_input("Enter the third side:")
    triangle = tri(height, side_one, side_two, side_three)
    triangle.perimeter = triangle.perim_calc()
    triangle.area = triangle.area_calc()
    print(triangle)
    return triangle
#makes the circle
def make_circle():
    radius = number_input("Enter the radius of the circle:")
    circle = circl(radius)
    circle.perimeter = circle.perim_calc()
    circle.area = circle.area_calc()
    print(circle)
    return circle