import copy
from typing import Type

class Address:
    def __init__(self, street_address, suite, city):
        self.suite = suite
        self.street_address = street_address
        self.city = city

    def __str__(self):
        return f'{self.street_address}, Suite #{self.suite}, {self.city}'
    
class Employee:
    def __init__(self, name, address):
        self.address = address
        self.name = name

    def __str__(self):
        return f'{self.name} works at {self.address}'

# that's effectly what makes the prototype possible
class EmployeeFactory:
    # static objects as Factorys?
    # two prototypes
    main_office_employee = Employee('', Address('123 East Drive','0','London'))
    aux_office_employee = Employee('', Address('123B East Drive','0','London'))

    # general creator which asks for what kind of prototype
    # agnostic to kind of employee
    @staticmethod
    def __new_employee(proto:Type[Employee], name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        # change object inside of address object which is inside of employee
        result.address.suite = suite
        return result


    # create factory methods for each prototype
    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            # use the prototype
            proto = EmployeeFactory.main_office_employee, 
            # and customize other attributes
            name = name, 
            suite = suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            # use the prototype
            proto = EmployeeFactory.aux_office_employee, 
            # and customize other attributes
            name = name, 
            suite = suite
        )
    
if __name__ == '__main__':
    elliot = EmployeeFactory.new_main_office_employee('Elliot',23)
    print(elliot)
    angela = EmployeeFactory.new_aux_office_employee('Angela',80)
    print(angela)