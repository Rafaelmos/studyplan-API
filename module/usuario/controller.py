from flask import Blueprint, jsonify, request, make_response, Response
from connect.bdutil import ConnectDataBase

from module.usuario.dao import UsuarioDao
from module.usuario.model import Usuario

from module.agenda.dao import AgendaDao
from module.agenda.model import Agendas

import traceback

app_usuario = Blueprint("app_usuario", __name__)
app_name = "usuario"

dao = UsuarioDao(connectDataBase=ConnectDataBase())
daoAgenda = AgendaDao(connectDataBase=ConnectDataBase())

# Rota para listar todos os usuarios
@app_usuario.route('/{}s/'.format(app_name), methods=['GET'])
def getAll_Usuarios():
  usuarios = dao.get_allUsers()

  return make_response(jsonify(usuarios), 200)


# Rota para listar apenas um usuario: Pesquisando pelo nome
@app_usuario.route('/{}/<string:nome>'.format(app_name), methods=['GET'])
def get_usuario_for_name(nome):
  usuarios = dao.get_allUsers()
  for usuario in usuarios:
    if usuario['nome'] == nome:
      return make_response(jsonify(usuario), 200)

  return make_response(
    {
      'error': True,
      'message': 'Usuario não encontrado'
    }, 404)

# Rota para listar apenas um usuario: Pesquisando por um ID
@app_usuario.route('/{}/<int:id>'.format(app_name), methods=['GET'])
def get_usuario_by_id(id):
  usuarios = dao.get_allUsers()

  for usuario in usuarios:
    if usuario['id'] == id:
      return make_response(jsonify(usuario), 200)

  return make_response(
    {
      'error': True,
      'message': 'Usuario foi encontrado'
    }, 404)

# Rota para adicionaar novos usuarios
@app_usuario.route('/{}/adicionar/'.format(app_name), methods=['POST'])
def add_Usuario():
  data = request.form.to_dict(flat=True)
  usuario = None
  agenda = None
  
  try:
    usuario = Usuario(**data)
    usuario = dao.save(usuario)

    agenda = Agendas(usuario.id)
    agenda = daoAgenda.save_Agenda(agenda)
    
  except Exception as e:
    print(traceback.format_exc())
    return make_response(
      {
        'error': True,
        'message': 'Verifique se os campos foram preenchidos corretamente'
      }, 400)

  return make_response({'id': usuario.id}, 201)

# Rota para Atualizar dados de um usuario
@app_usuario.route('/{}/atualizar/<int:id>'.format(app_name), methods=['PUT'])
def update_usuario(id):
  data = request.form.to_dict(flat=True)
  get_all_usuarios = dao.get_allUsers()
  
  try:
    usuario_update = Usuario(**data)
    for usuario in get_all_usuarios:
      if usuario['id'] == id:
        dao.update_user(usuario_update, id)
        return make_response({'message' : 'Dados Atualizados'}, 200)
    
    return make_response(
      {
        'error' : True,
        'message' : 'Error, Usuário não encontrado'
      }, 404)
  
  except Exception as e:
    print(traceback.format_exc())
    return make_response(
      {
        'error' : True,
        'message' : 'Erro, Verifique se os campos foram preenchidos corretamente'
      }, 400)

# Rota para deletar algum usuario
@app_usuario.route('/{}/delete/<int:id>'.format(app_name), methods=['DELETE'])
def delete_Usuario(id):
  get_all_usuarios = dao.get_allUsers()

  for usuario in get_all_usuarios:
    if usuario['id'] == id:
      dao.delete_user(id)
      return make_response(
      { 
        'message' : 'Usuario ' + usuario['nome'] + ' Deletado' 
      }, 200)

  return make_response(
    {
      'error' : True,
      'message' : 'Erro, O usuario não foi encontrado'
    }, 400)
