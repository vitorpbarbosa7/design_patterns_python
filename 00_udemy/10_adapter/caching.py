from typing import Type, Union, List, Dict

class Point:
    def __init__(self,x,y):
        self.y = y
        self.x = x
    
    def draw_point(p):
        print('.', end = '')

# This is an API, like, the pandas is an api, so you need to 
# adapt to correspond to your needs

# my application:
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Rectangle(list):
     def __init__(self, x, y, width, height):
         # call base class initializer
         super().__init__()
         # start = (0,0)
         self.append(Line(Point(x,y), Point(x + width,y)))
         self.append(Line(Point(x,y), Point(x, y + height)))
         # start = (1,1)
         self.append(Line(Point(x + width, y + height), Point(x + width, y)))
         self.append(Line(Point(x + width, y + height), Point(x, y + height)))

# Build the Adapter
class LinetoPointAdapter(list):
    '''Receives a line and transforms it in a series of points'''
    cache = {}

    def __init__(self, line:Type[Line]):
        
        # cache implementation with hash code
        self.h = hash(line)
        if self.h in self.cache:
            # does nothing
            return 

        super().__init__()

        # Generate points for the line
        print(
        f'[{line.start.x},{line.start.y}]->'
        f'[{line.end.x},{line.end.y}]'
        )

        # coordinates for the line
        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        bottom = min(line.start.y, line.end.y)
        top = max(line.start.y, line.end.y)

        # append list to the cache
        points = []

        # if right point equals left point
        if right - left == 0:
            # append the several points of the line
            for y in range(top, bottom):
                points.append(Point(x = left, y = y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x = x, y = top))

        # each line has a sequence of points
        # line defined by the hash key 
        # points will be assigned as values
        self.cache[self.h] = points

    # iterar over each object
    # self.cache[self.h] return an object of self
    # __iter__ allows to execute the __init__ method 
    # over every element?
    def __iter__(self):
        # When I iterate the object adapter, it will return the iteration over the hash object?
        return iter(self.cache[self.h])

def draw(rcs):
    print('\n\n --- Drawing some stuff --- \n')
    for rc in rcs:
        for line in rc:
            # our original api which were given to us is based on points, and not 
            # in lines

            # calls the adapter interface4
            # adapter returns a list of points, from the line it is given]
            # in this case p is a part of line
            # original interface is a part of my interface i constructed
            adapter = LinetoPointAdapter(line)
            for p in adapter:
                p.draw_point()



if __name__ == '__main__':
    rcs = [
        Rectangle(0,0,4,4),
        Rectangle(1,1,10,11)
    ]
    # When we call two times, for example, we see it generates temporary objects
    # because
    draw(rcs)
    draw(rcs)