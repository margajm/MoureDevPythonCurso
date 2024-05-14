#Expresiones regulares
'''
Sirven para inspeccionar si una cadena de texto tiene "n" cosas.
Comprueba si una cadena de texto tiene o no ciertos elementos.
Se comprueban letra a letra a ver si tienen lo que queremos buscar.
Son capaces de decirnos si la cadena de texto tiene lo que buscamos y retornarnos las ocurrencias de lo que coincide de lo que coincide con las expresiones regulares.
Lo tenemos en todos los lenguajes.

- Es como crear una fórmula que le pasaremos a un inspector de expresiones regulares del lenguaje que utilizamos, y va a trabajar con esa forma.

"Hector de León tiene unos videos buenazos de expresiones regulares."

Web para aprender y validar expresiones regulares :
- https://regex101.com/
'''

#Primero tenemos que llamar a su módulo en python.

import re

my_string = "Esta es la lección número 7:Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Lección Manejo de ficheros"

###Match###

#Nos va a ayudar a encontrar un patrón DESDE EL INICIO DE LA CADENA.
#Aquí le decimos si tiene esta frase en nuestra variable.
print(re.match("Esta es la lección", my_string))
#<re.Match object; span=(0, 18), match='Esta es la lección'> Nos dice que lo encontró desde el caracter 0 al 18.


#Consultamos por la otra variable:
print(re.match("Esta es la lección", my_other_string))
#None: Porque no lo encontró allí.

print(re.match("Expresiones regulares", my_string))
#None: A pesar que si lo tiene sale NONE, porque busca solo si tiene el patrón en el inicio de la cadena de texto.











##FUNCIONES REGEX INCORPORADAS EN PYTHON
#re.I o re.IGNORECASE
'''
Este es un modificador que le dice a la función match que ignore las diferencias entre mayúsculas y minúsculas al realizar la coincidencia. 
'''
#Pondremos al Match en una variable
match = re.match("Esta es la lección", my_string, re.I)
print(match)

#span trae una tupla con la posición de inicio y final de la coincidencia encontrada en una cadena de texto.
span = match.span()
print(span)

#Desacoplando la tupla que tiene 2 valores la posición inicial y final.
start, end = match.span()
print(my_string[start:end])


print("Comprobando con un None")

#Comprobando que pasa si lo hacemos con un None
match2= re.match("Esta no es la lección", my_other_string, re.I)

#if not (match2 == None): #Una forma de comprobar
if match is not None: #Otra forma de comprobar
    print(match2)

    start2, end2 = match2.span()
    print(my_other_string[start2: end2])





#Search
#Con search podemos buscar en cualquier parte de la cadena de texto

search = re.search("lección", my_string, re.I)
print(search)

start, end = search.span()
print(my_string[start:end])


#findall
'''
Se utiliza para encontrar todas las ocurrencias de un patrón en una cadena de texto y devuelve una lista con todas las coincidencias encontradas.
'''

findall = re.findall("lección", my_string, re.I)
print(findall) #['lección', 'Lección']




#Split

'''
Se utiliza para dividir una cadena de texto en partes utilizando un patrón de expresión regular como separador.
'''

#Dividimos la cadena a partir del salto de línea
#print(re.split("\n", my_string))

#Dividimos usando los 2 puntos
print(re.split(":", my_string))


#sub
'''
Se utiliza para reemplazar todas las ocurrencias de un patrón en una cadena de texto con otro texto especificado.
'''
print(re.sub("Expresiones", "EXPRESIONES", my_string))

#El operador | se utiliza para proporcionar opciones alternativas en un patrón de expresión regular, es como un "o".
print(re.sub("lección|Lección", "LECCIÓN", my_string))

#Los corchetes "[ ]" definen un conjunto de caracteres, 
#lo que significa que se buscará cualquier carácter que esté dentro de los corchetes. En este caso, los caracteres son "l" y "L".
print(re.sub("[l|L]ección", "LECCIÓN", my_other_string))


##Patterns
'''
 La r antes de las comillas iniciales indica que la cadena es un raw string. En Python, 
 los raw strings son utilizados habitualmente para expresiones regulares porque evitan el procesamiento de caracteres de escape por el propio lenguaje Python. 

 [lL] significa que la expresión puede coincidir con 'l' minúscula o 'L' mayúscula. 
'''

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))


'''
Los espacios en las expresiones regulares son significativos y son tratados como caracteres que deben coincidir exactamente en la cadena de entrada
'''
#pattern2 = r"[lL]ección | Expresiones"

