alumnos = [
    ["Ana", 8, 7.5, 9],
    ["Luis", 6, 8, 7],
    ["Marta", 9.5, 10, 8.5],
]

print("Datos:")
for nombre, nota1, nota2, nota3 in alumnos:
    print(f"{nombre}: {nota1}, {nota2}, {nota3}")

print()

print(f"{'Alumno':<8} | {'Promedio':<8}")
print("-" * 8 + "|" + "-" * 9)

for nombre, nota1, nota2, nota3 in alumnos:
    media = (nota1 + nota2 + nota3) / 3
    print(f"{nombre:<8} | {media:<8.2f}")