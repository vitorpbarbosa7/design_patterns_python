from abc import ABC, abstractmethod
from typing import Type


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        pass

class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'lines'

class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'pixels'

class Shape:
    def __init__(self, renderer):
        self.renderer = renderer
        self.name = None

    def __str__(self):
        return f'Drawing {self.name} as {self.renderer.what_to_render_as}'

class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Triangle'

class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Square'


# imagine VectorTriangle and RasterTriangle are here too

if __name__ == '__main__':
    vector_renderer = VectorRenderer()
    square = Square(vector_renderer)
    print(square)

    raster_renderer = RasterRenderer()
    triangle = Triangle(raster_renderer)
    print(triangle)