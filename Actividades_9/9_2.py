# Actividad 2: descomponer una duración
# Guarda en una variable una duración total de 7384 segundos. Calcula cuántas horas completas, minutos restantes y segundos restantes contiene,
# usando división entera (//) y resto (%). Muestra los tres resultados; deben ser 2 horas, 3 minutos y 4 segundos.

d_total = 7384
horas = d_total // 3600
segundos_restantes = d_total % 3600

minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

print(f"Duración total: {d_total} segundos")
print(f"Resultado: {horas} horas, {minutos} minutos y {segundos} segundos.")