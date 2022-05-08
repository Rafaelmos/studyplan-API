import psycopg2

SCRIPT_SQL_INSERT = 'INSERT INTO CRONOGRAMADEMATERIAS(descricao, data, agenda_id, usuario_id, materia_id) values(%s, %s, %s, %s, %s) returning id'
SCRIPT_SQL_SELECT_ALL_CRONOGRAMAS = 'SELECT * FROM CRONOGRAMADEMATERIAS'
SCRIPT_SQL_DELETE_ID = 'DELETE FROM CRONOGRAMADEMATERIAS WHERE id = {}'


class CronogramaDao:
  def __init__(self, connectDataBase):
    self.connectDataBase = connectDataBase

  def save_cronograma(self, cronograma):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_INSERT, cronograma.get_values_save_cronograma())
    id = cursor.fetchone()[0]
    self.connectDataBase.connect.commit()
    cursor.close()
    cronograma.set_id(id)

    return cronograma

  def getAll_cronogramas(self):
    cronogramas = []
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_SELECT_ALL_CRONOGRAMAS)
    columns_name = [column[0] for column in cursor.description]
    cronograma_cursor = cursor.fetchone()
    while cronograma_cursor:
      cronograma = dict(zip(columns_name, cronograma_cursor))
      cronograma_cursor = cursor.fetchone()
      cronogramas.append(cronograma)
    cursor.close()

    return cronogramas

  def delete_cronograma(self, id):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_DELETE_ID.format(id))
    self.connectDataBase.connect.commit()
    cursor.close()