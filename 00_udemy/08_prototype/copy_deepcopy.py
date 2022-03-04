import copy
 
class Address:
    def __init__(self, street_address, city, country):
        self.city = city
        self.street_address = street_address
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


 
# how to make it easy to make another person to live at the same addres? 

if __name__ == '__main__':
    john = Person('Elliot', Address('217 East Broadway','New York','USA'))

    jane = copy.deepcopy(john)
    # now I can customize the address
    jane.name = 'Jane'
    jane.address = Address('218 East Broadway','New York','USA')
    print(john)
    print(jane)

