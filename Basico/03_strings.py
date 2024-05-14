### Strings ###

my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string)) #Cuenta cuantos caracteres.
print(len(my_other_string)) #Cuenta los caracteres.

print(my_string + " " + my_other_string)

#Salto de línea con \n
my_new_line_string = "Este es un String \n con salto de línea"
print(my_new_line_string)

#Tabulación con \t
my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

#Scape string
#String con taabulación que salta a la siguiente línea sin ella
my_scape_string = "\t Este es un String\n escapado"
print(my_scape_string)

#Con doble barra diagonal evitamos que funcionen
my_noscape_string = "\\t Este es un String\n escapado"
print(my_noscape_string)

my_sinscape_string = "\\t Este es un String\\n atrapado"
print(my_sinscape_string)

#Formateo
name, surname, age = "Brais", "Moure", 35

# % hace que el primer texto que yo le pase formateado a esta cadena de texto lo va a poner allí
print("Mi nombre es %s %s y mi edad es %s" .format(name, surname, age))

#Ahora si nos funcionara el format porque se usa con las llaves
#Esto es muy util cuando tenemos la página en inglés y español y pedimos datos 
#Esta es una forma más adecuada si estamos tirando datos tal cuañ
print("Mi nombre es {} {} y mi edad es {}" .format(name, surname, age))

#Esto es más si de verdad estamos formateando los datos, con enteros, etc.
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) #Le ponemos %d para señalar que es un entero.

#Esta forma no es bueno de usar 
#print("Mi nombre es" +  name +  " " + surname + "y mi edad es" + " " + age) #age no es string por eso botara error
print("Mi nombre es" +  name +  " " + surname + "y mi edad es" + " " + str(age))

print("\n")
#Formateo inferido que es la mejor porque agarra el valor de las variables tal cual
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquetado de caracteres
#Asi no funciona porque debemos declarar la otra variable del mismo tamaño de caracteres

'''
language = "Python"
a,b = language

print(a)
print(b)

'''

language = "Python"
a,b,c,d,e,f= language

print(a)
print(b)
print(f)

'''
language = "Python": Se asigna la cadena "Python" a la variable language.

a, b, c, d, e, f = language: Se está intentando desempaquetar la cadena language en variables individuales. 
Dado que language contiene 6 caracteres y se están asignando a 6 variables (a través del desempaquetado), 
cada variable obtendrá un carácter de la cadena language. En este caso, a tomará "P", b tomará "y", c tomará "t", d tomará "h", e tomará "o", y f tomará "n".


'''

#Division

language_slice = language[1:3]
print(language_slice) # Imprime "yt"

#Si le quitamos el segundo número nos imprimira todo a partir del primer número
language_slice = language[1:]
print(language_slice)

language_slice = language[-2] # Accede al penúltimo carácter de la cadena language, que es "o" en este caso.
print(language_slice) #Imprime o

#Reverse
#El final empieza desde -1
'''El primer índice (-1) indica que empezamos desde el último carácter.
El segundo índice (no especificado) indica que terminamos en el primer carácter.
El tercer índice (-1) indica que nos movemos hacia atrás, es decir, en dirección opuesta a la dirección normal.'''
reverse_language = language[::-1]
print(reverse_language)

#Ponemos asi para los caracteres que no queremos que se muestren
language_slice = language[1:2:4]
#Dado que el paso es 4 y solo hay un carácter entre los índices 1 y 2 (que es el carácter en el índice 1), la operación de segmentación solo capturará ese carácter.
print(language_slice) #Imprime "y"

language_slice = language[0:6:2]
print(language_slice)
#Imprime pto el caracter 0,2,4

"""
language_slice = language[0:6:2]: Esto realiza una operación de segmentación en la cadena language.

0 es el índice de inicio del segmento, que apunta al primer carácter "P".
6 es el índice de finalización del segmento (exclusivo), lo que significa que el segmento se detiene antes del índice 6, por lo tanto, incluirá hasta el carácter en el índice 5 ("n").
2 es el paso del segmento, indicando que se incluirá cada segundo carácter.
En resumen, language_slice contendrá caracteres de la cadena language desde el índice 0 hasta el 5, incluyendo solo cada segundo carácter.

print(language_slice): Imprime el valor de language_slice, que contendrá "Pto", que son los caracteres seleccionados de la cadena "Python" mediante la segmentación.

"""

#Funciones
fruta = "limonada"
print(fruta.capitalize()) #La primera letra saldrá en mayuscula
print(fruta.upper()) #Todo saldrá en mayúscula
print(fruta.count("a")) #Contara cuantas "a" tiene
print(fruta.isnumeric()) #Nos dice si es un número o no
print("1".isnumeric()) #Si le pongo este string nos dice True

verdura = "APIO"
print(verdura.lower()) #Todo será en minúscula

#En el momento que hacemos una transformación veremos si cambio
print(fruta.upper().isupper()) #fruta="limonada" esta en mayuscula luego de convertirla en mayuscula?
print(verdura.lower().isupper()) 

#Comprobar si una palabra empieza con ciertos caracteres
print(fruta.startswith("li"))
print(fruta.startswith("o"))
print(fruta.startswith("Li"))


