# utils, debug, very simple, i'm learning
def log(s):
    if DEBUG:
        print(s)

class CodeElement:
    indent_unit = 2

    def __init__(self, attribute = '', text = ''):
        self.attribute = attribute
        self.text = text
        # central array (actually a list) to receive every block of row code
        self.elements = []

    # string representation
    def __str(self, indent_multiplier):
        # each line of code will be constructed considering its pieces
        lines = []
        # indentation
        i = ' ' * (indent_multiplier * self.indent_unit)
        # appends identation and attribute
        # First attribute, class name
        # se for o primeiro elemento, entao inicializar
        if not self.text:
            lines.append(f'{i} class {self.attribute}:')
            i = ' ' * ((indent_multiplier + 1) * self.indent_unit)
            lines.append(f'{i} def __init__(self):')

        # # attributes objects
        # if self.text:
        #     i = ' ' * ((indent_multiplier + 1) * self.indent_unit)
        #     lines.append(f'{i}{self.text}')

        # para cada elemento na linha (construido a partir do CodeBuilder), retornar a representacao
        # __str, de forma recursiva, com adicional de identacao

        if self.text:
            log(lines)
            i = ' ' * ((indent_multiplier + 1) * self.indent_unit)
            lines.append(f'{i} self.{self.attribute} = {self.text}')

        for e in self.elements:
            log(e)
            lines.append(e.__str(indent_multiplier + 1))

        # uma vez adicionado o atributo e o texto, pular a linha, 
        # juntando as ja existentes
        log(lines)
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)



# Builder itself is very simple to create
class CodeBuilder:
    def __init__(self, root_name):
        self.__root = CodeElement(attribute = root_name)

    def add_field(self, child_attribute, child_text):
        # append next nodes to root_node, which also is a CodeElement
        self.__root.elements.append(
            CodeElement(child_attribute, child_text)
        )
        return self

    # string representation
    def __str__(self):
        return str(self.__root)

    
if __name__ == '__main__':
    DEBUG = False
    cb = CodeBuilder('Person').add_field('name', '""')\
                              .add_field('age','0')
print(cb)