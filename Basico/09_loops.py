### Loops ###

'''
## While
Mientras algo sea verdadero haz algo
'''

my_condition = 0

#Como es verdadero se imprimira infinitamente 
#hasta que se le acabe la memoria al ordenador
while my_condition < 10:
    print(my_condition)
    #Por ello tenemos que hacer que la condición sea diferente
    #Para que pare de ejecutarse
    #Esto seguirá imprimiendo hasta que no cumpla a condición es decir ser menor de 10.
    my_condition +=2 #Asi imprimimos solo pares
   
#En python tenemos la opción de ejecutar en un loop un else
#Así podemos imprimir algo cuando no se cumple.
else:
    print("Mi condición es mayor o igual que 10")

#Aqui ya estamos fuera
print("Se detuvo el bucle 1")

#Un while es un bucle infinito.
while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: #Es opcional
    print("Mi condición es mayor o igual que 10")

'''
#No nos acepta el elif un while
elif my_condition == 10:
    print("Mi condición es igual que 10")
'''
print("Se detuvo el bucle 2")


#Bucle 3
while my_condition < 20:

    my_condition += 2
    print(my_condition)

#Nunca se cumple esta condición porque solo son pares.
    if my_condition == 15:
        print("Mi condición es 15")

    print("Mi condición es menor que 20")

print("Salimos del bucle 3")
#Pero ahora nuestra variable vale 20
print(my_condition)

my_condition1 = 0

#Bucle 4
while my_condition1 < 20:

    my_condition1 += 1
    #Ahora si se cumple por aumentar de 1 en 1. 
    if my_condition1 == 15:
        print("Mi condición es 15")

    print(my_condition1)

print("Salimos del bucle 4")

#Bucle 5
#Podemos detener por ejemplo cuando tenemos que calcular
#Y parar cuando se cumple una condición concreta.

while my_condition1 < 30:
    my_condition1 += 1
    if my_condition1 == 25:
        print("Se detiene la ejecución")
        break #Con esto rompemos el bucle.
    print(my_condition1)

print("El bucle 5 acabó")

#Bucle FOR
'''
Nos sirve para iterar un listado de elementos, como una lista, tuplas, sets, diccionarios.
Un for se va a repetir tantas veces como elementos tengamos.
Cada vez que le de vuelta al for accedera a cada elemento.
'''

#Listas sirven para guardar elementos en forma ordenada.
my_list = [35, 24, 62, 52, 30, 30, 17]


#A estos valores hoy los llamaremos element
for element in my_list:
    print(element)  

print ("Se imprimió la lista")

#Tuplas son inmutables
my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)

print ("Se imprimió la tupla")


#Sets guardan elementos que no se pueden repetir.
my_set = { "Brais", "Moure", 35}

for element in my_set:
    print ( element)

print ("Se imprimió el set")

#Dicts guardan elementos en par clave : valor
my_dict = { "Nombre" : "Brais", "Apellido" : "Moure", "Edad": 35, 1: "Python"}

for element in my_dict:
    print(element)

print ("Se imprimió el diccionario y sus claves")

#Así podemos imprimir los valores del diccionario:
for element in my_dict.values():
    print(element)

print ("Se imprimió el diccionario y sus valores")

#Tambien podemos pasarlo en formato lista
for element in list(my_dict.values()):
    print(element)

print ("Se imprimió el diccionario y sus valores en formato lista")

#Tambien podemos poner else en un bucle For
for element in my_dict:
    print(element)
else:
    print("El bucle for para mi diccionario terminó")

#También podemos usar el break en un bucle FOR
#Así para cuando encuentra algo que queremos
#No podemos poner un elif en un bucle for directamente porque no funciona
#Pero si podemos poner el elif, else, dentro del if que tenemos dentro.
    
for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se continúa ejecutando")
else:
    print("No se encontró")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue #Se desaconseja utilizar ahora en lenguaje moderno.
    #El continue hace una interrupción corta para que si llega a x condición
    #Entonces lo restante del bucle no se ejecute sino que vuelva al inicio.
    #Y de ahi continúa de manera normal hasta el final.
    print("Se ejecuta")
else: #Es opcional
    print("El bucle de dict se acabó")
