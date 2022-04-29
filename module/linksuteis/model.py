class Linksuteis:
    def __init__(self,titulo, link, usuario_id):
        self.titulo = titulo
        self.link = link
        self.usuario_id = usuario_id
        self.id = None

    def set_id(self, id):
        self.id = id

    def __str__(self):
       return 'Título: {} - Link: {} - Usuario: {}'.format(self.titulo, self.link, self.usuario_id)

    def get_values_saves(self):
            return [self.titulo, self.link, self.usuario_id]