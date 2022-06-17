from os import link
from flask import redirect, render_template, request
from application import app
from application.model.dao.noticia_dao import NoticiaDao, ComentarioDao
from application.model.entity.comentario import Comentario
from application.model.dao.estado_dao import EstadoDao
from application.model.entity.noticia import Noticia

noticiadao = NoticiaDao()
estadodao = EstadoDao()
comentariodao = ComentarioDao()

@app.route("/noticia/<id>", methods=["GET"])
def exibir_noticia(id):
    segundaNoticia = noticiadao.segunda_noticia()
    while segundaNoticia == id:
        segundaNoticia = noticiadao.segunda_noticia()
    return render_template("noticia.html", noticia=noticiadao.noticia_id(id), estados=estadodao.listar_estado(), noticia2=noticiadao.segunda_noticia(), comentarios=comentariodao.lista_comentario())


@app.route("/salvar/<id>", methods=["POST", 'GET'])
def salvar(id):
    usuario = request.form.get("usuario")
    texto = request.form.get("comentario")
    email = request.form.get("email")
    link = noticiadao.noticia_id(id)
    avaliacao = Comentario(usuario, texto, email)
    comentariodao.inserir(avaliacao, link)
    return redirect("/noticia/" + id)
