### Error Types ###

#SyntaxError

#print"¡Hola comunidad! #Error
print("¡Hola comunidad!")

'''
Error de sintaxis:  Algo escribiste mal
Statements must be separated by newlines or semicolons ()

SyntaxError: unterminated string literal (detected at line 5)
'''

#NameError
frutilla = "fresa"
#print(frutas)
print(frutilla)
'''
NameError: name 'frutas' is not defined
La variable no está definida
'''

#IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5]) #IndexError: list index out of range

'''
IndexError
Nos dice que el elemnto está fuera del índice
'''

#Module Not Found Error

#import maths Error
import math

'''
Nos dice que no hay un módulo llamado así
ModuleNotFoundError: No module named 'maths'

Cuando queremos importar un:
- Módulo que no existe.
- Módulo que está mal escrito

'''

#Attribute Error
print(math.pi)
#print(math.PI) Error

'''
Importamos un módulo queremos acceder a alguna función que tiene, pero:
- La función no existe
- Escribimos mal la función del módulo

AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?  
'''


#Key Error
'''
Los diccionarios son una estructura que nos permiten guardar un valor asociado a una clave.
- No es ordenada no existe la posición 0
- Se debe acceder por el nombre de la propiedad o clave
'''

my_dict = { "Nombre": "Marga", "Apellido": "Li", "Edad": 21, 1 : "Rosa"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) Error!
print(my_dict["Apellido"])

'''
KeyError: 'Apelido'

Se refiere a la clave del diccionario que estamos consultando:

- La clave no existe
- La clave está mal escrito
'''

#print(my_list["Nombre"]) Error!
#print(my_list["0"]) Error!
print(my_list[0]) #Python

#Podemos acceder con valores booleanos a una lista
#NO ES RECOMENDABLE HACER ESTO!
print(my_list[False]) #Imprime Python = 0, porque False es 0
print(my_list[True]) #True = 1 Imprime Swift



#Type Error
'''
Las listas :
Se acceden a la posición por el número de índice
- No tienen clave : valor.

TypeError: list indices must be integers or slices, not str
 - Indices deben ser números enteros y no strings
'''

#Import Error

#from math import PI        Error!
from math import pi
print(pi)
'''
ImportError: cannot import name 'PI' from 'math' (unknown location). Did you mean: 'pi'?

Importamos un módulo pero solo queremos importar una función específica de él.

- Sin embargo la función que queremos importar del módulo no existe
- No existe la función 

'''

#Value Error

#Forma correcta de transformar strings a enteros
#Sólo podemos hacerlo con números en forma de string.

my_int = "10"

print(my_int) #10
print(type(my_int)) #String

#Imaginemos que ahora quiero transformarlo a un entero
my_int = int("10") 
print(type(my_int)) #Ahora dice que es un entero
print(my_int) #10


'''
Pero si intentamos hacerlo con números más texto nos da error.
Porque no se puede

ValueError: invalid literal for int() with base 10: '10 Años'
'''
#my_int = int("10 Años") Error


#Zero Division Error

print(4/2)
#print(4/0) Error!

'''
ZeroDivisionError: division by zero

- Errores cuando intentamos dividir entre cero.
'''