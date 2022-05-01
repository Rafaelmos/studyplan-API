import psycopg2


SCRIPT_SQL_INSERT = 'INSERT INTO AGENDA(usuario_id) values(%s) returning id'
SCRIPT_SQL_SELECT_ALL_AGENDAS = 'SELECT * FROM AGENDA'
SCRIPT_SQL_SELECT_LEMBRETES_BY_AGENDA_ID = 'SELECT * FROM  lembretes as y WHERE y.agenda_id= {}'
SCRIPT_SQL_SELECT_METAS_BY_AGENDA_ID =  'SELECT * FROM  metas as x WHERE x.agenda_id= {}'
SCRIPT_SQL_SELECT_CRONOGRAMA_BY_AGENDA_ID = 'SELECT * FROM  cronogramadematerias as z WHERE z.agenda_id= {}'


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
    return agenda
    
  def getAll_by_agenda_id(self,id):
    agendabyid = []
    agendabyid.append('LEMBRETES')
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_SELECT_LEMBRETES_BY_AGENDA_ID.format(id))
    columns_name = [column[0] for column in cursor.description]
    agenda_cursor = cursor.fetchone()
    while agenda_cursor:
      agenda = dict(zip(columns_name, agenda_cursor))
      agenda_cursor = cursor.fetchone()
      agendabyid.append(agenda)
    agendabyid.append('METAS')
    cursor.execute(SCRIPT_SQL_SELECT_METAS_BY_AGENDA_ID.format(id))
    columns_name = [column[0] for column in cursor.description]
    agenda_cursor = cursor.fetchone()
    while agenda_cursor:
      agenda = dict(zip(columns_name, agenda_cursor))
      agenda_cursor = cursor.fetchone()
      agendabyid.append(agenda)
    agendabyid.append('CRONOGRAMA')
    cursor.execute(SCRIPT_SQL_SELECT_CRONOGRAMA_BY_AGENDA_ID.format(id))
    columns_name = [column[0] for column in cursor.description]
    agenda_cursor = cursor.fetchone()
    while agenda_cursor:
      agenda = dict(zip(columns_name, agenda_cursor))
      agenda_cursor = cursor.fetchone()
      agendabyid.append(agenda)
    cursor.close()
    return agendabyid
