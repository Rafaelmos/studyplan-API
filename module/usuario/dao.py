import psycopg2

SCRIPT_SQL_INSERT = 'INSERT INTO USUARIO(nome, senha, idade) values(%s, %s, %s) returning id'
SCRIPT_SQL_SELECT_ALL = 'SELECT * FROM USUARIO'
#SCRIPT_SQL_SELECT_USER = 'SELECT id, nome, senha, idade FROM USUARIO WHERE id = {}'
SCRIPT_SQL_DELETE_ID = 'DELETE FROM USUARIO WHERE id={}'

class UsuarioDao:
  def __init__(self, connectDataBase):
    self.connectDataBase = connectDataBase

  def save(self, usuario):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_INSERT, usuario.get_values_save())
    id = cursor.fetchone()[0]
    self.connectDataBase.connect.commit()
    cursor.close()
    usuario.set_id(id)
    return usuario
  

  def get_allUsers(self):
    usuarios = []
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_SELECT_ALL)
    columns_name = [column[0] for column in cursor.description]
    usuario_cursor = cursor.fetchone()
    while usuario_cursor:
      usuario = dict(zip(columns_name, usuario_cursor))
      usuario_cursor = cursor.fetchone()
      usuarios.append(usuario)
    cursor.close()
    return usuarios
"""
  def delete_user(self, id):
    cursor = self.database.connect.cursor()
    cursor.execute(SCRIPT_SQL_DELETE_ID.format(id))
    cursor.close()
    return self.get_allUsers

"""
''' Não foi necessário utilizar essa função

  def get_user_id(self, id):
    date_usuario = []
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_SELECT_USER.format(id))
    self.connectDataBase.connect.commit()
    columns_name = [column[0] for column in cursor.description]
    usuario_cursor = cursor.fetchone()
    while usuario_cursor:
      usuario = dict(zip(columns_name, usuario_cursor))
      usuario_cursor = cursor.fetchone()
      date_usuario.append(usuario)
    cursor.close()
    return date_usuario
'''