from flask import Blueprint, request, jsonify, make_response
from connect.bdutil import ConnectDataBase

import traceback

from module.materias.model import Materias
from module.materias.dao import MateriaDao

dao = MateriaDao(connectDataBase=ConnectDataBase())

app_materias = Blueprint("app_materias", __name__)
app_name = "materias"


@app_materias.route(f'/{app_name}/', methods=["GET"])
def getAll_materias():
    materias = dao.getAll_Materias()

    return make_response(jsonify(materias), 200)

@app_materias.route(f'/{app_name}/adicionar/', methods=['POST'])
def add_materia():
    data = request.form.to_dict(flat=True)
    materia = None
    try:
        materia = Materias(**data)
        materia = dao.save_Materia(materia)
    except Exception as e:
        print(traceback.format_exc())
        return make_response(
            {
                'error': True,
                'mensagem': 'Verifique se todos os campos foram preenchidos corretamente'
            }, 400)
    return make_response({'id': materia.id}, 200)

@app_materias.route('/{}/delete/<int:id>'.format(app_name), methods=['DELETE'])
def delete_materia(id):
  get_all_materias = dao.getAll_Materias()

  for materia in get_all_materias:
    if materia['id'] == id:
      dao.delete_materia(id)
      return make_response(
      { 
        'message' : 'Materia ' + materia['materia'] + ' Deletado' 
      }, 200)

  return make_response(
    {
      'error' : True,
      'message' : 'Erro, A materia não foi encontrada'
    }, 400)    


@app_materias.route('/{}/atualizar/<int:id>'.format(app_name), methods=['PUT'])
def update_metas(id):
  data = request.form.to_dict(flat=True)
  get_all_materias = dao.getAll_Materias()
  
  try:
    materia_update = Materias(**data)
    for meta in get_all_materias:
      if meta['id'] == id:
        dao.update_materia(materia_update, id)
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