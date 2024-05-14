### Functions ###
'''
Podemos tener funciones simples, con parámetros
'''

#Función simple
def my_function ():
    print("Esto es una función")
    #my_function() NO se pone aquí porque crea un bucle infinito de llamar a la función.

my_function()
my_function()
my_function()




#Función con parámetros
#Aquí podemos ponerle 2 parámetros para poder usar 2 valores.
# Se necesita si o si pasarle 2 valores si hacemos esto.
def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
# sum_two_values (5, 3, 2) Nos saldrá error porque solo son 2 parámetros.
sum_two_values("5", "7") #Aquí lo que hace es concatenar.

'''
El tipado es fantasía en Python, la variable toma el tipo de dato del valor que le pongamos dentro.
Por ello si le ponemos una tupla pues se comerá la tupla.

Lo único que podemos hacer es comprobar el valor que se ingresó.
Por ejemplo:
Si comprueba que si es un entero entonces ejecuta, sino no.
'''
sum_two_values(1.4, 5.2)




#Segundaa función
'''
Sabemos que el tipado es débil o dinámico en Python, por ello :
- Podemos colocar ":" y especificar que tipo de dato es, para orientarle al programador.
Ya que no servirá para el usuario pero si para que el programador sepa que tipo de dato debe ir allí.
'''
def divide_two_values (first_value2: int, second_value2):
    print(first_value2 / second_value2)

divide_two_values(5, 7)
divide_two_values(54754, 71231)
#divide_two_values("5", "7") Aqui nos saldrá error porque no podemos dividir 2 strings.




#Función con return
#Cuando queremos que la función haga algo y nos retorne.
def sum_two_values_with_return(first_value, second_value):
    #Ponemos return 
    return first_value + second_value

#No se imprime nada en la consola.
sum_two_values_with_return(10, 5)

#Podemos guardamos en una variable el resultado del return
my_result = sum_two_values_with_return(10, 5)
print(my_result)
#También podemos hacer esto para que no almacene y retorne directamente.
print(sum_two_values_with_return(10, 5))

#En cambio si guardamos en una variable el print de la anterior función, no pasará nada.
my_result2 = divide_two_values(5, 2)
print(my_result2) #Sale none, porque no retorna nada.



#Función 4 con variable dentro
def divide_two_values_with_return ( first_value, second_value):
    my_division = first_value / second_value
    return my_division

print(divide_two_values_with_return(10, 5))




#Función 5 
def print_name (name, surname):
    #Estamos formateando con f que al acceder a esos valores serán cadenas de texto.
    print(f"{name} {surname}")

#Puedo cambiar el orden de los parámetros formateandolos de esta manera.
print_name(surname = "Moure", name = "Brais")
#Aquí se imprimió en el orden correcto a pesar que le pasamos los parámetros en desorden.




#Función 6 con valores por defecto
'''
Si alguien se olvidó de colocar algún parámetro, nosotros podemos ponerle
un valor por defecto para que no quede vacío de esta forma:
- En los parámetros o el parámetro colocamos así:

alias = "Sin alias" #Al colocarlo en comillas le indicamos que es string.
'''
def print_name_with_default ( name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure", "MoureDev")
print_name_with_default("Brais", "Moure")





#Función 7 Imprimiendo textos

def print_text(text):
    print(text)

print_text("Hola")



#Función 8 imprimiendo varios textos:
#Para ello ponemos el asterisco por delante para indicar que son varios:
#Así indicamos que para ese parámetro puedo pasarle los valores que se me de la gana.
#Por ejemplo para pasar todos los textos a mayúsculas.
def print_texts(*text):
    print(text)

print_texts("Hola")
print_texts("Hola", "Python", "MoureDev")


#Función con for
#Vemos que lo trata como una tupla los valores, pero podría tratarlo como una lista.
#Pero podemos pasarle los tipos de datos que nos de la gana.
#Solo que así forzamos a pasarle varios parámetros pero todos separados por comas.
def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts("Hola")
print_upper_texts("Hola", "Python", "MoureDev")