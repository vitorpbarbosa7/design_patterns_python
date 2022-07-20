import pandas as pd

# a simple object
class Vazia:
    pass

# criar classe a partir do type
# criar casse MinhaClasse de maneira dinamica, atraves do type no return
def criaClasse(**args):
    # MinhaClasse vai hedar os argumentos?
    return type("MinhaClasse", (object, ), args)

if __name__ == '__main__':
    a = criaClasse(idade = 13, olhos = 2)
    # return another kind of class
    print(a)
    print(a.idade)
    print(a.olhos)
    print(dir(a))

    # python inside:
    print(pd.__dict__)