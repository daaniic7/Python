import random

titular = "Daniel"
saldo = random.randint(0, 1000)
estado = True

operacion = input("Introduce que operacion quieres hacer ")

match operacion:

    case "ingresar":
        print(f"Tu saldo actual es: {saldo}")
        ingreso = int(input("Introduce la cantidad que quieres ingresar "))
        if ingreso > 0:
            saldo += ingreso
            print(f"Ingresando: {ingreso} euros")
            print(f"Felicidades ahora tienes: {saldo} euros")
        else:
            print("Esa no es una cantidad valida")
        
    case "retirar":
        print(f"Tu saldo actual es: {saldo}")
        retiro = int(input("Introduce la cantidad que vas a retirar "))
        if retiro > 0 and saldo >= retiro:
            saldo -= retiro
            print(f"Retirando: {retiro} euros")
            print(f"Felicidades ahora tienes: {saldo} euros")
        else:
            print("Esa no es una cantidad valida")
       
    case "abrir cuenta":
        if not estado:
            estado = True
        print("La cuenta está abierta")

    case "cerrar cuenta":
        print("Cuenta cerrada")
        if estado:
            estado = False
        print("La cuenta está cerrada")

    case "consultar":
        print(f"Tu saldo actual es :{saldo} euros")

    case _:
        print("Opcion no valida")
