

# base class
class Car():
    def __init__(self, type):
        self.type = type

# subclass
class PetrolCar(Car):
    def __init__(self, type):
        self.type = type


# properties being erroneous modified outside of 
# class base function and method

# call base class
car = Car('SUV')
#add properties to base class
car.properties = {'Color':'Red','Gear':'Auto','Capacity':6}
print(car.properties)

# petrol car which inherits from base class
petrol_car = PetrolCar('Sedan')
# defining properties in a no standard manner
petrol_car.properties = ('Blue':'Manual',4)
print(petrol_car.properties)





