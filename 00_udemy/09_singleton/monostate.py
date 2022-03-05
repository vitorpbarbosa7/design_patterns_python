'''
The best approach is to use decorator or metaclass to create 
the singleton function which will govern the function class behaviour 
when instantiated, that is, share same attributes, as a singleton should do
'''

# typical company has a single CEO
class CEO:
    # static state that is shared for every CEO class that will be instantiated
    __shared_state = {
        'name':'Steve',
        'age':55
    }

    def __init__(self):
        # whenever you initialize an CEO, you will use the same attributes
        # when we use self.__dict__ equals to a dictionary, we're attributing several 
        # things at once
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f'{self.name} is {self.age} years'

# 
class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        # this __dict__ can be setted outside, it's accessible for the client
        # to create any attribute in subclass
        obj.__dict__ = cls._shared_state
        return obj 
        
# CFO inherits from Monostate? 
# is it the same as metaclass?
class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money_managed = 0

    def __str__(self):
        return f'{self.name} manages ${self.money_managed}'



if __name__ == '__main__':
    # ceo1 = CEO()
    # print(ceo1)

    # # ceo2 changed also the ceo1
    # ceo2 = CEO()
    # ceo2.age = 77 
    # print(ceo1)
    # print(ceo2)

    cfo1 = CFO()
    cfo1.name = 'Shery1'
    cfo1.money_managed = 1
    print(cfo1)

    # both refer to the same, it's reaally a monostate
    # this isn't the best approach 
    cfo2 = CFO()
    cfo2.name = 'Ruth'
    cfo2.money_managed = 10
    print(cfo1, cfo2, sep = '\n')
