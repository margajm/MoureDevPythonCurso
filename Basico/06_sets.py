### Sets ###
'''Un set y una lista tiene de base un array
#Aunque eso realmente no existe sino solo listas.

set es un tipo de dato tambiénm
Se pueden hacer operaciones de las listas, pero:
- No tiene estructura de orden
- No se puede acceder a cada elemento individualmente por su índicie
- Utiliza un hash interno para ordenar
- No admite repetidos


Ventajas:
- No acepta repetidos
- Puede trabajar muy rápido con estructuras que no sean ordenadas.
'''

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

#Pero ya cuando le añadimos valores el reconoce que es un set
my_other_set = { "Brais", "Moure", 35}
print(type(my_other_set))

#Usamos length para contar cuantos elementos hay.
print(len(my_other_set))
print(my_other_set)


#Añadimos un nuevo elemento
my_other_set.add("MoureDev")

#Vemos que nos lo coloca primero porque un set no es una estructura ordenada
#Por dentro utiliza un hash para meter cada elemento
print(my_other_set)

#Por ello no se puede acceder a cada elemento porque no hay orden

#print(my_other_set[0]) Un SET no es una estructura ordenada.

#Añadimos de nuevo el mismo elemento
my_other_set.add("MoureDev")
#Vemos que NO lo imprime, porque un SET NO ADMITE REPETIDOS.
print(my_other_set)

#Si queda ordenado es casualidad porque no tiene estructura y se ordena por un hash interno.

#CONSULTAS
#Preguntamos "Moure" existe en "my_other_set"? ...

print("Moure" in my_other_set)
print("Mouri" in my_other_set)

#Podemos eliminar elementos individuales dentro de un set
my_other_set.remove("Moure")
print(my_other_set)

#Podemos vaciar el set
my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

#Cuando ponemos un . nos aparece las funciones propias del objeto-
#En cambio "del" es propio del sistema.

#Eliminamos la variable 
del my_other_set
#print(my_other_set) Error variable eliminada

#Vamos a transformar my_set en una lista
#Sin embargo es arriesgado porque no sabemos el orden que se colocará.

my_set = { "Brais", "Moure", 35}
my_list = list(my_set)
print(type(my_set))



print(my_list)
#Vemos que se convirtió una lista
print(type(my_list))
#Ahora si podemos entrar al índice de cada elemento.
print(my_list[0])

#Añadiremos una variable llamada igual que la que borramos
my_other_set = { 'Kotlin', 'Swift', 'Python'}
#Podemos concatenar sets
my_new_set = my_set.union(my_other_set)
print(my_other_set)
print(my_new_set)
#NO se pude concatenar valores repetidos porque no admite repetidos.
print(my_new_set.union(my_new_set))
#Aquí de nuevo sigue igual porque no le pasamos nada diferente.
print(my_new_set.union(my_new_set).union(my_set))
#Aqui si pasa algo porque le pasamos valores diferentes en el print.
#Pero no se almacena esto porque solo lo hemos puesto en el print.
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))

#Podemos imprimir las diferencias o los valores distintos entre 2 sets.
print(my_set)
print(my_new_set)
print(my_new_set.difference(my_set))


