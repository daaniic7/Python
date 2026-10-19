import random

saldo = random.randint(0, 1000)
titular = input("Introduce el nombre del titular de la cuenta: ")
cuenta_activa = True
continuar = True

while continuar:
    operacion = input("Introduce una operación: ").strip().lower()

    match operacion:
        case "ingresar":
            if cuenta_activa:
                cantidad = float(input("Introduce la cantidad a ingresar: "))
                saldo += cantidad
                print(f"Se han ingresado {cantidad} euros, el saldo actual es {saldo} euros")
            else:
                print("La cuenta está cerrada, no se puede ingresar dinero")

        case "retirar":
            if cuenta_activa:
                cantidad = float(input("Introduce la cantidad a retirar: "))
                if cantidad <= saldo:
                    saldo -= cantidad
                    print(f"Se han retirado {cantidad} euros, el saldo actual es {saldo} euros")
                else:
                    print("Saldo insuficiente para realizar la retirada")
            else:
                print("La cuenta está cerrada, no se puede retirar dinero")

        case "consultar":
            estado = "activa" if cuenta_activa else "cerrada"
            print(f"Titular: {titular}, Saldo: {saldo} euros, Estado de la cuenta: {estado}")

        case "cerrar cuenta":
            if cuenta_activa and saldo == 0:
                cuenta_activa = False
                print("La cuenta ha sido cerrada")
            elif not cuenta_activa:
                print("La cuenta ya está cerrada")
            else:
                print("No se puede cerrar la cuenta con saldo disponible")

        case "abrir cuenta":
            if not cuenta_activa:
                cuenta_activa = True
                saldo = 0
                print("La cuenta ha sido abierta con un saldo inicial de 0 euros")
            else:
                print("La cuenta ya está activa")

        case "salir":
            estado_final = "activa" if cuenta_activa else "cerrada"
            print(f"Estado final de la cuenta Titular: {titular}, Saldo: {saldo} euros, Estado: {estado_final}")
            continuar = False

        case _:
            print("Operación no válida")