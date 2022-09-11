from abc import ABC, abstractmethod



class Person(ABC):
    '''
    Abstract base class
    '''

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self, msg):
        pass


    def __drop_all_fucking_useless_variables(self):
        


class Indian(Person):

    '''
    Detalhe de implementacao
    Classe cliente
    '''

    def speak(self, msg):
        print(f'Indian language')

class Brazilian(Person):

    def speak(self, msg):
        print('Football')


