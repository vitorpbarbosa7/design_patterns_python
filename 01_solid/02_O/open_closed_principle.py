import numpy as np
# import abstract base class
from abc import ABC, abstractmethod

# Abstract Class
class Operations(ABC):
    '''Operations'''
    @abstractmethod
    def operation():
        pass

    def general_function():
        # function which applies to any of subclasses which inherit from this one
        pass

# subclasses with similar function
class Mean(Operations):
    '''Compute Mean'''
    # aqui efetivamente eu implemento o que a operacao vai fazer
    def operation(list_):
        print(f'The mean is {np.mean(list_)}')

    def specific_function():
        # function which is specific to this class, it will not be a modification, because base class is 
        # being used
        # seria horrivel se eu precisa-se propagar essa funcao para outras classes, entao soh se for bem especifica
        pass

class Max(Operations):
    '''Compute Max'''
    def operation(list_):
        print(f'The max is {np.max(list_)}')



# Pode ocorrer apendices de novas operacoes que utilizam a "Operations" class como base
# mas cada classe nao vai ser modificada

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