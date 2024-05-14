### Tuples ###
#Podemos declarar así una tupla
#Una tupla es un conjunto de valores IMMUTABLES.

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

#También podemos acceder a sus elementos internamente
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[-1]) #-1 accede al último elemento
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

##Count es para contar las repeticiones de un valor
print(my_tuple.count("Brais"))
print(my_tuple.index("Moure")) #Nos indica en qué nro de indice está el valor
#Si impriminos de nuevo, nos dará 2 porque se queda con el primer índice que ha encontrado.
print(my_tuple.count("Brais"))

''' LAS TUPLAS SON INMUTABLES
#Una tupla es INMUTABLE no se pueden reasignar los valores como en las listas.
my_tuple[1] = 1.80
print(my_tuple) 

#Si intento agregar un nuevo valor tampoco funcionará porque una tupla es INMUTABLE.
my_tuple[5]= 1.80
print(my_tuple) 
'''

#Concatenar tuplas
#Esta es una nueva tupla pero sigue siendo IMMUTABLE
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:6])

'''
my_sum_tuple = (35, 1.77, 'Brais', 'Moure', 'Brais', 35, 60, 30): Aquí se define una tupla llamada my_sum_tuple que contiene varios elementos de diferentes tipos de datos, incluyendo enteros, flotantes y cadenas de caracteres.

print(my_sum_tuple[3:6]): Esto imprime una porción de la tupla my_sum_tuple. La porción se toma desde el índice 3 hasta el índice 6 (no inclusive). Es decir, se incluyen los elementos en las posiciones 3, 4 y 5 de la tupla.

El elemento en la posición 3 es 'Moure'.
El elemento en la posición 4 es 'Brais'.
El elemento en la posición 5 es '35'.
'''

#Podemos convertir nuestras tuplas en listas 
my_tuple = list(my_tuple)
print(type(my_tuple))
#Ya que ahora e suna lista podemos cambiar los actuales.
my_tuple[4] = "MoureDev"
# Y añadirle nuevos valores 
my_tuple.insert(1, "Azul") #En el índice 1 insertamos la palabra "Azul"
print(my_tuple) #Imprimimos la lista

#La cambiamos ahora para que sea tupla de nuevo
my_tuple = tuple(my_tuple)
print(my_tuple) 
print(type(my_tuple))

#Pero una tupla debe ser una tupla de principio a fin,
#Sin embargo sin por alguna ocasion debemos hacer un cambio esta es una opcion.

#No se puede eliminar un elemento dentro de una tupla
del my_tuple[2]

#Podemos eliminar una tupla 
del(my_tuple)
print(my_tuple) #Sale error porque ahora la variable my_tuple no existe.