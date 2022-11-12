class Rectangle:
    def __init__(self, x, y, widht, height):
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height

    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.widht}, {self.height}'

    def getArea(self):
        return self.widht * self.height

rect_1 = Rectangle(5,10,50,100)
print(rect_1)
print(f'Площадь прямоугольника равна {rect_1.getArea()}')