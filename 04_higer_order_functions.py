#Funciones de Orden superior#
'''
Funciones que hacen cosas con funciones
Las funciones son ciudadanos de primera clase que están en lo más alto de la jerarquía a la hora de tratar con propiedad este tipo de dato de lenguaje de programación.

Ciudadanos de primer orden:
- Tipos de datos
- Strings
- Input

Existen funciones de orden superior creadas dentro del sistema.

Funciones que tienen dentro funciones.
'''
#Esta es una función normal
def sum_one(value):
    return value + 1

#¿Por qué una función puede usarse dentro de otra función?

#Una función puede llamar dentro otra función pero aún no hablamos de las funciones de orden superior.
def sum_two_values_and_add_one(first_value, second_value):
    #Aquí le pasamos a la función anterior el cual le suma 1
    return sum_one(first_value + second_value)


print(sum_two_values_and_add_one(5, 2))

print("Función como parámetro")

#Pasamos la función en un parámetro
def sum_two_values_and_add_one1(first_value, second_value, f_sum_one):
    #Aquí le decimos que retorne la función anterior el cual le suma 1
    return f_sum_one(1)

#Nos retorna 2 porque no hacemos nada con los otros parámetros.
print(sum_two_values_and_add_one1(5, 2, sum_one))

print("Función 2 como parámetro")

def sum_five(value):
    return value + 5

'''
Funciones de orden superior
- Son capaces de ejecutar funciones 
- Se pueden utilizar como una base para reutilizarlas.
'''

#Pasamos la función en un parámetro
#Aquí podemos ponerle f_sum para aclarar que es una función de suma o f, es un Magic value
def sum_two_values_and_add_one2(first_value, second_value, f):
    #Aquí le decimos que retorne la función anterior el cual le suma 1
    return f(first_value + second_value)

print(sum_two_values_and_add_one2(4, 3, sum_one))
#Aquí reaprovechamos la función pero le pasamos otra función como parámetro.
print(sum_two_values_and_add_one2(4, 3, sum_five))






print("Closures")





#### Closures ###
'''
Hacen referencia a las funciones de orden superior pero con una peculiaridad.
Dentro de una función definimos otra función que hará algo.
- Una función que retorna otra función por eso no lleva parámetros mayormente.
- Vale para montar paradigmas asíncronos como en Swift o Kotlin
'''

def sum_ten():
    def add(value):
        return value + 10
    return add


add_closure = sum_ten()
print(add_closure)
#Le hablo directamente a la función guardada
print(add_closure(5)) #15

##Probaremos pasándoles un parámetro a la función
def sum_ten2(original_value):
    def add(value):
        return value + 10 + original_value
    return add

#Ahora debemos ponerle un valor por el parámetro que pusimos.
add_closure2 = sum_ten2(1)
print(add_closure2)
#Le hablo directamente a la función guardada
print(add_closure2(5)) #16 
#El original value lo tiene como contexto aunque nos haya retornado la función.
'''
Aunque no le pasamos el valor a la closure que es del add, el ya guardó la referencia del original.
- El value que le pasamos es 5
- + 10 es 15
- + el valor original que es 1
- Nos da 19

Por lo cual se sigue guardando todo
- En este caso el original value forma parte de la definición a la hora de llamar a sum_ten con la variable.
'''
print("Lo llamamos de otra forma")
#Aquí agrupamos la llamada a una función, la función retorna una función y nosotros invocamos a la nueva función con un nuevo valor.
print((sum_ten2(5))(1))







### Built-in Higher Order Functions ###
'''
Funciones de orden superior que ya existen en el propio lenguaje.
'''
print("Funciones construidas")
#Datos de referencia
#Una función Map siempre va a necesitar un conjunto iterable.

numbers = [2, 5, 10, 21, 3, 30]

#Map
'''
The map() function executes a specified function for each item in an iterable. 
The item is sent to the function as a parameter.

- Map recorre todos los valores y ejecuta una función sobre cada uno de ellos para modificar su valor.

map(function, iterables)
'''
def multiply_two(number):
    return number * 2

print(map(multiply_two, numbers)) #Imprime que tenemos un objeto

#Ahora lo guardamos en una lista para tener algo más visual:
print(list(map(multiply_two, numbers)))
'''
Map ha iterado cada uno de los valores y ha ejecutado sobre cada valor la función que le pasamos.
Por ello de un listado original hemos obtenido un listado que ha duplicado su valor.

- Map con un listado iterable, genera otro listado iterable en función de la función que pasamos.'''

print("Ahora probaremos con una lambda")

#Ahora aquí tiene más sentido las lambdas.
#Porque definimos una operación ya que solo queríamos multiplicar cada operación del listado de datos x3
print(list(map(lambda number: number * 3, numbers)))


#Filter
print("Filter...")

'''
Definition and Usage
The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.

- Requiere una función que de True o False para saber cuando filtrar.
- Recorre todos los valores y ejecuta una función que retorna true o false para saber como filtrar los valores del literal.
filter(function, iterable)
}
'''
#Si es mayor que 10 retorna true
def filter_greater_that_ten(number):
    '''if number > 10:
        return True'''
    
    return number > 10 #Esto es lo mismo que el if anterior.

print(filter(filter_greater_that_ten, numbers))  #Nos sale que es un objeto
#Tenemos que ponerlo con list y se creará un nuevo listado.
print(list(filter(filter_greater_that_ten, numbers)))

#Ahora probaremos con una lambda
print(list(filter(lambda number: number > 10, numbers))) #Retorna lo mismo







### Reduce
print("Función Reduce...")

from functools import reduce

'''
Reduce:
- Tenemos que importarla para usarla porque está en un módulo independiente.
from functools import reduce

La mayoría de las funciones de orden superior del sistema necesitan un iterable algo que puedan recorrer.

- Reduce opera entre los valores que va recorriendo
- Opera con los valores que tiene en cada caso cuando la recorre
- Reduce opera con un valor más el acumulado.
'''
#numbers = [2, 5, 10, 21, 3, 30]


def sum_two_values(first_value, second_value,):
    #Esto solo lo ponemos para ver que hay dentro
    print(first_value)
    print(second_value)
    #Esto es lo que devuelve la función
    return first_value + second_value

'''
71 es el resultado de haber ido sumando cada valor hasta reducirlo a 1.

Aquí decidimos como ir reduciendo, y no tenemos un listado, sino un único valor.
- En base a todos los elementos del iterable fue capaz de ir juntandolos segun nuestro criterio,
recibiendo siempre los 2 valores y sumándolos.

2 + 5 = 7.
7 + 10 = 17
17 + 21 = 38
38 + 3 = 41
41 + 30  = 71
'''

print(reduce(sum_two_values, numbers)) #71

###Sale error
def sum_two_values(first_value, second_value, three_value):
    return first_value + second_value + three_value

#print(reduce(sum_two_values, numbers)) error!
