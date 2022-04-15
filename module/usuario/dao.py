import psycopg2

SCRIPT_SQL_INSERT = 'INSERT INTO USUARIO(nome, senha, idade) values(%s, %s, %s) returning id'

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
  