from typing import Type

class A:

    x = 5

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        return value
    
class ChangesA:
    def __init__(self,class_a:Type[A]):
        self.x_changed = class_a.x*2

    
class ChangesA2:
    def __init__(self,class_a:Type[A]):
        self.y_changed = class_a.y*2

if __name__ == '__main__':

    a = A
    a_changed = ChangesA(a)
    print(a.x)
    print(a_changed.x_changed)

    a.x = 10
    print(a_changed.x_changed)

    
    a2 = A
    a2.y = 2
    a_changed2 = ChangesA2(a2)
    print(a_changed2.y_changed)

    a2.y = 10
    print(a_changed2.y_changed)

    # # change
    # a.x = 5
    # print(a.x)