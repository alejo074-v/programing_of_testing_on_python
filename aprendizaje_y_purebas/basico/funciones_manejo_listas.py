'''**Suma **(+) Concatena dos o más listas:
a=[1,2]
b=[3,4]
a + b --> [1,2,3,4]
**Multiplicación **(*) Repite la misma lista:
a=[1,2]
a * 2 —> [1,2,1,2]
Añadir elemento al final de la lista:
a=[1]
a.append(2)=[1,2]
Eliminar elemento al final de la lista:
a=[1,2]
b=a.pop()
a=[1]
**Eliminar elemento **dado un indice:
a=[1,2]
b=a.pop(1)
a=[2]
Ordenar lista de menor a mayor, esto modifica la lista inicial
a=[3,8,1]
a.sort() —> [1,3,8]
Ordenar lista de menor a mayor, esto NO modifica la lista inicial
a=[3,8,1]
a.sorted() —> [1,3,8]
Eliminar elementos de lista Elimina el elemento de la lista dado su indice
a=[1,2,3]
del a[0] —> a[2,3]
Eliminar elementos de lista Elimina el elemento de la lista dado su valor
a=[0, 2, 4, 6, 8]
a.remove(6)
a=[0, 2, 4, 8]
**Range **creacion de listas en un rango determinado
a=(list(range(0,10,2))) -->crea un conteo desde 0 hasta 10 en pasos de 2 en 2.
a=[0,2,4,6,8]
Tamaño lista len Devuelve el valor del tamaño de la lista:
a=[0,2,4,6,8]
len(a)=5'''

'''append()
Este método agrega un elemento al final de una lista.

count()
Este método recibe un elemento como argumento, y cuenta la cantidad de veces que aparece en la lista.

extend()
Este método extiende una lista agregando un iterable al final.

index()
Este método recibe un elemento como argumento, y devuelve el índice de su primera aparición en la lista.

insert()
Este método inserta el elemento x en la lista, en el índice i.

pop()
Este método devuelve el último elemento de la lista, y lo borra de la misma.

remove()
Este método recibe como argumento un elemento, y borra su primera aparición en la lista.

reverse()
Este método invierte el orden de los elementos de una lista.

sort()
Este método ordena los elementos de una lista.

Convertir a listas
Para convertir a tipos listas debe usar la función list() la cual esta integrada en el interprete Python.'''