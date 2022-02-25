import numpy as np
# import abstract base class
from abc import ABC, abstractmethod

# Abstract Class
class Operations(ABC):
    '''Operations'''
    @abstractmethod
    def operation():
        pass

# subclasses with similar function
class Mean(Operations):
    '''Compute Mean'''
    def operation(list_):
        print(f'The mean is {np.mean(list_)}')

class Max(Operations):
    '''Compute Max'''
    def operation(list_):
        print(f'The max is {np.max(list_)}')

# this class right here should be also closed for modification, so, any new classes should be added before
class Main:
    '''Main'''
    @abstractmethod
    def get_operations(list_):
        for operation in Operations.__subclasses__():
            # call operation method from subclasses
            operation.operation(list_)

if __name__ == '__main__':
    Main.get_operations([1,2,3,4,5,6])