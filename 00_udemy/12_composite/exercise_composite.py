from abc import ABC
from collections.abc import Iterable
from typing import List, Union

class SumElements(Iterable, ABC):
    '''
    Allows for summing the values
    '''
    @property
    def sum(self):
        result = 0
        for element in self:
            for item in element:
                result += item
        return result

class SingleValue(SumElements):
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        yield self.value

class ManyValues(list, SumElements):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    single_value  = SingleValue(11)
    other_values = ManyValues()
    other_values.append(22)
    other_values.append(33)

    all_values = ManyValues()
    all_values.append(single_value)
    all_values.append(other_values)

    print(all_values)

    print(all_values.sum)

    
