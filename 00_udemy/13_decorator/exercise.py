from abc import ABC
from typing import Type

class Shape(ABC):
    def __str__():
        return ''

    def resize(self, factor):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return 'A circle of radius %s' % {self.radius}

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return 'A Square of side %s' % {self.side}

class ColoredShape:
  def __init__(self, shape:Type[Shape], color):
    self.shape = shape
    self.color = color

  def resize(self, factor):
    if callable(self.shape.resize):
        self.shape.resize(factor)
    
  def __str__(self):
    return '%s and color %s' % (str(self.shape), {self.color})

if __name__ == '__main__':
    circle =  Circle(5)
    square = Square(4)

    print(circle)
    print(square)
    print('\n\n')
    circle.resize(4)
    print(circle)
    print('\n\n')
    coloredCircle = ColoredShape(circle, 'green')
    print(coloredCircle)

    coloredCircle.resize(7)
    print(coloredCircle)

    print('\n\n')
    coloredSquare = ColoredShape(square, 'blue')
    print(coloredSquare)
    coloredSquare.resize(5)
    print(coloredSquare)