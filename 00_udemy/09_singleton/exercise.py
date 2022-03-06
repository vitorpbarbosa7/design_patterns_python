'''too much code here, knowin the difference between is and == would solve the problem'''

from typing import Type, Union, List, Dict
from abc import ABC
from enum import Enum, auto
import unittest

class Person(ABC):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'name is {self.name}'

def singleton(class_):
    # instances methods will be stored in a dict
    instances = {}

    #wrapper which adds/alters the class_ function
    def get_instance(*args, **kwargs):
        # if a instance is not in the set of instance, then we will add it 
        # to the set of instances
        if class_ not in instances:
            # add it
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    # return specific instance 
    return get_instance

# Trying to implement a PersonFactory singleton
# but a singleton factory would not be very useful
@singleton
class PersonFactory():
    _instances = {}

    # __call__ dunder allows to instances behave like functions
    # and can be called like a function
    # 
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(PersonFactory, cls)\
                .__call__(*args, **kwargs)
        return cls._instances[cls]

    def __init__(self, name):
        self.person = Person(name)
        # iteractively idx attribute from class
        # everytime you run this factory it augments the idx variable


    # def create_person(self,name):
    #     person = Person(name)
    #     # iteractively idx attribute from class
    #     # everytime you run this factory it augments the idx variable
    #     return person


class TestSingletonFactory(unittest.TestCase):

    def is_singleton(self,factory:Type[PersonFactory]):
        p1 = factory('Lionel').person
        p2 = factory('Cristiano').person
        self.assertEqual(p1,p2)

if __name__ == '__main__':
    TestSingletonFactory.is_singleton(PersonFactory)

