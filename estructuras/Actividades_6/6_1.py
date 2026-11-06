productos = ["pan", "leche", "huevos"]
precios = [0.85, 1.20, 2.50]
carrito = []

def convertir_numero(texto):
    numero = int(texto)
    if numero < 0:
        raise ValueError("El número no puede ser negativo")
    return numero


def anadir(carrito, numero):
    if numero not in [0, 1, 2]:
        raise IndexError("El producto no existe")
    carrito.append(precios[numero])


def quitar(carrito, posicion):
    if posicion >= len(carrito):
        raise IndexError("La posicion no es valida")
    carrito.pop(posicion)


def calcular_total(carrito):
    total = 0
    for p in carrito:
        total += p
    return total


def repartir(total, personas):
    if personas <= 0:
        raise ValueError("El número de personas debe ser mayor a 0")
    return total / personas


def menu():
    print("1. Añadir")
    print("2. Quitar")
    print("3. Repartir")
    print("4. Salir")


def main():
    continuar = True

    while continuar:
        menu()
        opciones = convertir_numero(input("Introduce una opción: "))

        match opciones:
            case 1:
                print("0. Pan")
                print("1. Leche")
                print("2. Huevos")
                try:
                    producto = convertir_numero(input("Qué producto quieres añadir? "))
                    anadir(carrito, producto)
                except IndexError as error:
                    print("Error", error)
                except ValueError as error:
                    print("Error", error)
                finally:
                    print(f"Carrito: {carrito}")
                    print(f"Precio de los productos: {calcular_total(carrito)} euros")
            case 2:
                try:
                    posicion = convertir_numero(input("Introduce la posición del producto a quitar: "))
                    quitar(carrito, posicion)
                    print("El producto se ha eliminado")
                except IndexError as error:
                    print("Error", error)
                except ValueError as error:
                    print("Error", error)
                finally:
                    print(f"Carrito: {carrito}")
                    print(f"Precio de los productos: {calcular_total(carrito)} euros")
            case 3:
                try:
                    personas = convertir_numero(input("Introduce el número de personas: "))
                    print("Cada persona tiene que pagar: ",repartir(calcular_total(carrito), personas))
                except ValueError as error:
                    print("Error", error)
                except ZeroDivisionError:
                    print("Error", error)
                else:
                    print("Operacion realizada")
                finally:
                    print("Lo productos que llevas tienen este precio: ", carrito)
                    print("El total que llevas es: ", calcular_total(carrito))
            case 4:
                continuar = False
            case _:
                print("Opción no válida")

    print("Adios")

if __name__ == "__main__":
    main()