'''
Para que la expresión regular funcione como se espera, 
debes eliminar los espacios alrededor del operador | y asegurarte de que los espacios formen parte de la cadena de caracteres a buscar solo cuando sea necesario. 
'''
pattern2 = r"[lL]ección|Expresiones"
print(re.findall(pattern2, my_string))






#Pattern 3 encontrando números

pattern3 = r"[0-5]" 
print(re.findall(pattern3, my_string)) #Si colocamos solo hasta el 5 nos devolverá un string vacío.

pattern3 = r"[0-9]"
print(re.findall(pattern3, my_string)) #Encontramos el 7, el único número que hay en el string.


#Probemos con Match
print(re.match(pattern2, my_string)) #None

print(re.match (pattern3, my_string)) #Imprime None


#Probando con Search
print(re.search (pattern3, my_string)) #Imprime <re.Match object; span=(26, 27), match='7'>



#Probando con otros patrones
print("Patrones cortos")
pattern4 = r"\d"
print(re.findall(pattern4, my_string))

pattern5 = r"\D"
print(re.findall(pattern5, my_string))


#Este patron buscará cualquier lugar en la cadena donde haya una 'l' seguida inmediatamente por cualquier otro carácter.
pattern6 = r"[l]."
print("Busquemos una l")
print(re.findall(pattern6, my_string))


pattern7 = r"[l].*"
print(re.findall(pattern7, my_string))


print("\nValidando emails")
#Email Validation Regular Expression
email = "mouredev@mouredev.com"
pattern_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern_email, email)) #Busca al inicio del string y retorna un objeto.
print(re.search(pattern_email, email)) #Busca en toda la cadena y retorna un objeto.
print(re.findall(pattern_email, email)) #Busca y retorna una lista.

# Busca y retorna una lista vacía porque esperaba el "."
email3 = "mouredev@mouredev"
print(re.findall(pattern_email, email3))

#Busca y retorna una lista vacía porque esperaba más carácteres luego del "."
email4 = "mouredev@mouredev."
print(re.findall(pattern_email, email4)) 

#Si le ponemos algo después del punto si vale.
email5 = "mouredev@mouredev.es"
print(re.findall(pattern_email, email5))

#Si no le ponemos arroba @ NO vale
email6 = "mouredevmouredev.es"
print(re.findall(pattern_email, email6))

#Si le colocamos doble arroba tampoco vale
email7 = "mouredev@@mouredev.es"
print(re.findall(pattern_email, email7))

#Cambiando el patrón para que acepte 2 arrobas
pattern_email2 = r"^[a-zA-Z0-9_.+-]+@@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email8 = "mouredev@@mouredev.es"
print(re.findall(pattern_email2, email7))

#Podemos visualizar dos dominios gracias a \.[a-zA-Z0-9-.]+$
email9 = "mouredev@mouredev.com.pe"
print(re.findall(pattern_email, email9))

#El símbolo $
'''
En una expresión regular representa el "final de la cadena". Esto significa que la coincidencia debe terminar justo en ese punto,
 asegurando que la expresión regular busque coincidencias hasta el final de la cadena y no en cualquier lugar intermedio.
'''
pattern_email3 = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]"
email10 = "mouredev@mouredev.com.pe"
print(re.findall(pattern_email3, email10))

#Es por ello que si nos acepta gracias a ese $ los demás subdominios también.
pattern_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email11 = "mouredev@mouredev.es.eu.ca"
print(re.findall(pattern_email, email11))


#Probando si le quitamos los números al final para que no los acepte como subdominio
pattern_email4 = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
email12 = "mouredev@mouredev.es.mx.112"
print(re.findall(pattern_email4, email12))


#Quitando el "." para que no acepte subdomnios
pattern_email5 = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-]+$"
email13 = "mouredev@mouredev.es.mx.112"
print(re.findall(pattern_email5, email13))

#Colocando "." para que no acepte subdomnios
pattern_email6 = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
email14 = "mouredev@mouredev.es.pe.mx"
print(re.findall(pattern_email6, email14))

#Quitando "$" para que agarre la primera coincidencia
pattern_email7 = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]"
email15 = "mouredev@mouredev.es.pe.mx"
print(re.findall(pattern_email7, email15))


#¡SIEMPRE DEBEMOS CERRAR NUESTROS PATRONES!
pattern_email8 = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+"
email16 = "mouredev@mouredev.es.pe.mx"
print(re.findall(pattern_email8, email16))