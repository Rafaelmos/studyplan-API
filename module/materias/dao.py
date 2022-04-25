import psycopg2

SCRIPT_SQL_INSERT = 'INSERT INTO MATERIAS(materia, area) values(%s, %s) returning id'
SCRIPT_SQL_SELECT_ALL_MATERIAS = 'SELECT * FROM MATERIAS'


class MateriaDao:
    def __init__(self, connectDataBase):
        self.connectDataBase = connectDataBase

    def save_Materia(self, materia):
        cursor = self.connectDataBase.connect.cursor()
        cursor.execute(SCRIPT_SQL_INSERT, materia.get_values_save_meta())
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
        

