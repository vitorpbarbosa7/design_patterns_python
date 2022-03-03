# abstract factory class to create others 

from abc import ABC
from enum import Enum, auto

class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious')

class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')

# Keeping this abstract class helps you to know what kind of interface, api, is expected to be implemented
class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water,'
              f' pour {amount} ml, enjoy')
        return Tea()

class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beaans, boil water,'
              f'pour {amount} ml, enjoy !')
        return Coffee()

# # create the make_entry function
# def make_drink(type:str):
#     if type == 'tea':
#         return TeaFactory.prepare(200)
#     elif type == 'coffee':
#         return CoffeeFactory().prepare(50)
#     else:
#         return None


# class to make use of the factories
class HotDrinkMachine:
    # This available drink class substitutes the function make_drink approach
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            # class AvailableDrink created to correspond to each drink
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                # eval parses string as a python code
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))
        
    ''' This implementation allows to call specific class according to what the 
    user wishes'''
    def make_drink(self):
        print('Available drinks:')
        for f in self.factories:
            print(f[0])
                 
        s = input(f'Please pick a drink (0-{len(self.factories)-1}): ')
        idx = int(s)
        s = input(f'Specify amount: ')
        amount = int(s)
        # use the specified factory to prepare the amount
        return self.factories[idx][1].prepare(amount)






if __name__ == '__main__':
    machine = HotDrinkMachine()
    machine.make_drink()


    # entry = input('What kind of drink would you like?')
    # drink = make_drink(entry)