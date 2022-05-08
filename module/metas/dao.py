import psycopg2

SCRIPT_SQL_INSERT = 'INSERT INTO METAS(nome, descricao, status,prazo, agenda_id, usuario_id) values(%s, %s, %s, %s, %s,%s) returning id'
SCRIPT_SQL_SELECT_ALL_METAS = 'SELECT * FROM METAS'
SCRIPT_SQL_DELETE_ID = 'DELETE FROM METAS WHERE id = {}'
SCRIPT_SQL_SELECT_METAS_BY_ID = 'SELECT * FROM metas WHERE usuario_id = {}'
SCRIPT_SQL_UPDATE_METAS = """UPDATE metas SET nome = '{}', descricao = '{}', status = {}, prazo = '{}', agenda_id = {}, usuario_id = {}  WHERE id = {}"""


class MetaDao:
  def __init__(self, connectDataBase):
    self.connectDataBase = connectDataBase

  def save_Meta(self, Meta):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_INSERT, Meta.get_values_save_meta())
    id = cursor.fetchone()[0]
    self.connectDataBase.connect.commit()
    cursor.close()
    Meta.set_id(id)

    return Meta

  def getAll_metas(self):
    metas = []
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_SELECT_ALL_METAS)
    columns_name = [column[0] for column in cursor.description]
    meta_cursor = cursor.fetchone()
    while meta_cursor:
      meta = dict(zip(columns_name, meta_cursor))
      meta_cursor = cursor.fetchone()
      metas.append(meta)
    cursor.close()

    return metas

  def get_meta_by_id(self, usuario_id):
    metas = []
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_SELECT_METAS_BY_ID.format(usuario_id))
    columns_name = [column[0] for column in cursor.description]
    meta_cursor = cursor.fetchone()
    while meta_cursor:
      meta = dict(zip(columns_name, meta_cursor))
      meta_cursor = cursor.fetchone()
      metas.append(meta)
    cursor.close()
    return metas

  def delete_meta(self, id):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_DELETE_ID.format(id))
    self.connectDataBase.connect.commit()
    cursor.close()


  def update_meta(self, meta_update, id):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_UPDATE_METAS.format(meta_update.get_values_save_meta()[0], meta_update.get_values_save_meta()[1], meta_update.get_values_save_meta()[2], meta_update.get_values_save_meta()[3], meta_update.get_values_save_meta()[4], meta_update.get_values_save_meta()[5], id))
    self.connectDataBase.connect.commit()
    cursor.close()