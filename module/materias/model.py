class Materias:
    def __init__(self, materia, area, usuario_id):
        self.materia = materia
        self.area = area
        self.usuario_id = usuario_id
        self.id = None

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return (f'Materia: {self.materia} - area: {self.area} - Usuario: {self.usuario_id}')

    def get_values_saves_materia(self):
            return [self.materia, self.area, self.usuario_id]


