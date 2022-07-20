'''
calculate_area calculates the area of a given rectangle

but I want to calcualte the are of a Square only
'''

from unittest import TestCase
from typing import Type, Union, List, Dict

class Square:
    def __init__(self, side=0):
        self.side = side

def calculate_area(rc):
    return rc.width * rc.height

class SquareToRectangleAdapter:
    def __init__(self, square):
        pass

class SquareToRectangleAdapter:
    '''Receives Square but transforms it to rectangle'''
    def __init__(self, square:Type[Square]):
        self.square = square

        # # transforms to Rectangle
        # self.width = square.side
        # self.height = square.side

        # When square object changes it's values, the adapter will change to 
    @property
    def width(self):
        return self.square.side

    @property 
    def height(self):
        return self.square.side


class Evaluate(TestCase):
    def test_exercise(self):
        sq = Square(11)
        adapter = SquareToRectangleAdapter(sq)
        self.assertEqual(121, calculate_area(adapter))
        sq.side = 10
        self.assertEqual(100, calculate_area(adapter))

if __name__ == '__main__':


    square = Square(side = 5)
    rectangle = SquareToRectangleAdapter(square)
    print(calculate_area(rectangle))

    Evaluate().test_exercise()


    
