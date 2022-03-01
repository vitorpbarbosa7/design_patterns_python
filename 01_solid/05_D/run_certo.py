from typing import Type

# Base class with abstract classes
from db.interface import Repositorio

# Specific implementations
from db.mysql_repository import MySqlRepositorio
from db.mongo_repository import MongoDBRepositorio

''' nao pode inverter os papeis?

classe de negocio
mas essa classe de negocio ta herdando metodos de outras classes
escrever em banco de dados essa classe nao pode, tipo, definir os metodos 
de escrita, quem define eh a classe base 
'''

# classe de negocio se comunicando diretament com a interface
class Usuario:

    def __init__(self, repositorio: Type[Repositorio]) -> None:

        self.__repositorio = repositorio
        # agora temos os metodos abstratos, presentes na interface

    # cliente pode utilizar as funcoes de inserir da interface
    def armazenar_dados(self, dado: any)  -> None:
        self.__repositorio.inserir(dado)

    def remover_dado(self, dado: any) -> None:
        self.__repositorio.deletar(dado)



# agora, se eu precisar criar para outro banco de dados, eu nao preciso dar copy paste nas 300 funcoes basicas de todo banco de dados que eh igual 
# eu posso soh criar outra classe que herda as caracteristcas da base class
if __name__ == '__main__':

    # instanciar objetos
    # Onde defino o comportamento do usuario
    # class usuario aceita objeto do tipo repositorio, logo podemos coloar o MySqlRepositorio, porque ele herda da classe Repositorio
    # e devo passar a propria classe
    # mantenho a mesma interface, de Repositorio
    usuario_mysql = Usuario(MySqlRepositorio())
    usuario_mongodb = Usuario(MongoDBRepositorio())

    # manipulacao das funcoes
    # aqui sempre referenciando a interface, logo nunca vou precisar mudar na classe Usuario, a maneira basica
    usuario_mysql.armazenar_dados(dado = 'mysql_data')
    usuario_mongodb.armazenar_dados(dado = 'mongodb_data')

'''
Vamos analisar o problema aqui 
Se meu chefe vem e pede para nao utilizar mais MySql, e sim Mongo
Entao, minha camada de negocio, ta explicitamente dependendo diretamente do MySql, 
e eu preciso criar uma maneira que dependa apenas de uma maneira abstrata de banco de dados

https://www.youtube.com/watch?v=OHmTpOD_AdI




'''