from .interface import Repositorio


# aqui posso implementar como seria o deletar no MySql
class MySqlRepositorio(Repositorio):

    def inserir(self, dado: any) -> None:
        print('Inserindo {} no banco MySql'.format(dado))

    def deletar(self, dado: any) -> None:
        print('Deletando {} do banco MySql'.format(dado))

    # dessa forma, se aqui, eu quiser criar alguma classe especifica par ao mySql e que nao esta presente no 
    # mongoDB, logo nao aparecera na interface, que eh o que ta sendo chamado la no usuario