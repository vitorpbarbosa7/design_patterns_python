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
    count = 0

    def __init__(self, line:Type[Line]):
        super().__init__()
        self.count += 1

        # Generate points for the line
        print(f'{self.count}: Generating points for the line'
        f'[{line.start.x},{line.start.y}]->'
        f'[{line.end.x},{line.end.y}]')

        # coordinates for the line
        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        bottom = min(line.start.y, line.end.y)
        top = max(line.start.y, line.end.y)

        # if right point equals left point
        if right - left == 0:
            # append the several points of the line
            for y in range(top, bottom):
                self.append(Point(x = left, y = y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                self.append(Point(x = x, y = top))

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
        Rectangle(0,0,2,2),
        Rectangle(1,1,2,2)
    ]
    # When we call two times, for example, we see it generates temporary objects
    # because
    draw(rcs)
    draw(rcs)