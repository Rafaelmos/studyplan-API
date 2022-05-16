import psycopg2

SCRIPT_SQL_INSERT = 'INSERT INTO LEMBRETES(nome, descricao, data, agenda_id, usuario_id) values(%s, %s, %s, %s, %s) returning id'
SCRIPT_SQL_SELECT_ALL_LEMBRETES = 'SELECT * FROM LEMBRETES'
SCRIPT_SQL_DELETE_ID = 'DELETE FROM LEMBRETES WHERE id = {}'
SCRIPT_SQUL_SELECT_LEMBRETES_BY_ID = 'SELECT * FROM lembretes WHERE usuario_id = {}'
SCRIPT_SQL_UPDATE_LEMBRTETES = """UPDATE lembretes SET nome = '{}', descricao = '{}', data = '{}', agenda_id = '{}', usuario_id = '{}'  WHERE id = {}"""


class LembreteDao:
  def __init__(self, connectDataBase):
    self.connectDataBase = connectDataBase

  def save_Lembrete(self, lembrete):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_INSERT, lembrete.get_values_save_lembrete())
    id = cursor.fetchone()[0]
    self.connectDataBase.connect.commit()
    cursor.close()
    lembrete.set_id(id)

    return lembrete

  def getAll_lembretes(self):
    lembretes = []
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_SELECT_ALL_LEMBRETES)
    columns_name = [column[0] for column in cursor.description]
    lembrete_cursor = cursor.fetchone()
    while lembrete_cursor:
      lembrete = dict(zip(columns_name, lembrete_cursor))
      lembrete_cursor = cursor.fetchone()
      lembretes.append(lembrete)
    cursor.close()
    return lembretes

  def get_lembretes_by_id(self, usuario_id):
    lembretes = []
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQUL_SELECT_LEMBRETES_BY_ID.format(usuario_id))
    columns_name = [column[0] for column in cursor.description]
    lembrete_cursor = cursor.fetchone()
    while lembrete_cursor:
      lembrete = dict(zip(columns_name, lembrete_cursor))
      lembrete_cursor = cursor.fetchone()
      lembretes.append(lembrete)
    cursor.close()
    return lembretes

  def delete_lembrete(self, id):
      cursor = self.connectDataBase.connect.cursor()
      cursor.execute(SCRIPT_SQL_DELETE_ID.format(id))
      self.connectDataBase.connect.commit()
      cursor.close()

  def update_lembrete(self, lembrete_update, id):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_UPDATE_LEMBRTETES.format(lembrete_update.get_values_save_lembrete()[0], lembrete_update.get_values_save_lembrete()[1], lembrete_update.get_values_save_lembrete()[2], lembrete_update.get_values_save_lembrete()[3], lembrete_update.get_values_save_lembrete()[4], id))
    self.connectDataBase.connect.commit()
    cursor.close()