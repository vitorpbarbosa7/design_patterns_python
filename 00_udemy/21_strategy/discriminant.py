from abc import ABC
from typing import Type
from cmath import sqrt

class DiscriminantStrategy(ABC):

    def calculate_discriminant(self, a, b, c):
        pass

class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):

        discriminant = b**2 - 4*a*c
        return discriminant

class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):

        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return float('nan')
        else:
            return discriminant

class QuadraticEquationSolver:

    _pos_result = None
    _neg_result = None

    def __init__(self, strategy:Type[DiscriminantStrategy]):
        self.strategy = strategy

    def solve(self, a, b, c):

        discriminant = self.strategy.calculate_discriminant(a,b,c)

        self._pos_result = (-b + sqrt(discriminant))/2*a
        self._neg_result = (-b - sqrt(discriminant))/2*a

        """ Returns a pair of complex (!) values """

    @property
    def result(self):
        return self._pos_result, self._neg_result


if __name__ == '__main__':

    ordinary = OrdinaryDiscriminantStrategy()
    real = RealDiscriminantStrategy()

    ordinary_solver = QuadraticEquationSolver(strategy = ordinary)
    real_solver = QuadraticEquationSolver(strategy = real)

    COEFFICIENTS = [1,2,7]
    
    a = COEFFICIENTS[0]
    b = COEFFICIENTS[1]
    c = COEFFICIENTS[2]

    ordinary_solver.solve(a,b,c)
    real_solver.solve(a,b,c)

    print(ordinary_solver.result)
    print(real_solver.result)