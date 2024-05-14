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



### 1. Txt en file
#Abriremos nuestro fichero con open() 
''''
Nosotros con el comando de abajo borramos el archivo:
os.remove("my_file.txt")

Pero al abrirlo con w+, va a intentar leerlo y como no existe lo va a crear.
- Luego le meterá el contenido que le pasemos.
- Y después la va a eliminar porque llamamos al.

os.remove("my_file.txt")

Pero si comentamos esa línea de remove, el archivo volverá.

'''

txt_file = open("my_file.txt", "w+")
#print(txt_file.read()) #Leemos todo el archivo

txt_file.write("Mi nombre es Lisa \nTengo 21 años \nMi mascota es un conejo")

#Si queremos por ejemplo solo leer los 10 primeros caracteres incluido el espacio. (Comentaremos la instrucción de leer de arriba para que funcione.)
print(txt_file.read(10)) # Imprimió: Mi nombre
print(txt_file.readline())
print(txt_file.readline())

for line in txt_file.readlines():
    print(line)


#Escribiendo en el archivo
txt_file.write("Mi lenguaje favorito es Python.")
print(txt_file.readline())

#Escribiendo con un salto de línea.
txt_file.write("\nAunque también me gusta JavaScript")
print(txt_file.readline())

#Así cerramos el fichero si ya no necesitamos trabajar con él, es una buena práctica.
txt_file.close()


'''
El problema es que estás intentando imprimir el contenido del archivo utilizando txt_file, que ya ha sido cerrado antes de llegar al bloque with.
 Después de cerrar txt_file, ya no puedes acceder a sus métodos para leer o escribir en él.

Para corregir esto y asegurarte de que puedas imprimir las líneas de código antes del bloque with,
 necesitas asegurarte de no cerrar el archivo antes de que hayas terminado de trabajar con él. 

'''
with open("my_file.txt", "a+") as txt_file:
    # Escribir en el archivo en modo de adjuntar ('a') para agregar más contenido
    txt_file.write("\nY Swift")    

    # Mover el cursor al principio del archivo para leerlo
    txt_file.seek(0)
    
    # Leer y mostrar el contenido completo del archivo
    print(txt_file.read())


'''
#Opcion 2


    # Abrir el archivo en modo de adjuntar ('a') para escribir en él
    with open("my_file.txt", "a") as my_other_file:
        my_other_file.write("\nY Swift")    

    # El archivo se cierra automáticamente al salir del bloque 'with'

    # Volver a abrir el archivo en modo de lectura
    with open("my_file.txt", "r") as my_other_file:
        print(my_other_file.read())'''