from abc import ABC, abstractmethod

class BaseClass(ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def operation(self):
        pass

class mean(BaseClass):
    def operation(self):
        return ((self.a + self.b)/2)

class sum(BaseClass):
    def operation(self):
        return ((self.a + self.b))

if __name__ == '__main__':
    A = 2
    B = 2
    list_ = ([operation(A,B).operation() for operation in BaseClass.__subclasses__()])
    print(list_)

