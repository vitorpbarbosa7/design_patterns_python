class Figure:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        # only returns 
        return self.__color
    
    @color.setter
    def color(self, color):
        # sets the parameter according to what is passed
        self.__color = color



# color eh a mesma propriedade para os dois
class Circle(Figure):
    def __init__(self, color, radius):
        # mandar par a mãe
        super().__init__(color)
        self.__radius = radius

    # create specific property and setter
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

        

class Square(Figure):
    def __init__(self, color, width):
        # mandar par a mãe
        super().__init__(color)
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

if __name__ == '__main__':
    c1 = Circle('red', 10)
    s1 = Square('green', 5)

print('Creation from specific objects which inherits')
print(s1.color)

# Can instantiate the concrete class
print(f'Creation from base class')
f = Figure('Orange')
print(f.color)

# Maybe we should block this Figure class to make it impossible to use it, since it's a abstract class