class Estado:
    def __init__(self, id, nome, sigla, bandeira):
        self.__id = id
        self.__nome = nome
        self.__sigla = sigla
        self.__bandeira = bandeira

    def get__id(self):
        return self.__id

    def get__nome(self):
        return self.__nome

    def get__sigla(self):
        return self.__sigla

    def get__bandeira(self):
        return self.__bandeira