from flask import Blueprint, request, jsonify, make_response
from connect.bdutil import ConnectDataBase

import traceback

from module.lembretes.model import Lembretes
from module.lembretes.dao import LembreteDao

dao = LembreteDao(connectDataBase=ConnectDataBase())

app_lembretes = Blueprint("app_lembretes", __name__)
app_name = "lembretes"

@app_lembretes.route('/{}/'.format(app_name), methods=['GET'])
def getAll_lembretes():
  lembretes = dao.getAll_lembretes()

  return make_response(jsonify(lembretes), 200)

@app_lembretes.route('/{}/<int:usuario_id>'.format(app_name), methods=['GET'])
def get_lembrete_by_id(usuario_id):
 
  lembretes_by_id = dao.get_lembretes_by_id(usuario_id)

  return make_response(jsonify(lembretes_by_id), 200)

@app_lembretes.route('/{}/adicionar/'.format(app_name), methods=['POST'])
def add_lembrete():
  data = request.form.to_dict(flat=True)
  lembrete = None

  try:
    lembrete = Lembretes(**data)
    lembrete = dao.save_Lembrete(lembrete)
  except Exception as e:
    print(traceback.format_exc())
    return make_response(
      {
        'error': True,
        'mensagem': 'Verifique se todos os campos foram preenchidos corretamente'
      }, 400)
  return make_response({'id': lembrete.id}, 200)

@app_lembretes.route('/{}/delete/<int:id>'.format(app_name), methods=['DELETE'])
def delete_lembrete(id):
  get_all_lembretes = dao.getAll_lembretes()

  for lembrete in get_all_lembretes:
    if lembrete['id'] == id:
      dao.delete_lembrete(id)
      return make_response(
      { 
        'message' : 'Lembrete ' + lembrete['nome'] + ' Deletado' 
      }, 200)

  return make_response(
    {
      'error' : True,
      'message' : 'Erro, O Lembrete não foi encontrado'
    }, 400)