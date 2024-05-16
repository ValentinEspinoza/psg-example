# De la siguiente lista [1,2,3,4,5,6,7,8,9,10] obtener una sub lista inversa utilizando índices de 3 en 3

lista = [1,2,3,4,5,6,7,8,9,10]
sub_lista = lista.copy()
sub_lista.reverse()
sub_lista = sub_lista[::3]

print('Sub lista inversa de 3 en 3: ', sub_lista)
