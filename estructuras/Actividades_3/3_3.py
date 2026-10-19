precio = 170
importe_pagado = 0

while importe_pagado < precio:
    moneda = int(input("Introduce una moneda: "))
    
    if moneda in [10, 20, 50, 100]:
        importe_pagado += moneda
    else:
        print("Introduce una moneda válida")

print("Producto entregado")

cambio = importe_pagado - precio

if cambio > 0:
    print(f"Cambio a devolver: {cambio} céntimos (o {cambio / 100:.2f} euros)")
else:
    print("Has pagado el importe exacto, no hay cambio")