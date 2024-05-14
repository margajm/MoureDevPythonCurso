#Variables, concatenar y tipos de datos, Python y su tipado debil.
my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)
print(type(my_int_variable))

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenación de variables en un print
"""print puede imprimir varias cosas con la coma
Aqui lo que hizo fue en realidad concatenar todo y volverlo un string 
incluyendo el número"""
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este el valor de:",my_bool_variable)

#Aqui lo podemos ver también
print(my_string_variable, my_int_to_str_variable, my_bool_variable)

#Pruebas raras: Print es una funcion NO un tipo de dato
print(type(print("Mi print"))) #Tipo "NoneType"

#Funciones del sistema
print(len(my_string_variable)) #len cuenta el número de caracteres incluyendo los espacios

#Variables en una sola línea
#Es peligroso, pero si estan muy relacionadas se puede pero no es buena práctica porque dificulta el mantenimiento del código
name, surname, alias, age = "Brais", "Moure", "MoureDev", 35
print("Me llamo:", name, surname, "Mi edad es:", age, "Y mi alias es:", alias)

#Inputs
#No son comunes, pero si cuando estamos usando la terminal y asi
#Una variable puede cambiar su valor
'''
name = input("¿Cuál es tu nombre?")
age = input("¿Cuántos años tienes?")
print(name)
print(age)

'''


#Cambiamos el tipo de dato de la variable
#No tiene un tipado fuerte, podemos cambiarle por eso.
name = 35
age = "Brais"
print(name)
print(age)

#¿Forzamos el tipado?
#No, porque es un lenguaje de tipado débil
addres: str = "Mi direccion"
addres = True
addres = 1.2
print(type(addres))

#Esto tiene más sentido en los inputs
addres: str = input("¿Cual es tu dirección?")
print(addres)
print(type(addres))