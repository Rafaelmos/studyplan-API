class Metas:
  def __init__(self, nome, descricao, status, prazo, agenda_id, usuario_id):
    self.nome = nome
    self.descricao = descricao
    self.status = status
    self.prazo = prazo
    self.agenda_id = agenda_id
    self.usuario_id = usuario_id
    self.id = None

  def set_id(self, id):
    self.id = id
  
  def __str__(self):
    return 'Nome: {} - Descrição: {} - Status: {} - Prazo: {} - Agenda: {} - Usuario: {}'.format(self.nome, self.descricao, self.status, self.prazo,self.agenda_id, self.usuario_id)
              
  def get_values_save_meta(self):
    return [self.nome, self.descricao, self.status, self.prazo, self.agenda_id, self.usuario_id]