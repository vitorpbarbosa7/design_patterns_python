from abc import ABC
from typing import Type, Union, List

class Shape(ABC):
	def __str__(self):
		return ''

class Circle(Shape):
	def __init__(self, radius:Union[int, float]):
		self.radius = radius

	def resize(self, factor:Union[int, float]):
		self.radius *= factor

	def __str__(self):
		return f'A circle of radius {self.radius}'

class Square(Shape):
	def __init__(self, side:Union[int, float]):
		self.side = side

	def __str__(self):
		return f'A square with side {self.side}'

# adding new functionalities to Shape objects
# inheriting from Shape so that works with both Square and Circle
class ColoredShape(Shape):
	def __init__(self, shape:Type[Shape], color:str):
		if isinstance(shape, ColoredShape):
			raise Exception('Cannot apply recursively decorator')
		self.shape = shape
		self.color = color

	def __str__(self):
		return f'{self.shape} has the color {self.color}'

class Quota(Shape):
	def __init__(self, shape:Type[Shape], quota):
		self.shape = shape
		self.quota = quota

	def __str__(self):
		return f'{self.shape} has quota {self.quota}'

if __name__ == '__main__':
	circle = Circle(2)
	print(circle)	
	
	red_circle = ColoredShape(shape = circle, color = 'red')
	print(red_circle)

	red_cilinder = Quota(shape = red_circle, quota = 5)
	print(red_cilinder)

	mixed_color = ColoredShape(ColoredShape(Circle(7), 'purple'), 'cyan')
	print(mixed_color) 
