# Conversión a días, horas, minutos

segundos = 288325

dias = int(segundos/3600/24)
segundos_rest = segundos - dias*3600*24

horas = int(segundos_rest / 3600)
segundos_rest -= horas*3600

minutos = int(segundos_rest / 60)
segundos_rest -= minutos * 60


print(f'Los {segundos} segundos equivalen a {dias} días, {horas} horas, {minutos} minutos y {segundos_rest} segundos.' )
