# metaclass of 
class Singleton(type):
    _instances = {}

    # __call__ dunder allows to instances behave like functions
    # and can be called like a function
    # 
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls)\
                .__call__(*args, **kwargs)
        return cls._instances[cls]

# class database will have its metaclass from Singleton class
# and Singleton class has its metaclass from type (obviously)
# since it's the metaclass for every class in python

class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading database')

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)



