class Lembretes:
  def __init__(self, nome, descricao, data, agenda_id, usuario_id):
    self.nome = nome
    self.descricao = descricao
    self.data = data
    self.agenda_id = agenda_id
    self.usuario_id = usuario_id
    self.id = None

  def set_id(self, id):
    self.id = id
  
  def __str__(self):
    return 'Nome: {} - Descrição: {} - Data: {} - Agenda: {} - Usuario: {}'.format(self.nome, self.descricao, self.data, self.agenda_id, self.usuario_id)
              
  def get_values_save_lembrete(self):
    return [self.nome, self.descricao, self.data, self.agenda_id, self.usuario_id]