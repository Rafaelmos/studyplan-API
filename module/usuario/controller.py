from flask import Flask
from flask import Blueprint

app_usuario = Blueprint("app_usuario", __name__)
app_name = "usuario"

# Rota para listar todos os usuarios
@app_usuario.route('/{}s/'.format(app_name))
def getAll_Usuarios():
  return 'Todos os Usuarios cadastrados'


# Rota para listar apenas um usuario
@app_usuario.route('/{}/nome/'.format(app_name))
def get_Usuario():
  return 'Um unico usuario'


# Rota para adicionaar novos usuarios
@app_usuario.route('/{}/adicionar/'.format(app_name))
def new_Usuario():
  return 'Novo Usuario'


# Rota para deletar algum usuario
@app_usuario.route('/{}/delete/'.format(app_name))
def delete_Usuario():
  return 'Deletando Usuario'
