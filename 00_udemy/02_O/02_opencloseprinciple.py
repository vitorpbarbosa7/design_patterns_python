from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# OCP : The Open Close Principle says:
# open for extension, close for modification
# a class, once created, should not be modified, but only 
# receive extensions considering current funcionality
# because this game of modifications could go forever
# this approach of adding keeps going and going and its not scalabe

class ProductFilter:
    ''' 
    pass the color, the list of products, and then it retuns only 
    the products with specified color
    '''
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    # add another filter
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    # then your manager comes and says, oh, add another filter 
    # then you have an idea of other useful filter... 
    # and this keeps going forever with modifications

# Enterprise pattern:
# Specification 

class Specification:
    # if a object respects or not a specific criteria
    def is_satisfied(self, item):
        pass

    # to use & operator
    # dunder __and__method modified
    # when & is called, it will use AndSpecification function
    def __and__(self, other):
        return AndSpecification(self, other)

############## The important Class to make it possible to generalize
class Filter:
    '''
    This class allow us to filter by anything, not a specific one
    '''
    def filter(self, items, spec):
        pass

class ColorSpecification(Specification):

    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):

    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class BetterFilter(Filter):
    def filter(self, items, spec):
        # check if specification are satisfied
        for item in items:
            if spec.is_satisfied(item):
                yield item

if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

# old method
pf = ProductFilter()
print('Green products (old):')
for p in pf.filter_by_color(products, Color.GREEN):
    print(f' - {p.name} is green')

# new method, with open closed principle
bf = BetterFilter()
print('Green products (new):')
# check if it is green
green = ColorSpecification(Color.GREEN)
# the filter method is general, 
# and we only have to create new specification objects
for p in bf.filter(products, green):
    print(f' - {p.name} is green')

print('Large Products (new)')
large = SizeSpecification(Size.LARGE)

for p in bf.filter(products, large):
    print(f' - {p.name} is large')

# Implement the combination
# AndSpecification method inherits anything defined in Specification
# So, if we defined __and__ dunder method to work like:
# return AndSpecification(self, other)
# it will
class AndSpecification(Specification):
    # pass more than one argument
    def __init__(self, *args):
        self.args = args
    
    def is_satisfied(self, item):
        # all checks if every return is a boolean value of True 
        # map applies the lambda function
        return all(map(
            # go through every item and check if specification is 
            # satisfied
            # the self.args are the specifications
            # the items will be the products
            lambda spec: spec.is_satisfied(item), self.args
        ))

print('Large green items: (with no dunder)')
green_and_large = AndSpecification(
    ColorSpecification(Color.BLUE), 
    SizeSpecification(Size.LARGE)
    )

for p in bf.filter(products, green_and_large):
    print(f'- {p.name} is green and large')


print('Large green items: (with dunder method __and__)')
green = ColorSpecification(Color.GREEN)
green_large = large & green
for p in bf.filter(products, green_large):
    print(f'- {p.name} is green and large')
