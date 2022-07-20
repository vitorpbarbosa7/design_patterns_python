from abc import ABC
from enum import Enum, auto

class Person(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __str__(self):
        return f'id is {self.id} and name is {self.name}'

# inherits attributes
class PersonFactory():
    # class attributes
    idx = 0

    def create_person(self,name):
        person = Person(PersonFactory.idx, name)
        # iteractively idx attribute from class
        # everytime you run this factory it augments the idx variable
        PersonFactory.idx += 1
        print(person)

if __name__ == '__main__':
    person = PersonFactory()
    person.create_person('Lionel')
    # print output
    person.create_person('Cristiano')
    # print output
    person.create_person('Mbappe')



