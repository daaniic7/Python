# Actividad 4: actualizar las plazas disponibles
# Un aula tiene 12 plazas disponibles. Reserva 3 plazas y después cancela 1 reserva, actualizando la variable con asignación aumentada. 
# Muestra el número final de plazas y, mediante una expresión condicional, muestra "Hay plazas" si queda alguna o "Completo" si no queda ninguna.


plazas = 12
plazas -= 3
plazas += 1

print(f"Número final de plazas: {plazas}")
estado = "Hay plazas" if plazas > 0 else "Completo"
print(estado)