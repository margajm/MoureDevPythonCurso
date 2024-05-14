#Json files
'''
Es muy común trabajar con este tipo de ficheros cuando trabajamos con servidores, aplicaciones web.
Porque es el tipo de serenización que estamos usando para codificar datos a través de la red.

Json son como un diccionario, clave: valor, lo podemos convertir en un objeto modelo para trabajar con él desde backend o frontend.

'''

import os

#Se usa para obtener la ruta absoluta donde estamos
# Imprimir el directorio de trabajo actual
print("Directorio de trabajo actual:", os.getcwd())
#c:/Users/Lenovo/Documents/Programacion/Moure_Dev/Python_moureDev/Intermediate/06.2_file_json_handling.py

# Cambiar al directorio donde deseas trabajar
os.chdir("C:\\Users\\Lenovo\\Documents\\Programacion\\Moure_Dev\\Python_moureDev\\Intermediate")

# Ahora puedes abrir el archivo con una ruta relativa
#Asegúrate de que la ruta a la que cambias con os.chdir() es exactamente la que contiene tu archivo.



# Para trabajar con un archivo json vamos a tener un módulo que es "import json" para trabajar con estos archivos en python.
import json

#Usando "w+" le decimos si NO existe, entonces crea el fichero y empieza a trabajar sobre él. Aquí lo creó por ello.
#Y lo almacenamos en una variable.
#El w+ puede escribir el archivo pero siempre borrará todo primero para escribir después.
json_file = open("my_file.json", "w+")

#Normalmente en json las claves son strings.
json_test = {  
    "Name": "Marga", 
    "Surname":"Li", 
    "Age": 21,
    "Language":
      [
        "Python",
        "Swift", 
        "Kotlin"
        ],
    "website": "https://moure.dev"
}

#Para escribir en Json debemos usar el módulo de json de python.
#Primero le pasamos el objeto de python, luego el nombre del archivo a escribir.

#Para indentar le agregamos indent y el número y listo.
json.dump(json_test, json_file, indent=2)
#json.dump(json_test, json_file, indent=2) Hace que se escriba lo mismo 2 veces y con error.

json_file.close() #Cerramos el archivo

'''
Ahora dará error, porque no podemos leer un archivo cerrado.

ValueError: I/O operation on closed file.

for line in json_file.readlines():
    print(line)
'''

with open("my_file.json") as another_file:
    for line in another_file.readlines():
        print(line)


'''
Hola! json.dump() es una función en Python que se utiliza para escribir datos en formato JSON en un archivo.
Hola! json.load() es una función en Python que se utiliza para cargar datos de un archivo JSON. Convierte los datos JSON en un objeto Python,

'''

#Si solo queremos leer y luego transformarlo en un diccionario.

json_dict = json.load(open("my_file.json"))

#Imprimimos el diccionario.

print("Imprimimos el diccionario python")
print(json_dict)
print(type(json_dict)) #<class 'dict'>

#Ahora podemos acceder a las claves valor ya que es un objeto python ahora.
print(json_dict["Name"])

