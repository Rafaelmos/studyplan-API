from flask import Blueprint, request, jsonify, make_response
from connect.bdutil import ConnectDataBase

import traceback

from module.linksuteis.model import Linksuteis
from module.linksuteis.dao import LinksDao

dao = LinksDao(connectDataBase=ConnectDataBase())

app_links = Blueprint("app_links", __name__)
app_name = "links"

@app_links.route('/{}/'.format(app_name), methods=['GET'])
def getAll_links():
  links = dao.getAll_links()

  return make_response(jsonify(links), 200)

@app_links.route('/{}/adicionar/'.format(app_name), methods=['POST'])
def add_link():
  data = request.form.to_dict(flat=True)
  link = None

  try:
    link = Linksuteis(**data)
    link = dao.save_Links(link)
  except Exception as e:
    print(traceback.format_exc())
    return make_response(
      {
        'error': True,
        'mensagem': 'Verifique se todos os campos foram preenchidos corretamente'
      }, 400)
  return make_response({'id': link.id}, 200)

@app_links.route('/{}/atualizar/<int:id>'.format(app_name), methods=['PUT'])
def update_link(id):
  data = request.form.to_dict(flat=True)
  get_all_links = dao.getAll_links()

  try:
    link_update = Linksuteis(**data)
    for link in get_all_links:
      if link['id'] == id:
        dao.update_link(link_update, id)
        return make_response({'message' : 'Dados Atualizados'}, 200)
    return make_response(
      {
        'error' : True,
        'message' : 'Error, Link não encontrado'
      }, 404)

  except Exception as e:
    print(traceback.format_exc())
    return make_response(
      {
        'error' : True,
        'message' : 'Erro, Verifique se os campos foram preenchidos corretamente'
      }, 400)

@app_links.route('/{}/delete/<int:id>'.format(app_name), methods=['DELETE'])
def delete_Link(id):
  get_all_links = dao.getAll_links()

  for link in get_all_links:
    if link['id'] == id:
      dao.delete_link(id)
      return make_response(
      { 
        'message' : 'LinkUtil ' + link['nome'] + ' Deletado' 
      }, 200)

  return make_response(
    {
      'error' : True,
      'message' : 'Erro, O LinkUtil não foi encontrado'
    }, 400)