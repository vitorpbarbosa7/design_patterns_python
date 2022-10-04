# event broker (observer)
# cqs (setters and getters - commands and queries)

from typing import Type
from enum import Enum
from abc import ABC

class Event(list):
    '''
    Event as a list of functions (hence, can be called)
    '''
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class Game:
    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query):
        #when performs the query, calls the handle?

        #this is the method, that's why it works
        self.queries(sender, query)

class CreatureModifier(ABC):
    def __init__(self, game, creature):
        self.game =  game
        self.creature = creature

        print(f'before appending self.handle')
        self.game.queries.append(self.handle)
        print(f'after appending self.handle')

    def handle(self, sender, query):
        pass

class IncreaseAttackModifier(CreatureModifier):

    def handle(self, sender, query):
        print(f'before handling {query.value}')
        if sender.creature_name == self.creature.creature_name and query.what_to_query == WhatToQuery.ATTACK:
            query.value *= 2  
        print(f'after handling {query.value}')

class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2

class Query:
    def __init__(self, creature_name, what_to_query:Type[WhatToQuery], default_value):
        self.creature_name = creature_name
        self.what_to_query = what_to_query
        self.value = default_value
        
class Creature:
    def __init__(self, game, creature_name, attack, defense):
        self.game = game
        self.creature_name = creature_name
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self):
        q = Query(self.creature_name, WhatToQuery.ATTACK,self.initial_attack)
        print(f'Getter passed here')
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.creature_name, WhatToQuery.DEFENSE,self.initial_defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f'{self.creature_name} ({self.attack}/{self.defense})'

if __name__ == '__main__':
    game = Game()
    goblin = Creature(game, 'Strong goblin',2,2)
    print(goblin)

    print(f'before increasing')
    iam = IncreaseAttackModifier(game, goblin)
    print(f'after increasing')

    print(goblin)
