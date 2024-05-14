### Modules ###
'''
Si tenemos algún fichero externo o archivo que quiera utilizarlo aquí en mi código:
Ejemplo:
- Clases que me pueden ser de utilidad

Va a llegar un momento que mi programa tiene que ser escalable segur.
- Tendre que usar mis ficheros externos para llamar a clases, funciones, etc que quiera utilizar.

Para ello:
1. Importamos
2. Llamamos

Entonces para ello debo tener acceso a esos ficheros externos en mi archivo actual para acceder a ellos.

- Uno de los errores al empezar a programar es copiar el código que tenemos en otro archivo.
- Pero lo mejor es llamar a ese fichero externo porque está dentro de todo lo que compone mi aplicación.
- De esta forma nos evitamos replicar el mismo código en los diferentes ficheros de nuestra aplicación.

Un módulo también puede ser una librería que creó otra persona, o del mismo python.

'''

#Aquí decimos todo lo que haya dentro de module quiero que se cargue aquí, lo cual puede hacer que se cargue, se demore un poquito más.
import Moure_Dev.Python_moureDev.Basic.my_module as my_module

'''
Esto no nos lo acepta así especifiquemos que solo queremos una función de ese archivo:
Eso es porque la forma en que fue nombrado el fichero no lo acepta Python.
- El aceptaría si el nombre del fichero que queremos importar estuviera escrito en camel case.

- En cambio my_module.py está escrito en CamelCase
from 10_functions import sum_two_values

'''

#Para acceder a los datos que tenemos en módulo
#Llamamos a módulo
my_module.sumValues(5, 3, 1)
my_module.printValue("Hola Python!")