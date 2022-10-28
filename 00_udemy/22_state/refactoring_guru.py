from abc import abstractmethod, ABC
from typing import Type

class Context:
    '''
    The interface of interest for the Client. 
    Maintains reference to an instance of State Class, which represents current state.
    '''

    _state = None
    '''
    Reference to the current state
    '''

    def __init__(self, state) -> None:
        '''
        Initiliazes and transitions to determined state
        '''
        self.transition_to(state)

    def transition_to(self, state):
        '''
        The helper function which executes the transition of state
        '''
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    '''
    Actions according to the state
    '''
    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()

class State(ABC):
    '''
    The state can transition the context to another state?
    '''

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        #a propriedade interna _context recebendo a externa context
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass

class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1")

    def handle2(self) -> None:
        print("ConcreteStateA handles request2")

class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2")

if __name__ == '__main__':
    
    context = Context(ConcreteStateA())

    context.request1()
    context.request2()

    context.transition_to(ConcreteStateB())

    context.request1()
    context.request2()
