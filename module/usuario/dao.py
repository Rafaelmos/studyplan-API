import psycopg2

SCRIPT_SQL_INSERT = 'INSERT INTO usuario(nome, senha, idade) values(%s, %s, %s) returning id'
SCRIPT_SQL_SELECT_ALL = 'SELECT * FROM usuario'
SCRIPT_SQL_UPDATE_USER = """UPDATE usuario SET nome = '{}', senha = '{}', idade = {} WHERE id = {}"""
SCRIPT_SQL_DELETE_ID = 'DELETE FROM usuario WHERE id = {}'

#SCRIP_SQL_SELECT_ULTIMO_ID = 'SELECT id FROM USUARIO ORDER BY id DESC LIMIT 1'

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

  def update_user(self, usuario_update, id):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_UPDATE_USER.format(usuario_update.get_values_save()[0], usuario_update.get_values_save()[1], usuario_update.get_values_save()[2], id))
    self.connectDataBase.connect.commit()
    cursor.close()

  def delete_user(self, id):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_DELETE_ID.format(id))
    self.connectDataBase.connect.commit()
    cursor.close()