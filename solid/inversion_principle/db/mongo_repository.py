from .interface import Repositorio

# aqui posso implementar como seria o deletar no MySql
class MongoDBRepositorio(Repositorio):


    def inserir(self, dado: any) -> None:
        print('Inserindo {} no banco MongoDB'.format(dado))

    def deletar(self, dado: any) -> None:
        print('Deletando {} do banco MongoDB'.format(dado))

    # def __privado(self, dado) -> None:
    #     pass