### Python Package Management
'''
Gestor de paquetes para Python, para usar módulos que no tengamos descargados.
Para ello usaremos una herramienta llamada "pip".
Tambien con este gestor podremos manejar nuestras versiones de Python

Por ejemplo para instalar e importar py, pandas, módulos de login, machine learning, big data, flash, para crear un APi, etc.

Nota: Un paquete es un conjunto de módulos, po ello tenemos un montón de ficheros. En el cual tenemos acceso a utilidades lógicas.
'''

#PIP https://pypi.org

#1. Importando Numpy
import numpy

import mypackage.arithmetics #py -m pip install "numpy"

print(numpy.version.version)

#Creamos un areglo numpy
numpy_array =  numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

#Lo imprimimos
print(numpy_array)

#Ahora lo multiplicamos  x2
print(numpy_array * 2)


#2. Importando pandas
import pandas #py -m pip install "pandas"

#pip list : Nos genera una lista de los paquetes que tenemos
# pip uninstal "pandas" : Podemos desinstalar paquetes, en este caso "pandas".


#3. Importando requests
import requests #py -m pip install "requests"
'''
Sirve para hacer peticiones a un API
'''
#Esta varriable ealiza una solicitud HTTP GET a la URL especificada.
# La función requests.get() es proporcionada por la biblioteca "requests" y se utiliza para realizar solicitudes HTTP GET.
#En este caso, la URL especificada es la API de Pokémon que devuelve información sobre los primeros 151 Pokémon.

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response) #Imprime el objeto de respuesta completo, que incluye detalles como el código de estado y posiblemente otros metadatos
print(response.status_code) #imprimiendo únicamente el código de estado HTTP de la respuesta

print(response.json()) # Extrayendo y decodificando los datos JSON de la respuesta HTTP que obtuviste de la API de Pokémon. 
#La respuesta de la API contiene un objeto JSON que tiene claves, aquí los nombres de Pokémones y sus valores correspondientes, como detalles de cada Pokémon.





#Aritmethics Package Management 
import mypackage
#print(sum_two_values(1, 4)) NameError: name 'sum_two_values' is not defined

print(mypackage.arithmetics.sum_two_values(1, 4)) #5


#Importando directamente forma 1
#Importando el módulo arithmetics completo del paquete mypackage

from mypackage import arithmetics
print(arithmetics.sum_two_values(2, 5))

#Importando directamente forma 2
##Importando directamente la función

from mypackage.arithmetics import sum_two_values
print(sum_two_values(3, 5))




#Llamando a otheraritmetics
from myotherpackage import otheraritmetics
print(otheraritmetics.sum_two_values(2, 5))
