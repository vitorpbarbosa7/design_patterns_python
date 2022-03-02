# abstract factory class to create others 

from abc import ABC

class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious')

class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')

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

# create the make_entry function
def make_drink(type:str):
    if type == 'tea':
        return TeaFactory.prepare(200)
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None



if __name__ == '__main__':
    entry = input('What kind of drink would you like?')
    drink = make_drink(entry)