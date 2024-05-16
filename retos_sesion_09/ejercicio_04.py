''' Tienes una tienda de abarrotes y tienes dos listas una con los productos que tienes y otra con los precios
1. Agregar 5 productos nuevos al final de las listas
2. Eliminar el producto con el nombre "Leche" de las listas
3. ¿Cuanto cuesta el producto "Pan" y "Huevo"?
4. ¿Cual es el producto más caro y más barato?
5. ¿Cuántos productos tienes en total?
6. ¿Cuanto cuesta el total de los productos?
7. Ordena los productos alfabéticamente y precios si es posible
8. Eliminar todos los productos de las listas
'''
'''
LISTA ABARROTES
* PRODUCTO      PRECIO(Bs.)
* Avena         4
* Azúcar        3.5
* Café          2.1
* Flan en polvo 15.7
* Pan           0.5
* Huevo         1.2
* Harina        4.5
* Arroz         5.9
* Mantequilla   8.9
* Leche         15.6
* Yoghurt       12.4
'''

lista_productos = ['Avena', 'Azúcar', 'Café', 'Flan en polvo', 'Pan', 'Huevo'] 
lista_precios = [4, 3.5, 2.1, 15.7, 0.5, 1.2]

# lista combinada (producto, precio)
lista_abarrote = list(zip(lista_productos, lista_precios))
print('Lista en el abarrote (producto, precio):','\n',lista_abarrote)
print('')

# 1. Agregar 5 productos nuevos al final de las listas
agrega_productos = ['Harina', 'Arroz', 'Mantequilla', 'Leche', 'Yoghurt']
agrega_precios = [ 4.5, 5.9, 8.9, 15.6, 12.4]

#agregando los 5 productos a lista productos y precios
lista_productos += agrega_productos
lista_precios += agrega_precios
#actualiza lista abarrote
lista_abarrote = list(zip(lista_productos, lista_precios))
print('(1) Lista Abarrote agregado 5 produtos (prod, precio):','\n', lista_abarrote) #lista actualizada
print('')



# 2. Eliminar el producto con el nombre "Leche" de las listas
producto_supr = 'Leche'
indice = lista_productos.index(producto_supr) #indice del producto a eliminar

#elimina el producto 'Leche' de lista productos y precios
lista_productos.pop(indice) #lista actualizada
lista_precios.pop(indice) #lista actualizada

#actualiza lista abarrote
lista_abarrote = list(zip(lista_productos, lista_precios))
print('(2) Lista Abarrote eliminando \'Leche\' (prod, precio):','\n', lista_abarrote) #lista actualizada
print('')



# 3. ¿Cuanto cuesta el producto "Pan" y "Huevo"?
producto_consultar = 'Pan'
indice = lista_productos.index(producto_consultar)
print('(3) Precio producto \'Pan\' y \'Huevo\':')
print('El precio de', producto_consultar, 'es: Bs.', lista_precios[indice])
#consulta precio 'Huevo'
producto_consultar = 'Huevo'
indice = lista_productos.index(producto_consultar)
print('El precio de', producto_consultar, 'es: Bs.', lista_precios[indice])
print('')



# 4. ¿Cual es el producto más caro y más barato?
#extrae indices del precio max y min
indice_max = lista_precios.index(max(lista_precios))
indice_min = lista_precios.index(min(lista_precios))
print('(4) Producto mas caro y mas barato:')
print('El producto mas caro es:', lista_productos[indice_max], 'y cuesta Bs.', lista_precios[indice_max])
print('El producto mas barato es:', lista_productos[indice_min], 'y cuesta Bs.', lista_precios[indice_min])
print('')



# 5. ¿Cuántos productos tienes en total?
print('(5) El total de productos en el abarrote es:', len(lista_productos))
print('')



# 6. ¿Cuanto cuesta el total de los productos?
print('(6) El costo total de los productos en el abarrote asumiendo que tenemos 10 unidades de cada producto resulta ser Bs.', sum(lista_precios)*10)
print('')



# 7. Ordena los productos alfabéticamente y precios si es posible
#copia de listas
lista_prod_ord = lista_productos.copy()
lista_precios_ord = lista_precios.copy()
#ordena alfabeticamente la lista productos
lista_prod_ord.sort()
#print(lista_prod_ord)

#obtiene los indices de productos que han sido movidos luego de ordenar respecto a la lista original
indices_ord = [ lista_productos.index(x) for x in lista_prod_ord ]
#print (indices_ord)

#genera los precios respecto a los indices de los productos ordenados
lista_precios_ord = [lista_precios[y] for y in indices_ord]
#print(lista_precios_ord)

#genera lista abarrote ordenado
lista_abarrote_ord = list(zip(lista_prod_ord, lista_precios_ord))
print('(7) Lista Abarrote ordenado alfabéticamente (producto, precio):','\n', lista_abarrote_ord) #lista ordenada
print('')



# 8. Eliminar todos los productos de las listas
lista_productos.clear()
lista_precios.clear()

print('(8) Eliminar todos los productos')
print('Lista productos: ',lista_productos)
print('Lista precios: ',lista_precios)
