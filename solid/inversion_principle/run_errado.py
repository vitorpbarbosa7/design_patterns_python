from typing import Type

from db.mysql_repository import MySqlRepositorio

# nao pode inverter os papeis?

# classe de negocio
# mas essa classe de negocio ta herdando metodos de outras classes
# escrever em banco de dados essa classe nao pode, tipo, definir os metodos 
# de escrita, quem define eh a classe base 
class Usuario:

    def __init__(self, repositorio: Type[MySqlRepositorio]) -> None:

        self.__repositorio = repositorio


    def armazenar_dados(self, dado: any)  -> None:
        self.__repositorio.inserir(dado)

    def remover_dado(self, dado: any) -> None:
        self.__repositorio.deletar(dado)



if __name__ == '__main__':
    # injecao do objeto MySqlRepositorio() dentro do objeto usuario
    # vai herdar as funcoes da classe
    usuario = Usuario(MySqlRepositorio())
    usuario.armazenar_dados(23)

'''
Vamos analisar o problema aqui 
Se meu chefe vem e pede para nao utilizar mais MySql, e sim Mongo
Entao, minha camada de negocio, ta explicitamente dependendo diretamente do MySql, 
e eu preciso criar uma maneira que dependa apenas de uma maneira abstrata de banco de dados




'''