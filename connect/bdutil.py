import psycopg2

class ConnectBD:

  _instace = None

  # Método para se conectar no Banco do Postgres, utilizando a biblioteca Psycopg2.
  def __init__(self):
    self._connect = psycopg2.connect(
      host="localhost",
      database="studyplan",
      user="postgres",
      password="Lu274235Ely5"
    )

  # Utilizado o classMethod para ser possível criar um atributo metodo da classe
  # Para não criar várias instancias do mesmo Objeto quando se for fazer uma conexão no banco
  @classmethod
  def get_connect(cls):
    if cls._instace is None:
      cls._instace = super().__new__(cls)
    
    return cls._instace
  
  '''
  # Outra forma de fazer o Singleton - Sobreescrevendo o método __new__()
  def __new__(cls, *args, **kwargs):
    if cls._instace is None:
      cls._instace = super().__new__(cls)
    
    return cls._instace
  '''
