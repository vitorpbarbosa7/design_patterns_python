class Car():
    def __init__(self, type):
        self.type = type
        # dictionary properties
        self.car_properties = {}

    # setter
    def set_properties(self, color, gear, capacity):
        self.car_properties = {'Color':color,
                                'Gear':gear,
                                 'Capacity':capacity}

    # getter
    def get_properties(self):
        return self.car_properties

class PetrolCar(Car):
    # realmente aqui a subclass pode ser substituida pela 
    # base class
    def __init__(self,type):
        # type subscreve o atribute da class Sup (Base Class)
        self.type = type
        self.car_properties = {}


    # can implement some other functions which are special to PetrolCar here
    def burnfuel(self,fuel):
        pass
    
    def destroyplanet(self, measurement):
        pass


# instanciar a partir da classe base
car = Car('SUV')
car.set_properties('Red','auto',6)

# instanciar um caso especifico
petrol_car = PetrolCar('sedan')
petrol_car.set_properties('Yellow','manual',4)

# list with every car object 
cars = [car,petrol_car]


def find_red_cars(cars):
    red_cars = 0.0
    for car in cars:
        if car.get_properties()['Color'] == 'Red':
            red_cars+=1
    print(f'Number of Red Cars = {red_cars}')

find_red_cars(cars)




