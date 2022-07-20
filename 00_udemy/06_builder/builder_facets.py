# diferentes aspectos de uma pessoa
# Building blocks

from typing import Type

class Pessoa:
    def __init__(self):
        print('Creating an instance of Person')
        ## for each of those, we will use a builder
        
        ### ADRESS
        self.street_name = None
        self.postcode = None
        self.city = None

        ### JOB
        self.company_name = None
        self.position = None
        self.annual_income = None

# Deve ser possivel printar essa personalidade
    def __str__(self) -> str:
        return f'Address: {self.street_name}, {self.postcode}, {self.city}\n' +\
            f'Employed at {self.company_name} as a {self.position} earning {self.annual_income}'


# Builders for job information and another for address

# And also a third builder, a PersonBuiler

class PersonBuilder:
    def __init__(self, pessoa=None):
        if pessoa is None:
            self.pessoa = Pessoa()
        else:
            self.pessoa = pessoa

    # How can we make the client use the PersonJobBuilder Class?
    # property of PersonBuilder calls Class PersonJobBuilder
    # to get the work (works)
    @property
    def works(self):
        # aqui na real ta entrando o pessoa
        # e a inicializacao do PersonJobBuilder eh o PersonBuilder
        # e a inicializacao do PersonBuilder chama o pessoa
        return PersonJobBuilder(self.pessoa)
    
    @property
    def lives(self):
        return PersonAddressBuilder(self.pessoa)

    # retorno a Pessoa, que foi tendo seus atributos alterados
    def build(self):
        return self.pessoa

# Inherits from PersonBuilder
class PersonJobBuilder(PersonBuilder):
    # vamos passar uma pessoa na qual ja estamos trabalhando com ela, e nao um 
    # novo objeto para ser instanciado
    def __init__(self, pessoa):
        # retornar a propria inicializacao da Sup Class
        super().__init__(pessoa)

    # pessoa works at some place
    def at(self, company_name):
        self.pessoa.company_name = company_name
        # fluent interface
        return self 

    def as_a(self, position):
        self.pessoa.position = position
        return self

    def earning(self, annual_income):
        self.pessoa.annual_income = annual_income
        return self

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, pessoa):
        super().__init__(pessoa)

    def at(self, street_name):
        self.pessoa.street_name = street_name
        return self

    def code(self, postcode):
        self.pessoa.postcode = postcode
        return self

    def city_(self, city):
        self.pessoa.city = city
        return self


if __name__ == '__main__':
    pb = PersonBuilder()
    # pessoa builder level
        # PersonAddressBuilder level
            # PersonAddressBuilder level for methods which alter the self attributes from base class as all are interconected
    p = pb.\
        lives\
            .at('Avenida Paulista')\
            .code('05249-520')\
            .city_('Sao Paulo')\
        .works\
            .at('Tesla')\
            .as_a('Software Engineer')\
            .earning('500k Dollars')\
        .build()
print(p)