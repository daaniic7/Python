# Actividad 1: calcular una factura
# Crea un programa que lea precio, unidades y porcentaje de descuento, calcule subtotal, descuento, IVA y total, y muestre cada importe con dos decimales. 
# Añade una condición que indique si el pedido supera un umbral de envío gratuito.

precio = float(input("Introduce el precio por unidad: "))
unidades = int(input("Introduce el número de unidades: "))
p_descuento = float(input("Introduce el porcentaje de descuento: "))
subtotal = precio * unidades
descuento = subtotal * (p_descuento / 100)
iva = (subtotal - descuento) * 0.21
total = (subtotal - descuento) + iva

print(f"Subtotal: {subtotal:.2f} euros")
print(f"Descuento: {descuento:.2f} euros")
print(f"IVA: {iva:.2f} euros")
print(f"Total: {total:.2f} euros")

if total >= 50.0:
    print("Has conseguido que el envío sea gratuito")
else:
    print(f"Te faltan {50.0 - total:.2f} euros para el envío gratuito.")