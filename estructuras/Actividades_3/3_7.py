palabra = input("Introduce una palabra: ").strip().lower()

letras = {}

for letra in palabra:
    if letra not in letras:
        letras[letra] = palabra.count(letra)

print("\n" + "=" * 25)
print(f"{'Letra':<12} | {'Frecuencia':<10}")
print("=" * 25)

for letra, frecuencia in letras.items():
    print(f"{letra:<12} | {frecuencia:<10}")

print("=" * 25)