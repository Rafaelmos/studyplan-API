class Materias:
    def __init__(self, materia, area, cronogramadematerias_id):
        self.materia = materia
        self.area = area
        self.cronogramadematerias_id = cronogramadematerias_id
        self.id = None

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return (f'Materia: {self.materia} - area: {self.area} - Cronograma: {self.cronogramadematerias_id}')

    def get_values_saves(self):
            return [self.materia, self.area, self.cronogramadematerias_id]

