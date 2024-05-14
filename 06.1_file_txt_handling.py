### File Handling

import os

#Se usa para obtener la ruta absoluta donde estamos
# Imprimir el directorio de trabajo actual
print("Directorio de trabajo actual:", os.getcwd())
#c:/Users/Lenovo/Documents/Programacion/Moure_Dev/Python_moureDev/Intermediate/06.1_file_handling.py

# Cambiar al directorio donde deseas trabajar
os.chdir("C:\\Users\\Lenovo\\Documents\\Programacion\\Moure_Dev\\Python_moureDev\\Intermediate")

# Ahora puedes abrir el archivo con una ruta relativa
#Asegúrate de que la ruta a la que cambias con os.chdir() es exactamente la que contiene tu archivo.

import os

# Se usa para obtener la ruta absoluta donde estamos
# Imprimir el directorio de trabajo actual
print("Directorio de trabajo actual:", os.getcwd())

# Cambiar al directorio donde deseas trabajar
os.chdir("C:\\Users\\Lenovo\\Documents\\Programacion\\Moure_Dev\\Python_moureDev\\Intermediate")

### 1. Txt en file
# Abriremos nuestro fichero con open()

txt_file = open("my_file.txt", "w+")
txt_file.write("Mi nombre es Lisa \nTengo 21 años \nMi mascota es un conejo")

# Reiniciamos la posición del cursor al inicio del archivo para leerlo desde el principio
txt_file.seek(0)

print(txt_file.read(10)) # Imprimió: Mi nombre
print(txt_file.readline())
print(txt_file.readline())

for line in txt_file.readlines():
    print(line)

txt_file.write("Mi lenguaje favorito es Python.")
print(txt_file.readline())

txt_file.write("\nAunque también me gusta JavaScript")
print(txt_file.readline())

# No necesitas cerrar el archivo aquí, ya que se cerrará automáticamente al final del script

# Abrir el archivo en modo de adjuntar ('a') para escribir en él
txt_file.write("\nY Swift")

# Reiniciamos la posición del cursor al inicio del archivo para leerlo desde el principio
txt_file.seek(0)

# Leer y mostrar el contenido completo del archivo
print(txt_file.read())

# Cerrar el archivo al finalizar el trabajo con él
txt_file.close()
