### File Handling
'''
Puede que nos hayamos descargado un fichero de internet, 
y nuestro programa lo empieze a leer.

Puede que nosotros estemos guardando algo en un fichero porque nos dio la gana.

... Pero y si es un excel o un csv?

- Nosotros podemoos leer muchos tipos de ficheros.
- Según el tipo de fichero tendremos que comportarnos y manejarlo de una forma en concreta.

'''
import os

#Se usa para obtener la ruta absoluta donde estamos
# Imprimir el directorio de trabajo actual
print("Directorio de trabajo actual:", os.getcwd())
#c:/Users/Lenovo/Documents/Programacion/Moure_Dev/Python_moureDev/Intermediate/06_file_handling.py

# Cambiar al directorio donde deseas trabajar
os.chdir("C:\\Users\\Lenovo\\Documents\\Programacion\\Moure_Dev\\Python_moureDev\\Intermediate")

# Ahora puedes abrir el archivo con una ruta relativa
#Asegúrate de que la ruta a la que cambias con os.chdir() es exactamente la que contiene tu archivo.



### 1. Txt en file
#Abriremos nuestro fichero con open() 
print("Usando Open")
'''
txt_file = open("my_file.txt", "w")

#ERROR! No se puede leer
#print(txt_file.read()) #io.UnsupportedOperation: not readable

#Para leer el archivo debemos cambiarle la "w" de escribir a "r" de leer.
txt_file = open("my_file.txt", "r")
print(txt_file.read())

#Si queremos leer y escribir a la vez debemos hacer esto:
#txt_file = open(my_file.txt, "rw") #ValueError: must have exactly one of create/read/write/append mode!

#De esta manera si podemos pero lo sobreescribe y borra todo:
txt_file = open("my_file.txt", "w+") 

Atención: Comentaré todo lo de arriba, porque hizo que se borre lo que escribí en el archivo ya que lo sobreescribe y borra todo al usar "w+".

'''
#De esta manera si lo lee de manera normal y también podemos escribir .
txt_file = open("my_file.txt", "r+")
#print(txt_file.read()) #Leemos todo el archivo

#Si queremos por ejemplo solo leer los 10 primeros caracteres incluido el espacio. (Comentaremos la instrucción de leer de arriba para que funcione.)
#print(txt_file.read(10)) # Imprimió: Mi nombre

'''Pero si hacemos esto:

print(txt_file.read()) #Leemos todo el archivo
print(txt_file.read(10)) # Imprimió espacios.

- Primero leera todo el archivo y como no queda nada, solo leerá los espacios en este caso 10.
'''

#Leemos línea por línea el archivo.
#print(txt_file.readline())
#print(txt_file.readline())


#Leemos varias líneas a la vez como un array
#print(txt_file.readlines())

for line in txt_file.readlines():
    print(line)


#Escribiendo en el archivo
txt_file.write("Mi lenguaje favorito es Python.")
print(txt_file.readline())

#Escribiendo con un salto de línea.
txt_file.write("\nAunque también me gusta JavaScript")
print(txt_file.readline())

#Así cerramos el fichero si ya no necesitamos trabajar con él.
txt_file.close()


'''
¡Hola! Los archivos .txt son archivos de texto plano. No contienen ningún formato especial, solo texto sin formato. Aquí tienes algunos ejemplos de uso:

Notas y documentos: Los archivos .txt son útiles para crear notas rápidas o documentos que no requieren formato especial.

Scripts y código fuente: Algunos lenguajes de programación y scripts utilizan archivos de texto para almacenar el código fuente.

Configuración de aplicaciones: Algunas aplicaciones utilizan archivos .txt para almacenar configuraciones y preferencias del usuario.

Almacenamiento e intercambio de datos: Aunque no es tan común como los formatos como CSV o JSON, puedes usar archivos .txt para almacenar y compartir datos.

'''


#Otros tipos de ficheros
'''
Se trabaja con sus respectivos módulos de python

'''


#JSON

