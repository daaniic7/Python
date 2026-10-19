aforo_maximo = 8
aforo_actual = 0
continuar = True

while continuar:
    accion = input("Introduce una acción: ")
    
    match accion:
        case "entra":
            if aforo_actual < aforo_maximo:
                aforo_actual += 1
                print(f"Ha entrado una persona, el aforo actual es: {aforo_actual}")
            else:
                print("La sala está llena, no puede entrar nadie más")
                
        case "sale":
            if aforo_actual > 0:
                aforo_actual -= 1
                print(f"Ha salido una persona, el aforo actual es: {aforo_actual}")
            else:
                print("No hay nadie dentro")
                
        case "fin":
            print(f"Quedan {aforo_actual} personas en la sala")
            continuar = False
            
        case _:
            print("Acción inválida")