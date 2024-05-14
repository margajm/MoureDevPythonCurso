### Listas ###
'''
Una lista es diferente a un vector o array, porque se puede hacer operaciones de inserción, recordación, ordenación
Una lista acaba por debajo con un array, pero un array es inamovible y no lo tenemos como tal en Python
'''
#Python es un lenguaje orientado a objetos


my_list = list()
#También esta es una lista
my_other_list = []

#Las lsitas sirven para añadir elementos es como una caja, el índice empieza en cero, sirve para agrupar datos en orden
print(len(my_list)) #Sale 0 porque hay cero elementos

#Python es de lenguaje dinámico
#Podemos tener valores iguales
my_list = [35,24,17,25,35, 37]
print(my_list)
print(len(my_list))

#En una lista podemos tener distintos tipos de datos
my_other_list = [35, 1.77, "Brais", "Moure"]
print(type(my_other_list))

#Podemos acceder a los elementos por separados
#Cuando usamos el len es más para acceder a los datos
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1]) #"Moure"
print(my_other_list[-3])
print(my_other_list[-4])
#IndexError print(my_other_list[-5]) #Error porque no hay ningun elemento
#IndexError print(my_other_list[4]) #Error porque ya se pasó del tamaño


#Podemos acceder con valores booleanos a una lista
#NO ES RECOMENDABLE HACER ESTO!

print(my_list[False]) #Imprime Python = 0, porque False es 0
print(my_list[True]) #True = 1 Imprime Swift



print(my_other_list.count("Brais")) #Count es para contar las repeticiones de un valor
print(my_list.count(35))

#Desempaquetando una lista


#Ponemos todo en el mismo orden de la lista
#Si ponemos solo 3 elementos no funciona, porque la lista tiene 4 y en el mismo orden.
#age, height, name = my_other_list
#print(age)

#Necesitamos poner todos los elementos
age, height, address, surname = my_other_list
print(address)  # Imprime Brais porque lo colocamos la variable en la posición del nombre.

#Intentaremos cambiar la posición y reasignaremos, pero es un posible foco de errores.
#Una lista es un objeto
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)
print(height)
print(age)
print(surname)

#Concatenamos 2 listas 
#Se concatenan en el orden en que pusimos 
print(my_other_list + my_list)

#Esto es una lista
print(list([1,2,3,4]))
print([1,2,3,4])

#Esto no funciona, no se puede hacer estas operaciones
#print(my_other_list - my_list)

#Una lista es mutable

#Append agrega un nuevo elemento a la lista
my_other_list.append("Moure Dev")
print(my_other_list)

#Insert agrega en una posición específica un elemento
my_other_list.insert(1, "Azul")
print(my_other_list)

#También podemos tomar el indice e igualarlo a un valor
my_other_list[1] = "Rosado"
print(my_other_list)

#Eliminar un elemento de una lista cuando sabemos cuál es el elemento.
my_other_list.remove("Rosado")
print(my_other_list)
#Vemos que teníamos dos 30, pero solo nos ha eliminado uno de ellos.
my_list.remove(35)
print(my_list)

#Eliminamos el último elemento de la lista

print(my_list.pop())
print(my_list)

#Podemos pasarle un índice un Pop para que elimine el elemento pero no es lo común.
#Podemos guardar el elemento eliminado del pop en una lista.
my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

#Podemos eliminar así de frente también por el índice.
del my_list[2]
print(my_list)


#Podemos copiar una lista
my_new_list = my_list.copy()

#Así vaciamos una lista
my_list.clear()
print(my_list)
print(my_new_list)

#Podemos ordenar al reves una lista
my_new_list.reverse()
print(my_new_list)

my_new_list.append(20)
print(my_new_list)

#Podemos ordenar una lista de menor a mayor
'''
Las listas de Python tienen un método incorporado list.sort() que modifica la lista in situ. 
También hay una función incorporada sorted() que crea una nueva lista ordenada a partir de un iterable.

Una clasificación ascendente simple es muy fácil: simplemente llame a la función sorted(). Retorna una nueva lista ordenada:
>>>sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]

También puede usar el método list.sort(). Modifica la lista in situ (y retorna None para evitar confusiones).
Por lo general, es menos conveniente que sorted(), pero si no necesita la lista original, es un poco más eficiente.

a = [5, 2, 3, 1, 4]
a.sort()
a
[1, 2, 3, 4, 5]
'''
#Otra diferencia es que el método list.sort() solo aplica para las listas. En contraste, la función sorted() acepta cualquier iterable.

'''
sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]

Funciones clave
Ambos list.sort() y sorted() tienen un parámetro key para especificar una función (u otra invocable) que se llamará en cada elemento de la lista antes de hacer comparaciones.

Por ejemplo, aquí hay una comparación de cadenas que no distingue entre mayúsculas y minúsculas:

>>>
sorted("This is a test string from Andrew".split(), key=str.casefold)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
El valor del parámetro key debe ser una función (u otra invocable) que tome un solo argumento y retorne una clave para usar con fines de clasificación. Esta técnica es rápida porque la función de la tecla se llama exactamente una vez para cada registro de entrada.

Un uso frecuente es ordenar objetos complejos utilizando algunos de los índices del objeto como claves. Por ejemplo:

>>>
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
La misma técnica funciona para objetos con atributos nombrados. Por ejemplo:

>>>
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
Objects with named attributes can be made by a regular class as shown above, or they can be instances of dataclass or a named tuple.
'''
my_new_list.sort()
print("Conociendo el sort")
print(my_new_list)

print(my_new_list[1:2])
print(my_new_list[0:1])

#Ordenación con sorted
print(sorted([9, 85, 7, 1, 3, 50]))
print(sorted("oveja"))


#Esto era una lista pero ya lo volví String porque tiene un TIPADO DINÁMICO
#Podemos trabajar con diferentes tipos de datos y luego le podemos cambiar.
#No se puede crear una constante en Python pero si variables finales que a nivel de sintaxis sería escribirlo en mayuscula.
my_list = "Hola Python"
print(my_list)
print(type(my_list))

