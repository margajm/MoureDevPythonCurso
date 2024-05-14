### List Comprehension o Listas Comprimidas###
'''
Es una forma de crear listas rápidamente o en base a listas que ya tenemos.
Es un mecanismo más potente, porque si ya tenemos una lista, nos va a servir para hacer más cosas.

Nos vale para crear una lista que nosotros ya estamos operando sobre ella en el momento que la vamos a crear.

'''
#Creamos lista base
my_original_list = [35, 24, 62 ,52, 30, 30, 17]

#Transformando una lista en otra
#i será cada uno de los elementos
my_list = [i for i in my_original_list]
print(my_list)

"Esto es un rango al fin y al cabo"
a_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(a_original_list)

#Podemos hacerlo de una forma más rápida y fácil, pero nos pilla solo los primeros 7 valores.
'''
Un for in es un bucle que va iterando sobre cada uno de los elementos.
Le decimos:
- Para cada uno de los elementos en este rango.
- Lo transformaras cada uno para que sea una lista
'''
my_list_range = [i for i in range(7)]
print(my_list_range) #[0, 1, 2, 3, 4, 5, 6]

#Si nosotros queremos hasta el 7 entonces debemos poner el 8 allí.
my_list2 = [i for i in range(8)]
print(my_list2)

#Un rango no es un objeto como tal....
my_range = range(8)
print(my_range)

#Pero si le metemos una lista si nos valdría
print(list(my_range))



'''
Imaginemos que vamos creando nuestra lista pero queremos hacer alguna operación sobre ella.

Le decimos:
- El valor que tu vas a guardar al crear la lista no es exactamente el que te dará el rango.
- El i será el elemento que tenemos cada uno en este rango. 
my_list2 = [i for i in range(8)]


- Este i corresponde a cada uno de los elementos de my_original_list.
my_list = [i for i in my_original_list]

'''



##Guardando en la lista pero con + 1 ###
'''Si hacemos esto ya NO nos está guardando 0, 1, 2
Está pasando por cada uno de los elementos que guarda y sumándole + 1 antes de añadirle a la nueva lista.
'''
my_list3 = [i + 1 for i in range(8)]
print(my_list3)

##Guardando en la lista pero el doble de cada valor ###
'''Si hacemos esto_
Está pasando por cada uno de los elementos que guarda y multiplicándole x 2'''
my_list4 = [i * 2 for i in range(8)]
print(my_list4)


##Guardando en la lista pero multiplicado por su mismo valor
'''Si hacemos esto_
Está pasando por cada uno de los elementos que guarda y multiplicándose por si mismo'''
my_list4 = [i * i for i in range(8)]
print(my_list4)


'''
Generamos una lista con un mecanismo rápido que modificamos en el momento que creamos, le podemos aplicar funciones, filtros, muchas cosas, etc.
- Es decir modificamos el valor antes de guardarlo.
'''

#Guardando una lista con funciones
def sum_five(number):
    return number + 5


#Aquí tenemos cada uno de los valores después de habersele sumado 5 con una función.
my_list5 = [sum_five(i) for i in range(8)]
print(my_list5)

