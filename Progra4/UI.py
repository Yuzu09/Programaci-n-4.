def obtenerDatosUsuario():
    numeroCuenta = input("Ingrese el numero de cuenta: ").strip().upper()
    documentoIdentidad = int(input("Ingrese su numero de documento: ").strip())
    nombre = input("Ingrese su nombre: ").strip().upper()
    return numeroCuenta, documentoIdentidad, nombre

def montoOpcion(opcion):
    monto = float(input(f"ingrese el monto a {opcion}: "))
    return monto

def mostrarMensaje(mensaje):
    print(mensaje)

