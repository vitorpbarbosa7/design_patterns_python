''' Using the Liskov Substitution Principle I can change a attribute value 
making use of a function fot that, that is, a setter
'''

# Base class
# Sup class
class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        # returns from setters
        return self._width * self._height

    #representation
    # using properties instead of attributes
    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

# Implement as properties and not as attributes
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property 
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

class Square(Rectangle):
    # Initilializing the squre
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    # Changes rectangle width to correspond to height
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    # Changes rectangle width to correspond to width
    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value

def use_it(rc):
    _new_height = 10
    # first value of width and propagated forward
    w = rc.width
    # in the middle of the use_it function I change one of the values, with a setter
    # So the original value from the class will be substituted
    rc.height = _new_height
    # current value of widght versus this new height
    # The problem is here, in which original width is still ond value and height is new one
    expected = int(w*_new_height)
    # the object already had an property of area 
    # this area property correspond to the setters
    print(f'Expected an area of {expected},\n Got {rc.area}')

if __name__ == '__main__':
    # # Defined width and height here
    # rc = Rectangle(2,3)
    # use_it(rc)

    sq = Square(5)
    use_it(sq)

    newsquare = Square(3)
    print(f'First area value {newsquare.area}')

    newsquare.width = 5
    print(f'New square area {newsquare.area}')




