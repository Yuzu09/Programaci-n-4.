
from modelo.hospital import Hospital
from modelo.doctor import Doctor

class HospitalController:
    def __init__(self):
        self.hospital = None

    def crear_hospital(self, nombre):
        self.hospital = Hospital(nombre)

    def agregar_doctor(self, dni, nombre, especialidad):
        if self.hospital is None:
            raise Exception("Primero se debe crear un hospital")
        doctor = Doctor(dni, nombre, especialidad)
        self.hospital.agregar_doctor(doctor)

    def buscar_doctor_por_dni(self, dni):
        if self.hospital is None:
            return None
        doctor = self.hospital.buscar_doctor_por_dni(dni)
        if doctor:
            return {
                "hospital": self.hospital.nombre,
                "doctor_nombre": doctor.nombre,
                "doctor_dni": doctor.dni,
                "especialidad": doctor.especialidad
            }
        return None
