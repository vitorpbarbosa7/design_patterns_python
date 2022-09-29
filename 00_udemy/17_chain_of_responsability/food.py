from abc import ABC, abstractmethod
from typing import Any, Optional, Type

class Handler(ABC):
    '''
    Handler interface with set_next handler and handle method to handle the request
    '''

    @abstractmethod
    def set_next(self, handler):
        pass

    def handle(self, request):
        pass

class AbstractHandler(Handler):
    '''
    Default chaining behaviour can be implemente in a Super Class and used in subclasses
    '''

    _next_handler: Handler = None

    def set_next(self, handler):
        self._next_handler = handler

        return handler

    @abstractmethod
    def handle(self, request):
        '''
        #1
        The magic for passing it along is here
        '''
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

'''
The Concrete Classes will handle the request or pass it along the Chain of Responsability
'''

class MonkeyHandler(AbstractHandler):
    def handle(self, request):
        if request == "Banana":
            return f"\nMonkey eats the {request}"
        else:
            #2 and the other part is here
            # returns handle method from super class which goes to next handler
            return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request):
        if request == 'Nuts':
            return f"\nSquirrel eats the {request}"
        else:
            return super().handle(request)

class CatHandler(AbstractHandler):
    def handle(self, request):
        if request == 'Fish':
            print(f"\nCat ate the delicious {request}")
        else:
            return super().handle(request)



def client_code(handler:Type[AbstractHandler]):
    '''
    As a kedro node function, the client code
    '''

    # some foods to be processed
    for food in ['Banana','Nuts','Fish']:
        # result from request
        
        # if it is the Banana, the monkey will alreay process it (if else statement)
        # if it is not the Banana, monkey will pass it and leave it to the squirrel, which will process it

        # that depends how we create the chain of resposability

        print(f'Who wants {food} ?')
        result = handler.handle(food)
        if result:
            print(f'Result from processing the {food}: {result}')
        else:
            print(f'The food {food} was not eaten')
        
if __name__ == '__main__':

    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    cat = CatHandler()

    # define the the chain of responsability

    # Runtime definition of chain of responsability
    # monkey has two nexts
    monkey.set_next(squirrel).set_next(cat)

    print(rf'Monkey -> Squirrel -> Cat ')
    client_code(monkey)

    print('\n\n')
    print(rf'Squirrel -> Cat')
    client_code(squirrel)
