class Agendas:
  def __init__(self, usuario_id):
    self.usuario_id = usuario_id,
    self.id = None

  def set_id(self, id):
    self.id = id
  
  def __str__(self):
    return 'Usuario: {}'.format(self.usuario_id)
              
  def get_values_save_meta(self):
    return [self.usuario_id]