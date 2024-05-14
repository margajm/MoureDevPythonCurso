### Diccionarios ###
'''
Son un hashmap por dentro, pero así como tal, no lo tenemos en Python.
- Tiene una estructura de par clave: valor
- Sirve para relacionar datos.
- Podemos almacenar datos en forma clave valor
- En un diccionario incluso puedo almacenar otro diccionario
Se relaciona con las apis, json.
- Nos da facilidad para acceder a un elemento.
'''
#¿Cómo vamos a crear un diccionario?
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

#Tenemos una estructura par clave:valor
#Aquí algunos son strings y otros combinación de entero y string.
my_other_dict = { "Nombre": "Brais", "Apellido": "Moure", "Edad":35, 1: "Python"}

my_dict = {
    "Nombre" : "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    #Como clave tiene un string
    #Pero como valor tiene un set dentro
    "Lenguajes" : {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

#Nos da facilidad para acceder a un elemento.
print(my_dict["Nombre"])

#Podemos actualizar un valor directamente
my_dict["Nombre"] = "Pedro" #Para ello accedemos a la clave
print(my_dict["Nombre"])

#Accedemos a la clave que se llama 1
print(my_dict[1])

#Así podemos añadir un nuevo campo al diccionario
my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

#Podemos eliminar un solo elemento dentro del diccionario
del my_dict["Calle"]
print(my_dict)

#Esta es una búsqueda por clave NO por valor.
print("Moure" in my_dict) #Por eso aquí sale False
print("Apellido" in my_dict) #Y aquí true

#De esta forma podemos acceder al valor de una clave
print(my_dict["Apellido"])

#Con items tenemos un listado de los items
print(my_dict.items())
#Con keys tenemos un listado de las keys o claves en formato listo.
print(my_dict.keys())
#Nos retorna todos los valores.
print(my_dict.values())
#Podemos pasarle una o más claves
#Y nos retornará esas claves sin valores
print(my_dict.fromkeys(("Nombre", 1)))

#Podemos crear un diccionario nuevo con claves pero sin valores
my_new_dict = my_other_dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

#Pero podemos hacer lo mismo de esta forma:
#Usando la palabra reservada dict
#Pero lo mejor es crear un diccionario vacío e ir llenándolo después.
my_new_dict2 = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict2)

print("De lista a diccionario")

#Podemos crear un diccionario a partir de una lista
my_list = ["Nombre", 1, "Fruta"]

my_another_dict = dict.fromkeys((my_list))
print(my_another_dict)

#Podemos copiar todas las claves de un diccionario 
my_another_dict = dict.fromkeys(my_dict)
print((my_another_dict))

#También podemos copiar y a la vez mandarle nuevos valores:
#El primer argumento son todas las claves principales
#El segundo parámetro es el valor para todas las claves.
my_another_dict = dict.fromkeys(my_dict, ("Brais", "Moure"))
print(my_another_dict)

#Es por eso que aquí estamos pasando un diccionario a todos los valores.
my_another_dict = dict.fromkeys(my_dict, my_dict)
print(my_another_dict)

#Si le ponemos en corchetes es lo mismo, pero no tiene sentido.
#Porque le mete el mismo valor a todas las claves.
my_another_dict = dict.fromkeys(my_dict, [ "Brais", "Moure"])
print(my_another_dict)

#Podemos trasnformar de diccionario a lista
#Pero el valor que tendremos son las claves nada más
dicci_to_list = list(my_another_dict)
print(dicci_to_list)
print(type(dicci_to_list))

#Pasa lo mismo si convertimos a tupla o a set
print(list(my_another_dict.values()))
print(tuple(my_another_dict))
print(set(my_another_dict))

my_values = my_another_dict.values()
print(type(my_values))

print(list(dict.fromkeys(list(my_another_dict.values())).keys)) 