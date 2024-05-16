''' Crear una lista de personas con 10 nombres de personas
1. Obtener una sub lista de 2 a 7
2. Buscar si existe el nombre "Jhon" en la lista original
3. Ordenar la sub lista alfabéticamente
4. Ordenar la lista original alfabéticamente de forma descendente
'''

lista_nombres = ['Valentin', 'Paul', 'Marcos', 'Gabriela', 'Rebeca', 'Carola', 'Fabricio', 'Esteban', 'Juan Pablo', 'Jhonny']

# 1. Obtener una sub lista de 2 a 7
sub_lista = lista_nombres[2:7]
print('1.- ', sub_lista)
print('')


# 2. Buscar si existe el nombre "Jhon" en la lista original
print('2.- Existe el nombre \'Jhon\' en la lista?: ','Jhon' in lista_nombres) 
print('')


#3. Ordenar la sub lista alfabéticamente
lista_ord_alfbt = sorted(sub_lista)
print('3.- ', lista_ord_alfbt)
print('')


# 4. Ordenar la lista original alfabéticamente de forma descendente
lista_ord_alfbt_desc = sorted(lista_nombres)
lista_ord_alfbt_desc.reverse()
print('4.- ', lista_ord_alfbt_desc)