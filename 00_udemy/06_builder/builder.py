# construction of a paragraph
text = 'hello'
parts = ['<p>', text, '</p>']
print(''.join(parts))

# E se eu quiser utilizar uma lista de palavras:
print('01. First \n\n')
words = ['hello','world']
# Ja comeca a ficar mais complicado de construir algo que generalize e faca a construcao de um paragrafo

print('02. Second n\n')
# unordered list
# open statement
parts = ['<ul>']
# <li> list item element 
for w in words:
    parts.append(f'  <li>{w}<\li>')
# at last
parts.append('</ul>')
print('\n'.join(parts))

# Precisamos terceirizar o processo de criacao

# Cada elemento do HTML pode ser instanciado a partir de uma classe por exemplo

print('\n\n 03 Third') 
class HtmlElement:
    indent_size = 2

    def __init__(self, name = '', text = ''):
        self.name = name
        self.text = text
        # elementos sao uma lista, por isso depois da para apendar ao elemento raiz, novos elementos
        self.elements = []

    # Representacao
    def __str(self, indent):
        # initial step
        # html syntax elements per se
        lines = []
        # identacao eh criada fazendo os espacos um certo numero de vezes, de acordo com o que vamos 
        # crescendo na arvore
        i = ' ' * (indent * self.indent_size) # uses fixed indent_size
        lines.append(f'{i}<{self.name}>')

        # text between html syntax elements
        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)
    
    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


# O Builder ta chamando o proprio elemento que sera construido
class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        # underscore underscore so that people don't access it directly
        self.__root = HtmlElement(name = root_name)

    # APIs para construir o objeto:
    # add child to current root
    def add_child(self, child_name, child_text):
        # Apendar ao root ()
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
            )

    # How to create a fluent interface in which we can chain it 
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        # se eu retorno o objeto inteiro per se, eu posso invocar a partir do mesmo as suas funcoes, que coisa linda
        return self

    # Como expor (ter a representacao) do objeto que estamos construindo?
    def __str__(self):
        # retornar a string de cada elemento
        return str(self.__root)


# with static method in which we can call it directly from class object
builder = HtmlElement.create('ul')
# builder.add_child('li','hello')
# builder.add_child('li','world')
builder.add_child_fluent('li','hello').add_child_fluent('li','hello')
print('Ordinay Builder')
# calls __str__
print(builder)














