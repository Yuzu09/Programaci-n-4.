class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []

    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)

    def buscar_doctor(self, dni):
        for doctor in self.doctores:
            if doctor.dni == dni:
                return doctor
        return None