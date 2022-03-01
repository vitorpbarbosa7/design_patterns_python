class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None
    
    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} '+\
            f'works as {self.position}'

    @staticmethod
    def new():
        # new method will actually calls the PersonBuilder 
        # class/object to construct
        return PersonBuilder()


# In a good scenario we should not go back to PersonBuilder
# or any other class to modify it
# but only use others classes which inherits from it 
class PersonBuilder:
    def __init__(self):
        self.person = Person()

    
    # builder method actually returns person object
    # with its __str__ implementation as long as objects'
    # attributes
    def build(self):
        return self.person


# Inheritance:
class PersonInfoBuilder(PersonBuilder):
    # PersonInfoBuilder inherits from PersonBuilder
    # and PersonBuilder will be Sup Class for PersonInfoBuilder
    # then Person Builder person is initialized as Person
    # which is actually the concrete block
    def called(self, name):
        self.person.name = name
        # fluent interface
        return self


# Inheritence class tree keeps building 
# adding new attributes using self
class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self

# this last one will beautfully inherit every attribute 
# from previous classes
class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self

pb = PersonBirthDateBuilder()
me = pb\
    .called('Elliot')\
    .born('New York')\
    .works_as_a('Cybersecurity Engineer')\
    .build()
# print will alwais invoke __str__ implementation
print(me)


