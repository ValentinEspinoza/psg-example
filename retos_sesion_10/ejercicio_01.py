# Anita y Pepito llevan saliendo juntos por 4 semanas, cada vez que salen van a comer a una plaza de comidas. Ambos quieren saber que tan compatibles son viendo cuantos platos de comida tienen en común. A continuación tienes los platos de comida que ambos han ido pidiendo a los largo de sus citas:

platos_anita = {'Sushi', 'Pizza', 'Tacos', 'Hamburguesa', 'Pasta', 'Alitas'}
platos_pepito = {'Pizza', 'Tacos', 'Ensalada', 'Pasta', 'Helado', 'Milanesa'}

#Si la cantidad platos de comida que tienen en comunes mayor a 50% entonces ambos seguirán saliendo

platos_en_comun = platos_anita.intersection(platos_pepito)
print(platos_en_comun)
media = (len(platos_anita)+len(platos_pepito)) / 2

print(media)

print("Seguirán saliendo?", len(platos_en_comun) > media)