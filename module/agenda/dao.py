import psycopg2

SCRIPT_SQL_INSERT = 'INSERT INTO AGENDA(usuario_id) values(%s) returning id'
SCRIPT_SQL_SELECT_ALL_AGENDAS = 'SELECT * FROM AGENDAS'
#SELECT * FROM  cronogramadematerias as z WHERE z.agenda_id= 1
#SELECT * FROM  metas as x WHERE x.agenda_id= 1
#SELECT * FROM  lembretes as y WHERE y.agenda_id= 1

class AgendaDao:
  def __init__(self, connectDataBase):
    self.connectDataBase = connectDataBase

  def save_Agenda(self, Agenda):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_INSERT, Agenda.get_values_save_agenda())
    id = cursor.fetchone()[0]
    self.connectDataBase.connect.commit()
    cursor.close()
    Agenda.set_id(id)

    return Agenda

  def getAll_agendas(self):
    agendas = []
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_SELECT_ALL_AGENDAS)
    columns_name = [column[0] for column in cursor.description]
    agenda_cursor = cursor.fetchone()
    while agenda_cursor:
      agenda = dict(zip(columns_name, agenda_cursor))
      agenda_cursor = cursor.fetchone()
      agendas.append(agenda)
    cursor.close()

    return agendas