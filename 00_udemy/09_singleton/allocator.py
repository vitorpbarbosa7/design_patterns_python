'''
Whenever a class is instantiated, the __new__ and __init__ methods are called

__new__ method is always called before the __init__ method

__new__ method can decide if __init__ will be called or not

'''

import random

class Database:
    _instance = None

    # cls is the class object to be instantiated
    def __new___(cls, *args, **kwargs):
        # if it was not instantiated
        if not cls._instance:
            # instantiante then
            cls._instance = super(Database, cls)\
                .__new__(cls, *args, **kwargs)
            return cls._instance
        ''' allocator method which will be responsible to allocate the object in memory'''

    def __init__(self):
        # this will demonstrate that it is really a different object, and should not be 
        # that is, the initializer is still called
        id = random.randint(1,101)
        print('id = ', id)
        print('Loading a database from file')

if __name__ == '__main__':
    # in this case both databases will be the same
    d1 = Database()
    d2 = Database()
    print(d1 == d2)    
