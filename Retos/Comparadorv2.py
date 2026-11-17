print("Comparador de numeros")

numeros = []
maximo = 0
minimo = 0
mitado = 0

numero1 = int(input("Escriba un número: "))
numero2 = int(input("Escriba un número: "))
numero3 = int(input("Escriba un número: "))

numeros.append(numero1)
numeros.append(numero2)
numeros.append(numero3)

minimo = min(numeros)
numeros.remove(minimo)
maximo = max(numeros)
numeros.remove(maximo)

if numeros[0] == minimo:
    print(numeros[0], "es el más pequeño")

elif numeros[0] == maximo:
    print(numeros[0], "es el más grande")

else: 
    numeros[0] == maximo
    print(numeros[0], "está en el medio")

