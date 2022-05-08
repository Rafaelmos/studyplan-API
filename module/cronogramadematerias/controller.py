from flask import Blueprint, request, jsonify, make_response
from connect.bdutil import ConnectDataBase

import traceback

from module.cronogramadematerias.model import Cronogramadematerias
from module.cronogramadematerias.dao import CronogramaDao

dao = CronogramaDao(connectDataBase=ConnectDataBase())

app_cronogramas = Blueprint("app_cronogramas", __name__)
app_name = "cronogramas"

@app_cronogramas.route('/{}/'.format(app_name), methods=['GET'])
def getAll_cronogramas():
  cronogramas = dao.getAll_cronogramas()

  return make_response(jsonify(cronogramas), 200)

@app_cronogramas.route('/{}/adicionar/'.format(app_name), methods=['POST'])
def add_cronogramas():
  data = request.form.to_dict(flat=True)
  cronograma = None

  try:
    cronograma = Cronogramadematerias(**data)
    cronograma = dao.save_cronograma(cronograma)
  except Exception as e:
    print(traceback.format_exc())
    return make_response(
      {
        'error': True,
        'mensagem': 'Verifique se todos os campos foram preenchidos corretamente'
      }, 400)
  return make_response({'id': cronograma.id}, 200)

@app_cronogramas.route('/{}/delete/<int:id>'.format(app_name), methods=['DELETE'])
def delete_cronograma(id):
  get_all_cronograma = dao.getAll_cronogramas()

  for cronograma in get_all_cronograma:
    if cronograma['id'] == id:
      dao.delete_cronograma(id)
      return make_response(
      { 
        'message' : 'Cronograma ' + cronograma['materia'] + ' Deletado' 
      }, 200)

  return make_response(
    {
      'error' : True,
      'message' : 'Erro, O Cronograma não foi encontrado'
    }, 400)