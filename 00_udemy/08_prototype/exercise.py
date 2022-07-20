from typing import Type, Union, List, Dict, Optional
from unittest import TestCase
import copy

# main object
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    '''The idea is that a line starts with a point and ends at another point?'''
    def __init__(self, start:Type[Point], end:Type[Point]) -> None:
        self.start = start
        self.end = end

    def __str__(self):
        return f'starts at:  ({self.start.x},{self.start.y}) and ends at ({self.end.x},{self.end.y})'

    def deep_copy(self):
        return copy.deepcopy(self)

class Evaluate(TestCase):
    def test_exercise(self):
        line1 = Line(
            Point(3, 3),
            Point(10, 10)
        )
        line2 = line1.deep_copy()
        line1.start.x = line1.end.x = line1.start.y = line1.end.y = 0

        # linha 2 nao pode ter mudado, essa eh a questao
        self.assertEqual(3, line2.start.x)
        print(line2.start.x)
        self.assertEqual(3, line2.start.y)
        print(line2.start.y)
        self.assertEqual(10, line2.end.x)
        print(line2.end.x)
        self.assertEqual(10, line2.end.y)
        print(line2.end.y)


if __name__ == '__main__':
#     linhaa = Line(start = Point(x = 1, y = 1), end = Point(x = 2, y = 2))
#     print(linhaa)
#     linhab = linhaa.deep_copy()
#     print(f'\n\n {linhab}')

    evaluate = Evaluate()
    evaluate.test_exercise()


