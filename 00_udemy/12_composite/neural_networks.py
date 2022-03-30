from abc import ABC, abstractmethod
from collections.abc import Iterable

class Connectable(Iterable, ABC):
    '''
    Base Class function which implements connect_to method 
    which with self logics allow us to use the connect_to with 
    Neuron and NeuronLayer classes
    '''
    def connect_to(self, right_neurons):
        
        myself_left_neuron = self
        if myself_left_neuron == right_neurons:
            return 

        for myself_left_neuron in self:
            for right_neuron in right_neurons:
                myself_left_neuron.outputs.append(right_neuron)
                right_neuron.inputs.append(myself_left_neuron)

class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self):
        return f'{self.name}, ' \
            f'{len(self.inputs)} inputs,' \
                f'{len(self.outputs)} outputs'

    def __iter__(self):
        yield self

class NeuronLayer(list, Connectable):
    def __init__(self, name, count):
        '''
        Parameters:
        ---------------
        name: name of this Neuron Layer
                ex: Hidden Layer, Output Layer
        count: How many neurons we want in this layer, so it will be appended
        '''
        
        super().__init__()
        self.name = name
        for x in range(0, count):
            self.append(Neuron(f'{name}-{x}'))

    def __str__(self):
        return f'{self.name} with {len(self)} neurons'

if __name__ == '__main__':
    neuron1 = Neuron('n1')
    neuron2 = Neuron('n2')

    layer1 = NeuronLayer('L1',3)
    layer2 = NeuronLayer('L2', 4)

    neuron1.connect_to(neuron2)

    neuron1.connect_to(layer1)

    layer1.connect_to(neuron2)
    layer1.connect_to(layer2)

    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)

