# Escriba un programa que pregunte si se quiere calcular el área de un triángulo o la de un círculo. Si se elige triángulo (T o t),
# pide base y altura; si se elige círculo (C o c), pide el radio. Después escribe el área.

import math

continuar = True
area = 0

while continuar:

    print("a) Triángulo")
    print("b) Círculo")
    opciones = input("¿Qué figura quiere calcular (Escriba T o C)? ").lower()
    match opciones:
        case "t":
            print("Calculo de areas")
            try:
                base = float(input("Escriba la base: "))
                altura = float(input("Escribe la altura: "))
            except ValueError as error:
                print("Error: ", error)
            else:
                area = (base * altura) /2
                print(f"Un triángulo de base {base} y altura {altura} tiene un área de {area}")
            finally:
                print("Operación Finalizada")
        case "c":
            print("Calculo de areas")
            try:
                radio = float(input("Escriba el radio: "))
            except ValueError as error:
                print("Error", error)
            else:
                area = math.pi * radio*radio
                print(f"Un círculo de radio {radio} tiene un área de {area}")
            finally:
                print("Operacón finalizada")
        case _:
            print("Opción no válida")



