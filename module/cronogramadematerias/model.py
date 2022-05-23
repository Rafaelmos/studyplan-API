class Cronogramadematerias:
  def __init__(self, descricao, data, agenda_id, usuario_id, materia_id):
    self.descricao = descricao
    self.data = data
    self.agenda_id = agenda_id
    self.usuario_id = usuario_id
    self.materia_id = materia_id
    self.id = None

  def set_id(self, id):
    self.id = id
  
  def __str__(self):
    return 'Descrição: {} - Data: {} - Agenda: {} - Usuario: {} - Materia: {}'.format(self.descricao, self.data, self.agenda_id, self.usuario_id, self.materia_id)
              
  def get_values_save_cronograma(self):
    return [self.descricao, self.data, self.agenda_id, self.usuario_id, self.materia_id]