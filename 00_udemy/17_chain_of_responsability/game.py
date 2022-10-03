from typing import Type

class Creature:
    def __init__(self, name, attack, defense, speed):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def __str__(self) -> str:
        return f'''
        {self.name} 
        - attack: {self.attack}
        - defense: {self.defense}
        - speed: {self.speed}
        '''

class CreatureModifier:
    def __init__(self, creature:Type[Creature]):
        self.creature = creature
        self.next_modifier = None
    
    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

        return modifier
    
    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()

class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f'Doubling {self.creature.name}''s attack')
        self.creature.attack *= 2
        super().handle()

class DoubleDefenseModifier(CreatureModifier):
    def handle(self):
        # condition to jump this modifier
        if self.creature.attack < 2:
            print(f'Doubling {self.creature.name}''s defense')
            self.creature.defense *= 2
        #propagates
        super().handle()

class DoubleSpeedModifier(CreatureModifier):
    def handle(self):
        print(f'Doubling {self.creature.name}''s speed')
        self.creature.speed *= 2
        super().handle()

# Breaking the chain without calling the super handle(), because it's the one which propagates
class NoBonuses(CreatureModifier):
    def handle(self):
        print('No Bonuses for you')


if __name__ == '__main__':

    creature = Creature('dragon', 4, 1, 1)
    print(creature)

    root = CreatureModifier(creature)

    # runtime modifiers construction
    # modifier can be jumped
    root.add_modifier(DoubleAttackModifier(creature))\
        .add_modifier(DoubleDefenseModifier(creature))\
        .add_modifier(NoBonuses(creature))\
        .add_modifier(DoubleSpeedModifier(creature))

    root.handle()

    print(creature)    
