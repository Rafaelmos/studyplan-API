from flask import Blueprint, jsonify, make_response,request
from connect.bdutil import ConnectDataBase

from module.agenda.model import Agendas
from module.agenda.dao import AgendaDao

import traceback

dao = AgendaDao(connectDataBase=ConnectDataBase())

app_agenda = Blueprint("app_agenda", __name__)
app_name = "agenda"

@app_agenda.route('/{}/'.format(app_name))
def getAll_agendas():
  agendas = dao.getAll_agendas()
  return make_response(jsonify(agendas), 200)

@app_agenda.route('/{}/adicionar/'.format(app_name), methods=['POST'])
def add_agenda():
  data = request.form.to_dict(flat=True)
  agenda = None

  try:
    agenda = Agendas(**data)
    agenda = dao.save_Agenda(agenda)
  except Exception as e:
    print(traceback.format_exc())
    return make_response(
      {
        'error': True,
        'mensagem': 'Verifique se todos os campos foram preenchidos corretamente'
      }, 400)
  return make_response({'id': agenda.id}, 200)
  

@app_agenda.route('/{}/<int:id>'.format(app_name))
def getAll_by_agenda_id(id):
  agenda = dao.getAll_by_agenda_id(id)
  return make_response(jsonify(agenda), 200)
