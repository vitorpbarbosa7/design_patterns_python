from typing import Union, Type, List
from abc import ABC

class StrategyInterface(ABC):

    def start(self, buffer):
        pass

    def end(self, buffer):
        pass

    def add_list_item(self, buffer, item):
        pass


class MarkdownStrategy(StrategyInterface):

    def add_list_item(self, buffer, item):
        buffer.append(rf' * {item} \n')


class HtmlListStrategy(StrategyInterface):

    def start(self, buffer):
        buffer.append(rf'<ul> ')

    def end(self, buffer):
        buffer.append(rf' </ul> \n')

    def add_list_item(self, buffer, item):
        buffer.append(rf' <li> {item} </li>')

# Concrete use
class TextProcessor:
    def __init__(self, strategy:Type[StrategyInterface]):
        self.strategy = strategy()
        self.buffer = []

    def append_list(self, items:Union[List, int, str]):
        self.strategy.start(self.buffer)
        for item in items:
            self.strategy.add_list_item(self.buffer, item)
        self.strategy.end(self.buffer)

    def __str__(self):
        return '\n'.join([_str for _str in self.buffer])

if __name__ == '__main__':

    NEY = ['neymar', 'junior']
    LEO = ['lionel', 'messi']

    ney_process = TextProcessor(MarkdownStrategy)
    ney_process.append_list(NEY)
    print(ney_process)

    leo_process = TextProcessor(HtmlListStrategy)
    leo_process.append_list(LEO)
    print(leo_process)