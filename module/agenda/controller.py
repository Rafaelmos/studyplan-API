from flask import Blueprint
from connect.bdutil import ConnectDataBase

app_agenda = Blueprint("app_agenda", __name__)
app_name = "agenda"

@app_agenda.route('/{}/'.format(app_name))
def get_agenda():
  return 'Todas as agendas'
#dao = UsuarioDao(connectDataBase=ConnectDataBase())
