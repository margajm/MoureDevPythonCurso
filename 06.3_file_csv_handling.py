#.csv file

import os

#Se usa para obtener la ruta absoluta donde estamos
# Imprimir el directorio de trabajo actual
print("Directorio de trabajo actual:", os.getcwd())
#c:/Users/Lenovo/Documents/Programacion/Moure_Dev/Python_moureDev/Intermediate/06_file_handling.py

# Cambiar al directorio donde deseas trabajar
os.chdir("C:\\Users\\Lenovo\\Documents\\Programacion\\Moure_Dev\\Python_moureDev\\Intermediate")

# Ahora puedes abrir el archivo con una ruta relativa
#Asegúrate de que la ruta a la que cambias con os.chdir() es exactamente la que contiene tu archivo.

import csv

csv_file = open("my_file.csv", "w+")

#Lo normal es abrir los archivos csv con un excel.


#Ahora para escribir, tenemos que hacerlo por filas.

#Intentaremos pasarle este diccionario pero en filas y columnas"
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

#Para poder escribir tenemos que usar csv.writer así.
csv_writer = csv.writer(csv_file)

#Luego le pasamos cada fila para escribir:
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Marga", "Li", 21, "Python", "https://moure.dev"])
#Ahora le pasamos con comillas vacías porque es un secreto.
csv_writer.writerow(["Roswell", " ", 2, "Cobol", ""])

#Luego de terminar de escribir cerramos.
csv_file.close()

with open("my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
      print(line)