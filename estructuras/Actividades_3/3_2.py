numero = int(input("Introduce un número entero mayor que 1: "))

es_primo = True

if numero <= 1:
    es_primo = False
else:
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False

if es_primo:
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} no es primo")