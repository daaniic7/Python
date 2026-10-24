TIEMPO_CINE = 2
DINERO_CINE = 10

TIEMPO_COMER = 2
DINERO_COMER = 30

TIEMPO_MUSEO = 1
DINERO_MUSEO = 5

TIEMPO_DEPORTE = 1
DINERO_DEPORTE = 1

TIEMPO_CASA = 1
DINERO_CASA = 0


def menu():
    """Muestra por pantalla las actividades disponibles.

    No recibe argumentos ni devuelve ningún valor. Su función es mostrar
    las opciones que el usuario puede elegir.
    """
    print("\n1. Ir al cine (10 euros/2 horas)")
    print("2. Salir a comer (30 euros/2 horas)")
    print("3. Visitar un museo (5 euros/1 hora)")
    print("4. Hacer deporte (1 euro/1 hora)")
    print("5. Quedarse en casa (0 euros/1 hora)")


def comprobar_presupuesto(dinero, precio, tiempo, duracion):
    """Comprueba si una actividad se puede realizar.

    Args:
        dinero: Dinero disponible para realizar la actividad.
        precio: Precio de la actividad.
        tiempo: Tiempo disponible para realizar la actividad.
        duracion: Duración de la actividad en horas.

    Returns:
        True si hay suficiente dinero y tiempo; False en caso contrario.
    """
    return dinero >= precio and tiempo >= duracion


def mostrar_resumen(actividades, dinero_gastado, tiempo_utilizado, dinero,tiempo):
    """Muestra el resumen final del día.

    Args:
        actividades: Lista con los nombres de las actividades elegidas.
        dinero_gastado: Cantidad total de dinero gastado.
        tiempo_utilizado: Cantidad total de tiempo utilizado en horas.
        dinero: Dinero que queda después de las actividades.
        tiempo: Tiempo que queda después de las actividades.

    Returns:
    Muestra el resumen directamente por pantalla.
    """
    print("\nRESUMEN DEL DÍA")

    if len(actividades) == 0:
        print("No has elegido ninguna actividad.")
    else:
        for actividad in actividades:
            print(f"- {actividad}")

    print(f"Dinero gastado: {dinero_gastado} euros")
    print(f"Tiempo utilizado: {tiempo_utilizado} horas")
    print(f"Presupuesto restante: {dinero} euros")
    print(f"Tiempo restante: {tiempo} horas")


def main():
    """Ejecuta el programa para organizar el día libre."""
    dinero = int(input("¿Cuánto dinero te quieres gastar como máximo? "))
    tiempo = int(input("¿Cuánto tiempo tienes? "))
    dinero_gastado = 0
    tiempo_utilizado = 0
    actividades_elegidas = []

    while tiempo > 0 and dinero > 0:
        menu()
        opcion = input("Elige una opción: ").strip()

        match opcion:
            case "1" | "cine":
                if comprobar_presupuesto(
                        dinero, DINERO_CINE, tiempo, TIEMPO_CINE):
                    actividades_elegidas.append("Ir al cine")
                    dinero -= DINERO_CINE
                    tiempo -= TIEMPO_CINE
                    dinero_gastado += DINERO_CINE
                    tiempo_utilizado += TIEMPO_CINE
                    print("Has elegido ir al cine.")
                else:
                    print("No tienes suficiente dinero o tiempo.")
            case "2" | "comer":
                if comprobar_presupuesto(
                        dinero, DINERO_COMER, tiempo, TIEMPO_COMER):
                    actividades_elegidas.append("Salir a comer")
                    dinero -= DINERO_COMER
                    tiempo -= TIEMPO_COMER
                    dinero_gastado += DINERO_COMER
                    tiempo_utilizado += TIEMPO_COMER
                    print("Has elegido salir a comer.")
                else:
                    print("No tienes suficiente dinero o tiempo.")
            case "3" | "museo":
                if comprobar_presupuesto(
                        dinero, DINERO_MUSEO, tiempo, TIEMPO_MUSEO):
                    actividades_elegidas.append("Visitar un museo")
                    dinero -= DINERO_MUSEO
                    tiempo -= TIEMPO_MUSEO
                    dinero_gastado += DINERO_MUSEO
                    tiempo_utilizado += TIEMPO_MUSEO
                    print("Has elegido visitar un museo.")
                else:
                    print("No tienes suficiente dinero o tiempo.")
            case "4" | "deporte":
                if comprobar_presupuesto(
                        dinero, DINERO_DEPORTE, tiempo, TIEMPO_DEPORTE):
                    actividades_elegidas.append("Hacer deporte")
                    dinero -= DINERO_DEPORTE
                    tiempo -= TIEMPO_DEPORTE
                    dinero_gastado += DINERO_DEPORTE
                    tiempo_utilizado += TIEMPO_DEPORTE
                    print("Has elegido hacer deporte.")
                else:
                    print("No tienes suficiente dinero o tiempo.")
            case "5" | "casa":
                if comprobar_presupuesto(
                        dinero, DINERO_CASA, tiempo, TIEMPO_CASA):
                    actividades_elegidas.append("Quedarse en casa")
                    dinero -= DINERO_CASA
                    tiempo -= TIEMPO_CASA
                    dinero_gastado += DINERO_CASA
                    tiempo_utilizado += TIEMPO_CASA
                    print("Has elegido quedarte en casa.")
                else:
                    print("No tienes suficiente dinero o tiempo.")
            case _:
                print("Opción no válida.")
                continue

        print(f"Ahora te quedan {tiempo} horas y {dinero} euros.")

    if tiempo == 0 and dinero == 0:
        print("\nSe te han acabado el tiempo y el dinero.")
    elif tiempo == 0:
        print("\nSe te ha acabado el tiempo.")
    elif dinero == 0:
        print("\nSe te ha acabado el dinero.")

    mostrar_resumen(actividades_elegidas,dinero_gastado,tiempo_utilizado,dinero,tiempo)


if __name__ == "__main__":
    main()
