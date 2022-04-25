class Materias:
    def __init__(self, materia, area):
        self.materia = materia
        self.area = area
        self.id = None

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return (f'Materia: {self.materia} - area: {self.area}')

    def get_values_saves(self):
            return [self.materia, self.area]

