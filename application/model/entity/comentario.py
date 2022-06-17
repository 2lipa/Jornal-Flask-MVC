class Comentario:
    def __init__(self, usuario, comentario, email, like=None, dislike=None):
        self.__usuario = usuario
        self.__comentario = comentario
        self.__link = None
        self.__like = like
        self.__dislike = dislike
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def getLink(self):
        return self.__link

    def setLink(self, link):
        self.__link = link

    def setUsuario(self, usuario):
        self.__usuario = usuario

    def setComentario(self, comentario):
        self.__comentario = comentario

    def get_usuario(self):
        return self.__usuario

    def get_comentario(self):
        return self.__comentario

    def get_like(self):
        return self.__like

    def get_dislike(self):
        return self.__dislike