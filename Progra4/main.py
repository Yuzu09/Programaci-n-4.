from UI import obtenerDatosUsuario, montoOpcion, mostrarMensaje
from cuentas import cuentaClientes
import os

def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

#Funcion para depositar dinero
def depositarDinero(cuentaClientes, documentoIdentidad, nuevoSaldo):
    for cuenta in cuentaClientes:
        if cuenta.documentoIdentidad == documentoIdentidad:
            retencion = nuevoSaldo * 0.19
            saldoFinal = nuevoSaldo - retencion
            cuenta.saldo += saldoFinal
            limpiarPantalla()
            print(f"Retencion aplicada del 19%: {retencion}")
            print(f"Saldo actualizado para {cuenta.nombre}: {cuenta.saldo}")
            return True, cuenta.saldo
    limpiarPantalla()
    print("Cuenta no encontrada.")
    return False, None
        
#Funcion para retirar dinero
def retirarDinero(cuentaClientes, documentoIdentidad, saldoRetirado):
    for cuenta in cuentaClientes:
        if cuenta.documentoIdentidad == documentoIdentidad:
            if cuenta.saldo >= saldoRetirado:
                cuenta.saldo -= saldoRetirado
                limpiarPantalla()
                print(f"Monto retirado: {saldoRetirado}")
                return True, cuenta.saldo
            else:
                limpiarPantalla()
                print(f"No hay suficientes fondos en su saldo")
                return False, cuenta.saldo
        limpiarPantalla()
    print("Cuenta no encontrada.")
    return False, None


def main():
    limpiarPantalla()
    numeroCuenta, documentoIdentidad, nombre = obtenerDatosUsuario()
    documentoIdentidad = int(documentoIdentidad)
    opcion =  input("1 = Depositar\n2 = Retirar \nIngrese la opcion que desea realizar:").strip()
    limpiarPantalla()
    if opcion == "1":
        monto = montoOpcion("Depositar")
        exito, saldoActual = depositarDinero(cuentaClientes,documentoIdentidad,monto)
        if exito:
                mostrarMensaje("Transaccion realizada con exito.")
        else:
            mostrarMensaje("No se ha podido realizar la transaccion.")

    elif opcion == "2":
           monto = montoOpcion("Retirar")
           exito, saldoActual = retirarDinero(cuentaClientes, documentoIdentidad, monto)
           if exito:
                mostrarMensaje("Transaccion realizada con exito.")
           else:
                mostrarMensaje("No se ha podido realizar la transaccion.")
    else:
        mostrarMensaje("Opcion no valida.")


if __name__ == "__main__":
    main()