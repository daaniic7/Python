import math
PLANTILLA = "ABCDABCDAB"

n_alumnos = 0
alumnos = []
respuestas = []
notas = []

print("CORRECTOR DE EXÁMENES")


def pedir_respuesta():
        respuesta = input("Respuestas: ")
        while len(respuesta) != 10:
           respuesta = input("Debe escribir 10 respuestas. ")
        return respuesta

def corregir(respuestas):
     nota = 0
     for respuesta in respuestas:
          nota = 0
          pos = 0
          for letra in respuesta:
               if letra != "-":
                if letra == PLANTILLA[pos]:
                    nota += 1
                elif letra != PLANTILLA[pos]:
                    nota -= 0.25 
               pos += 1
     notas.append(nota)
     return nota

def mejor_nota(nota):
     mejor = max(nota)
     return mejor

def nota_media(notas):
    return sum(notas) / len(notas)

def main():
    n_alumnos = int(input("¿Cuántos alumnos hay? "))

    for a in range(n_alumnos):
        alumnos.append(input("Nombre: "))
        respuestas.append(pedir_respuesta())    
    
    for alumno in alumnos:
         print(f"{alumno}: {corregir(respuestas)}")

    print(f"Nota media: {nota_media(notas)}")
    print(f"Mejor nota: {mejor_nota(notas)}")
  
if __name__ == "__main__":
    main()