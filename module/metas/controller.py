from flask import Blueprint, request, jsonify, make_response
from connect.bdutil import ConnectDataBase

import traceback

from module.metas.model import Metas
from module.metas.dao import MetaDao

dao = MetaDao(connectDataBase=ConnectDataBase())

app_metas = Blueprint("app_metas", __name__)
app_name = "metas"

@app_metas.route('/{}/'.format(app_name), methods=['GET'])
def getAll_metas():
  metas = dao.getAll_metas()

  return make_response(jsonify(metas), 200)

@app_metas.route('/{}/adicionar/'.format(app_name), methods=['POST'])
def add_meta():
  data = request.form.to_dict(flat=True)
  meta = None

  try:
    meta = Metas(**data)
    meta = dao.save_Meta(meta)
  except Exception as e:
    print(traceback.format_exc())
    return make_response(
      {
        'error': True,
        'mensagem': 'Verifique se todos os campos foram preenchidos corretamente'
      }, 400)
  return make_response({'id': meta.id}, 200)

@app_metas.route('/{}/delete/<int:id>'.format(app_name), methods=['DELETE'])
def delete_meta(id):
  get_all_metas = dao.getAll_metas()

  for meta in get_all_metas:
    if meta['id'] == id:
      dao.delete_meta(id)
      return make_response(
      { 
        'message' : 'Meta ' + meta['nome'] + ' Deletado' 
      }, 200)

  return make_response(
    {
      'error' : True,
      'message' : 'Erro, A meta não foi encontrada'
    }, 400)