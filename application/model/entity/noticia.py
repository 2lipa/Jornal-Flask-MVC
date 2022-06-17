class Noticia:

    def __init__(self, id, titulo, descricao, texto, foto, estado, data, curtida=None):
        self.__id = id
        self.__titulo = titulo
        self.__descricao = descricao
        self.__texto = texto
        self.__foto = foto
        self.__estado = estado
        self.__data = data
        self.__curtida = curtida


    def get_id(self):
        return self.__id

    def get__titulo(self):
        return self.__titulo

    def get__descricao(self):
        return self.__descricao

    def get__texto(self):
        return self.__texto

    def get__foto(self):
        return self.__foto

    def get__estado(self):
        return self.__estado

    def get__data(self):
        return self.__data

    def get__curtida(self):
        return self.__curtida

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setComentario(self, comentario):
        self.comentario = comentario
