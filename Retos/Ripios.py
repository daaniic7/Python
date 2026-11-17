#Ripios
#Escriba un programa que pida dos palabras y diga si riman: si coinciden las tres últimas letras, riman; 
# si solo coinciden las dos últimas, riman un poco; si no, no riman.

print("Ripios")
palabra1 = input("Dígame una palabra: ")
palabra2 = input("Dígame otra palabra: ")

if palabra1[-3:] == palabra2[-3:]:
    print(f"Las palabras {palabra1} y {palabra2} riman")


elif palabra1[-2:] == palabra2[-2:]:
    print(f"Las palabras {palabra1} y {palabra2} riman un poco")

elif palabra1[-1:] == palabra2[-1:]:
    print(f"Las palabras {palabra1} y {palabra2} no riman")