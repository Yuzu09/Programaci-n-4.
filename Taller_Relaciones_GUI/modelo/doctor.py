class Doctor:
    def __init__(self, nombre, especialidad, dni):
        self.id = nombre
        self.nombre = especialidad
        self.especialidad = dni

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Especialidad: {self.especialidad}"