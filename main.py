import string
from flask import Flask

##from connect.bdutil import ConnectBD
##from module.curso.dao import CursoDao

##app = Flask('')

'''
@app.route("/usuario/")
def get_all_user():
    user_dao = UserDao(ConnectBD().get_connect())
    lista_user = user_dao.get_all()
    return {
            'status': True,
            'objects': [curso.get_json() for curso in lista_cursos]
        }

@app.route("/curso/<int:id>/")
def get_curso(id):
    curso_dao = CursoDao(ConnectBD().get_connect())
    curso = curso_dao.get_curso(id)
    if curso:
        return curso.get_json()
    return {}
'''
app = Flask(__name__)

@app.route("/")
def get_user():
  return "Hello world"

app.run()