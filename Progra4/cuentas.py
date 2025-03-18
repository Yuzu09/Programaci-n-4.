class Cuenta:
    def __init__(self, numeroDeCuenta, documentoIdentidad, nombre, Saldo):
        self.numeroDeCuenta = numeroDeCuenta
        self.documentoIdentidad = documentoIdentidad
        self.nombre = nombre
        self.saldo = Saldo

#datos de cuentas
cuenta1 = Cuenta(12345, 1088238419, "NICOLAS", 10000)
cuenta2 = Cuenta(12345, 123456789, "SOFIA", 30000)
cuenta3 = Cuenta(12345, 987654321, "ANGEL", 100000)
cuenta4 = Cuenta(12345, 132435465, "JUAN", 5000)
cuenta5 = Cuenta(12345, 6543211234, "JOSE", 20000)
cuenta6 = Cuenta(12345, 3265232352, "ANGELICA", 1000000)
cuenta7 = Cuenta(12345, 42105574, "ANDREA", 0)

#lista que contiene todas las cuentas
cuentaClientes = [cuenta1,cuenta2,cuenta3,cuenta4,cuenta5,cuenta6,cuenta7]