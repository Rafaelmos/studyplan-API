import psycopg2

SCRIPT_SQL_INSERT = 'INSERT INTO LINKSUTEIS(titulo, link, usuario_id) values(%s, %s, %s) returning id'
SCRIPT_SQL_SELECT_ALL_LINKS = 'SELECT * FROM LINKSUTEIS'

class LinksDao:
  def __init__(self, connectDataBase):
    self.connectDataBase = connectDataBase

  def save_Links(self, Links):
    cursor = self.connectDataBase.connect.cursor()
    cursor.execute(SCRIPT_SQL_INSERT, Links.get_values_save_links())
    id = cursor.fetchone()[0]
    self.connectDataBase.connect.commit()
    cursor.close()
    Links.set_id(id)

    return Links

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