from flask import render_template
from application import app
from application.model.dao.noticia_dao import NoticiaDao
from application.model.dao.estado_dao import EstadoDao


noticiadao = NoticiaDao()
estadodao = EstadoDao()

@app.route('/', methods=['GET'])
def index():
    return render_template("principal.html", noticia=noticiadao.listar_noticia(), estados=estadodao.listar_estado(), noticia2=noticiadao.randomizar1(), noticia3=noticiadao.randomizar2(), noticia4=noticiadao.randomizar3())