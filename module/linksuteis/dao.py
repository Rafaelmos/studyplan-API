import psycopg2

SCRIPT_SQL_INSERT = 'INSERT INTO LINKSUTEIS(titulo, link, usuario_id) values(%s, %s, %s) returning id'
SCRIPT_SQL_SELECT_ALL_LINKS = 'SELECT * FROM LINKSUTEIS'
SCRIPT_SQL_DELETE_ID = 'DELETE FROM LINKSUTEIS WHERE id = {}'
SCRIPT_SQL_UPDATE_LINK = """UPDATE linksuteis SET titulo = '{}', link = '{}', usuario_id = {} WHERE id = {}"""

class LinksDao:
  def __init__(self, connectDataBase):
    self.connectDataBase = connectDataBase

  def save_Links(self, link):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_INSERT, link.get_values_saves())
    id = cursor.fetchone()[0]
    self.connectDataBase.connect.commit()
    cursor.close()
    link.set_id(id)

    return link

  def getAll_links(self):
    links = []
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_SELECT_ALL_LINKS)
    columns_name = [column[0] for column in cursor.description]
    link_cursor = cursor.fetchone()
    while link_cursor:
      link = dict(zip(columns_name, link_cursor))
      link_cursor = cursor.fetchone()
      links.append(link)
    cursor.close()

    return links

  def update_link(self, link_update, id):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_UPDATE_LINK.format(link_update.get_values_saves()[0], link_update.get_values_saves()[1], link_update.get_values_saves()[2], id))
    self.connectDataBase.connect.commit()
    cursor.close()

  def delete_link(self, id):
      cursor = self.connectDataBase.connect.cursor()
      cursor.execute(SCRIPT_SQL_DELETE_ID.format(id))
      self.connectDataBase.connect.commit()
      cursor.close()