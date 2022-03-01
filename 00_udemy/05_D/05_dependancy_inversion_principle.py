from abc import abstractmethod
from enum import Enum

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLINKG = 2

class Person:
    def __init__(self,name):
        self.name = name


#Solve the problem with this class
class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self,name): pass
    
# Low level module, since it deals for example with storage
# A module which stores the relations
# any relationship here will inherit from RelationshipBrowser
# This function could for example relate to a database
class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self,parent,child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self,name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name



# High level module:
# Research is a client function, which is now depending on how 
# the previous class relationship is implemented 
# So if there we used a tuple to stablish the relationship, 
# here we must implement a loop with tuple structure
class Research: # High level module
    # def __init__(self, relationships):
    #     relations = relationships.relations

    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}')

    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a children name {p}')




if __name__ == '__main__':

    parent = Person('John')
    child1 = Person('Chris')
    child2 = Person('Matt')

    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    Research(relationships)

        