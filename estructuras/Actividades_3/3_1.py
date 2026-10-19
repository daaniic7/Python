codigo_correcto = "4826"
intentos_restantes = 3

codigo = input("Introduce el código de acceso: ")

if codigo == codigo_correcto:
    print("Acceso autorizado")
else:
    while codigo != codigo_correcto and intentos_restantes > 1:
        intentos_restantes -= 1
        print(f"El código {codigo} es incorrecto.")
        codigo = input(f"Vuelve a intentarlo, te quedan {intentos_restantes} intentos: ")
        
        if codigo == codigo_correcto:
            print("Acceso autorizado")

    if codigo != codigo_correcto:
        print("Acceso bloqueado, has agotado los tres intentos.")