import psycopg2

from module.metas.dao import SCRIPT_SQL_UPDATE_METAS

SCRIPT_SQL_INSERT = 'INSERT INTO MATERIAS(materia, area, usuario_id) values(%s, %s, %s) returning id'
SCRIPT_SQL_SELECT_ALL_MATERIAS = 'SELECT * FROM MATERIAS'
SCRIPT_SQL_DELETE_ID = 'DELETE FROM MATERIAS WHERE id = {}'
SCRIPT_SQL_SELECT_MATERIA_BY_ID = 'SELECT * FROM materias WHERE usuario_id = {}'
SCRIPT_SQL_UPDATE_MATERIA = """UPDATE Materias SET materia = '{}', area = '{}', usuario_id = {} WHERE id = {}"""

class MateriaDao:
  def __init__(self, connectDataBase):
    self.connectDataBase = connectDataBase

  def save_Materia(self, materia):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_INSERT, materia.get_values_saves_materia())
    id = cursor.fetchone()[0]
    self.connectDataBase.connect.commit()
    cursor.close()
    materia.set_id(id)

    return materia

  def getAll_Materias(self):
    metas = []
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_SELECT_ALL_MATERIAS)
    columns_name = [column[0] for column in cursor.description]
    meta_cursor = cursor.fetchone()
    while meta_cursor:
      meta = dict(zip(columns_name, meta_cursor))
      meta_cursor = cursor.fetchone()
      metas.append(meta)
    cursor.close()
    return metas

  def get_materias_by_id(self, usuario_id):
    materias = []
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_SELECT_MATERIA_BY_ID.format(usuario_id))
    columns_name = [column[0] for column in cursor.description]
    materia_cursor = cursor.fetchone()
    while materia_cursor:
      materia = dict(zip(columns_name, materia_cursor))
      materia_cursor = cursor.fetchone()
      materias.append(materia)
    cursor.close()
    return materias

  def delete_materia(self, id):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_DELETE_ID.format(id))
    self.connectDataBase.connect.commit()
    cursor.close()

  def update_materia(self, materia_update, id):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_UPDATE_MATERIA.format(materia_update.get_values_saves_materia()[0], materia_update.get_values_saves_materia()[1], materia_update.get_values_saves_materia()[2], id))
    self.connectDataBase.connect.commit()
    cursor.close()

