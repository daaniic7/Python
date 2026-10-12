# Actividad 3: comprobar el acceso a un aula
# Guarda si una persona está matriculada (True), si tiene autorización especial (False) y su edad (17). Puede acceder si está matriculada y tiene al menos 18 años,
# o si tiene autorización especial. Calcula y muestra el resultado como True o False.
# Cambia los valores para comprobar también un caso en el que sí pueda acceder.


matriculado = True
tiene_autorizacion = False 
edad = 17

puede_acceder = (matriculado and edad >= 18) or tiene_autorizacion

print(f"¿Puede acceder? {puede_acceder}")

edad = 18  
puede_acceder = (matriculado and edad >= 18) or tiene_autorizacion

print(f"¿Puede acceder? {puede_acceder}")