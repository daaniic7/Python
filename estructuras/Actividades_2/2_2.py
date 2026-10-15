ENTRADA_GENERAL = 8
ENTRADA_MENORES = 5
ENTRADA_MAYORES = 6
DESCUENTO_MIERCOLES = 1
PELICULA_3D = 2


edad = int(input("Introduce tu edad: "))
dia = input("Introduce el día de la semana: ").strip().lower()
es_3d = input("¿La sesión es 3D? ").strip().lower()
precio = 0


match edad:

    case edad if edad < 0:
        print("La edad no puede ser negativa ")

    case edad if edad < 12:
        precio = ENTRADA_MENORES
        print(f"Entrada: {ENTRADA_MENORES} euros ")

        if dia == "miércoles" or dia == "miercoles":
            precio -= DESCUENTO_MIERCOLES
            print(f"Descuento miercoles: -{DESCUENTO_MIERCOLES} euros")

        if es_3d == "sí" or es_3d == "si":
            precio += PELICULA_3D
            print(f"Pelicula 3D: +{PELICULA_3D} euros")

        print(f"Precio final: {precio} euros")

    case edad if edad >= 65:
        precio = ENTRADA_MAYORES
        print(f"Entrada: {ENTRADA_MAYORES} euros")

        if dia == "miércoles" or dia == "miercoles":
            precio -= DESCUENTO_MIERCOLES
            print(f"Descuento miércoles: -{DESCUENTO_MIERCOLES} euros")

        if es_3d == "sí" or es_3d == "si":
            precio += PELICULA_3D
            print(f"Pelicula 3D: +{PELICULA_3D} euros")

        print(f"Precio final: {precio} euros")

    case _:
        precio = ENTRADA_GENERAL
        print(f"Entrada: {ENTRADA_GENERAL} euros")

        if dia == "miércoles" or dia == "miercoles":
            precio -= DESCUENTO_MIERCOLES
            print(f"Descuento miércoles: -{DESCUENTO_MIERCOLES} euros")

        if es_3d == "sí" or es_3d == "si":
            precio += PELICULA_3D
            print(f"Pelicula 3D: +{PELICULA_3D} euros")

        print(f"Precio final: {precio} euros")