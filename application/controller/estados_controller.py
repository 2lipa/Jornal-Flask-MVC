from flask import render_template
from application import app
from application.model.dao.noticia_dao import NoticiaDao
from application.model.dao.estado_dao import EstadoDao

noticiadao = NoticiaDao()
estadodao = EstadoDao()

@app.route("/estados/<id>")
def estados(id):
    return render_template("estados.html", estado=estadodao.listar_estado_id(id), estados=estadodao.listar_estado(), noticia=noticiadao.listar_noticia())
