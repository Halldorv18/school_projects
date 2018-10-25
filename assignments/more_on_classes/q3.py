class Rectangle(object):
    def __init__(self, length=0,width=0):
        if length < 0:
            length = 0
        elif width < 0:
            width = 0
        self.length = length
        self.width = width
    def __str__(self):
        return "Length: {}, Width: {}".format(self.length, self.width)
    def __eq__(self, other_rectangle):
        return self.area() == other_rectangle.area()
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return self.length*2 + self.width*2
    def __repr__(self):
        return "Rectangle({},{})".format(self.length, self.width)