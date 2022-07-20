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
    def __init__(self):
        self.public = []
        self.idx = 0

    # non static method ~@staticmethod    
    def create_person(self, name):
        self.idx += 1
        # public object allow us to store names and auto
        self.public.append(( name, self.idx))
        print(Person(id = self.public[len(self.public)-1][1], 
                     name = self.public[len(self.public)-1][0]))


if __name__ == '__main__':
    person = PersonFactory()
    person.create_person('Lionel')
    # print output
    person.create_person('Cristiano')
    # print output
    person.create_person('Mbappe')



