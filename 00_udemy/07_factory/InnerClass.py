
from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


# this would be for example a cartesiana init from the CoordenateSystem
class Point:
    def __init__(self, x=0, y=0):
        # generic x and y
        # but if I need more arguments in any other 
        # args?
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    class PointFactory:
        # Factory method is returning the point concrete class
        # @staticmethod
        def new_cartesian_point(x,y):
            p = Point()
            p.x = x
            p.y = y
            return p

        # @staticmethod
        def new_polar_point(rho, theta):
            p = Point()
            p.x = rho * cos(theta)
            p.y = rho * sin(theta)
            return p


if __name__ == '__main__':
    # you can initialize the point, and then, define in which
    # cartesian use it
    p = Point(2, 3)
    p2 = Point.PointFactory.new_polar_point(1, 2)
    print(p, p2)



























# this would be for example a cartesiana init from the CoordenateSystem
# class Point:
    # def __init__(self, a, b, system = CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = a * sin(b)