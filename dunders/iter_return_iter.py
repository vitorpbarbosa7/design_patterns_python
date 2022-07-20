

class MyClass:
    # mega blaster global variable without need to say __init__?
    cache = {}

    def __init__(self, lista:list):
        self.lista = lista

        # cache implementation with hash code
        self.h = hash(tuple(lista))
        if self.h in self.cache:
            # does nothing
            return 

        self.cache[self.h] = lista

    def __iter__(self):
        # returning the values
        return iter(self.cache[self.h])

        # returning self
        # return self
        # result: TypeError: iter() returned non-iterator of type 'MyClass'

    def __str__(self):
        return f'lista: {self.lista}'

if __name__ == '__main__':
    obj1 = MyClass(lista = [1,2,3])
    obj2 = MyClass(lista = [4,5,6])

    obj = iter(obj1)
    try:
        while True:
            print(next(obj))
    except:
        print('no more elements')

