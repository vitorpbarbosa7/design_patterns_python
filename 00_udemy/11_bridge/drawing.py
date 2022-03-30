# circle square
# vector raster

# One approach: four approaches
# VectorCircle
# VectorSquare
# RasterCircle
# RasterSquare

# The famous complexity explosion 

from typing import Type

from abc import ABC, abstractmethod

class Renderer(ABC):
    def render_circle(self, radius):
        pass

    def render_square(self, side):
        pass
    # render_square

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')

    def render_square(self, side):
        print(f'Drawing a square of side {side}')

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')

    def render_square(self, side):
        print(f'Drawing pixels for a square of side {side}')

class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self, factor):
        pass

class Circle(Shape):
    def __init__(self, renderer:Type[Renderer], radius):
        super().__init__(renderer)
        self.radius = radius
    
    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor

class Square(Shape):
    def __init__(self, renderer:Type[Renderer], side):
        super().__init__(renderer)
        self.side = side 

    def draw(self):
        self.renderer.render_square(self.side)

    def resize(self, factor):
        self.side *= factor

if __name__ == '__main__':
    raster_renderer = RasterRenderer()
    vector_renderer = VectorRenderer()
    circle = Circle(raster_renderer, 5)
    square = Square(vector_renderer, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
    square.draw()
    square.resize(2)
    square.draw()
