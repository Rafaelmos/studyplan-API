from flask import Blueprint, jsonify, request, make_response, Response
from connect.bdutil import ConnectDataBase

from module.usuario.dao import UsuarioDao
from module.usuario.model import Usuario

import traceback

app_usuario = Blueprint("app_usuario", __name__)
app_name = "usuario"

dao = UsuarioDao(connectDataBase=ConnectDataBase())

# Rota para listar todos os usuarios
@app_usuario.route('/{}s/'.format(app_name))
def getAll_Usuarios():
  return 'Todos os Usuarios cadastrados'


# Rota para listar apenas um usuario
@app_usuario.route('/{}/nome/'.format(app_name))
def get_Usuario():
  return 'Um unico usuario'


# Rota para adicionaar novos usuarios
@app_usuario.route('/{}/adicionar/'.format(app_name), methods=['POST'])
def add_Usuario():
  data = request.form.to_dict(flat=True)
  usuario = None
  try:
    usuario = Usuario(**data)
    usuario = dao.save(usuario)
  except Exception as e:
    print(traceback.format_exc())
    return make_response(
      {
        'error': True,
        'message': 'Verifique se os campos foram preenchidos corretamente'
      }, 400)

  return make_response({'id': usuario.id}, 201)

# Rota para deletar algum usuario
@app_usuario.route('/{}/delete/'.format(app_name))
def delete_Usuario():
  return 'Deletando Usuario'