import json
'''
¡Hola! Los archivos JSON (JavaScript Object Notation) son un formato de intercambio de datos que se utiliza para almacenar 
y transmitir datos entre un servidor y una aplicación web, o entre diferentes partes de una misma aplicación. 
Los datos en un archivo JSON se presentan en pares de clave-valor y pueden ser fácilmente leídos o generados por la mayoría de los lenguajes de programación.

Aquí tienes algunos ejemplos de uso:

Configuración de aplicaciones: Muchas aplicaciones utilizan archivos JSON para almacenar configuraciones y preferencias del usuario.

Intercambio de datos: Los archivos JSON son una forma común de intercambiar datos entre el cliente y el servidor en aplicaciones web.

Almacenamiento de datos: Algunas bases de datos NoSQL, como MongoDB, utilizan JSON para almacenar y recuperar datos.

APIs: Muchas APIs web, como la API de Twitter o la API de Google Maps, devuelven datos en formato JSON.
'''


#.csv file

import csv

'''
¡Hola! Los archivos CSV (Comma-Separated Values) son un tipo de archivo de texto plano que se utiliza para almacenar datos tabulares, es decir,
 datos organizados en filas y columnas. Cada línea del archivo representa una fila de datos y los valores individuales en una fila están separados por comas,
   de ahí el nombre.

Aquí tienes algunos ejemplos de uso:

Intercambio de datos: Los archivos CSV son una forma común de intercambiar datos entre diferentes aplicaciones. 
Por ejemplo, puedes exportar datos de una base de datos SQL a un archivo CSV para importarlos en otra aplicación.

Análisis de datos: Los archivos CSV son ampliamente utilizados en el análisis de datos.
 Puedes abrir un archivo CSV en una hoja de cálculo o en un programa de análisis de datos para analizar los datos.

Almacenamiento de datos: Aunque no es tan común, puedes usar archivos CSV para almacenar datos. 
Sin embargo, no son tan flexibles como las bases de datos o los archivos XML para este propósito.

Importación/Exportación de datos en hojas de cálculo: Los archivos CSV son una forma común de importar y exportar datos en aplicaciones de hojas de cálculo
como Microsoft Excel o Google Sheets.
'''


#.xlsx file
'''
Primero se debe instalar el módulo antes de importarlo.
'''
#import xlrd
'''
¡Hola! Los archivos .xlsx son un tipo de archivo de hoja de cálculo creados por Microsoft Excel. Se utilizan para organizar, analizar y almacenar datos en forma tabular.
 Aquí tienes algunos ejemplos de uso:

Análisis de datos: Los archivos .xlsx son muy utilizados en el análisis de datos. Puedes usarlos para recopilar y analizar datos, 
realizar cálculos y representar los datos en gráficos.

Gestión financiera: Muchas empresas utilizan archivos .xlsx para la gestión financiera, como la elaboración de presupuestos, el seguimiento de gastos
 y la planificación financiera.

Planificación de proyectos: Los archivos .xlsx pueden ser útiles para la planificación de proyectos, permitiéndote seguir el progreso de las tareas y asignar recursos.

Creación de informes: Puedes usar archivos .xlsx para crear informes que presenten datos de una manera fácil de entender.

Recuerda que, aunque los archivos .xlsx son muy útiles, también tienen limitaciones, como un número máximo de filas y columnas, 
y pueden no ser la mejor opción para conjuntos de datos muy grandes o para el análisis de datos más avanzado.
'''



#.xml file
import xml
'''
¡Hola! Los archivos XML (eXtensible Markup Language) se utilizan para almacenar y transportar datos. 
Son útiles porque son legibles tanto para las máquinas como para las personas. 
En el contexto de la informática, se utilizan para estructurar datos en una forma que puede ser fácilmente interpretada
 y utilizada por diferentes sistemas y aplicaciones.

¡Por supuesto! Aquí tienes algunos ejemplos de cómo se utilizan los archivos XML:

Configuración de aplicaciones: Muchas aplicaciones de software utilizan archivos XML para almacenar configuraciones y preferencias del usuario.

Intercambio de datos: Los archivos XML son una forma común de intercambiar datos entre sistemas diferentes, especialmente en servicios web.

Almacenamiento de datos: Algunas bases de datos utilizan XML para almacenar y recuperar datos.

Descripción de datos: XML se utiliza en lenguajes como RDF (Resource Description Framework) para describir recursos web en la web semántica.

Documentos: Algunos formatos de documentos, como Office Open XML (utilizado por Microsoft Word) y OpenDocument (utilizado por OpenOffice y LibreOffice),
 utilizan XML para describir el contenido y la estructura de los documentos.'''