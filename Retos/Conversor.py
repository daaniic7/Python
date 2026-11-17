# El calendario musulmán empezó en el año 622 del calendario gregoriano y sus años son algo más cortos. 
# Una relación aproximada entre los dos es 33 g = 32 m + 20526 (g: año gregoriano, m: año musulmán). 
# Escriba un programa que convierta un año de un calendario al otro en los dos sentidos.

# EJEMPLO

# Dígame un año: 2002
# El año 2002 del calendario gregoriano es aproximadamente el año 1423 del calendario musulmán.
# El año 2002 del calendario musulmán es aproximadamente el año 2563 del calendario gregoriano.

# De musulman a gregoriano (2002) ---> 33g = 32*2002 + 20526 g = ((32*anyo + 20526)/33)/33
# De gregoriano a musulman (2002) ---> 33*2002 = 32m + 20526 g =(33*2002 - 20526)/32

print("Convertidor entre calendarios")

try:
    anyo = int(input("Digame un año: "))
except ValueError as error:
        print("Error",error)

gregoriano=((32*anyo + 20526)/33)/33
musulman=(33*2002 - 20526)/32


print(f"El año {anyo} del calendario gregoriano es aproximadamente el año {gregoriano} del calendario musulmán")
print(f"El año {anyo} del calendario gregoriano es aproximadamente el año {musulman} del calendario musulmán")