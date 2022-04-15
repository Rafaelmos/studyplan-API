class Usuario:
  def __init__(self, nome, senha, idade):
    self.nome = nome
    self.senha = senha
    self.idade = idade
    self.id = None

  def set_id(self, id):
    self.id = id

  def __str__(self):
    return 'Nome: {} - Senha: {} - Idade: {}'.format(self.nome, self.senha, self.idade)

  def get_values_save(self):
    return [self.nome, self.senha, self.idade]

  def get_json(self):
    return {
      'id': self.id,
      'nome': self.nome,
      'senha': self.senha,
      'idade': self.idade,
    }
