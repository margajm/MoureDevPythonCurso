### Conditionals ###
'''
Es la manera de establecer flujos de ejecución en nuestro código.
Ejemplo:
Una pantalla de login para comprobar y llamar al servidor.

Un condicional es un if
"Si esto es así" +  entonces haz esto

También podemos hacer algo cuando la condición no se cumple.
if =  Cuando se cumple una condición.
else = Cuando no se cumple nada
elif = Cuando la condición o condiciones no se cumplen, 
pero ponemos unas alternativas que pueden cumplirse. 

La estructura correcta de los condicionales es:
1. Colocar el if o todos los if
2. Los elif o el elif
3. el else.

El "if not" nos permite comprobar si una condición no se cumple.

'''
#Usamos los booleanos de true o false para las condiciones
my_condition = False

#En el momento que hacemos un if se tiene que cumplir la condición
#Por ello poner el true es algo redundante.
if my_condition:
    print("Se ejecuta la condición del if")

#Solo se imprimirá esto porque la condición
print("Se ejecuta la condición del if")

#Segundo if
#Aqui no le pasamos ninguna condición, pero como tiene algo con valor eso le vale.
my_condition = 5*2 #Vale 10
if my_condition:
    print("Se ejecuta el segundo if")

print("La ejecución 2 continúa")

#Tercer if
#Aqui si comprobamos una condición
#Si es true para adelante lo ejecuta sino no.
if my_condition == 11:
    print("Se ejecuta el tercer if")

print("La ejecución 3 continúa")

#Aqui comprueba si es mayor que 10 
if my_condition > 10:
    print("Se ejecuta el cuarto if")
    #Aquí decimos si la condición es falsa entonces:
else:
    print("Es menor o igual que 10")

print("La ejecución 4 continua")

#Podemos usar los operadores lógicos con las condiciones
#Hacer que se cumplan 2 condiciones.

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor igual que 20")

print("La ejecución 5 continúa")

#6XTO if

my_condition = 5*3

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
#Una condición alternativa cuando las condiciones no se cumplen.
elif my_condition == 1:
    print("Es igual a 1")
else:
    print("Es menor o igual que 10 o mayor igual que 20")

#Si le quitamos la tabulación ya considera que está fuera del if o else.
print("La ejecución 6 continúa")

#Usando el elif
#Aquí veremos que ya no imprime el else, porque comprobó en orden:
#Desde el if, luego vio que en el elif lo cumplía y paró.
my_condition = 5*5

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
#Una condición alternativa cuando las condiciones no se cumplen.
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor igual que 20")

#Si le quitamos la tabulación ya considera que está fuera del if o else.
print("La ejecución 7 continúa")

#Para que esté vacía debo colocar sin espacios.
my_string = ""

#Si tenemos un string vacío nos lo da como false.
if my_string:
    print("Mi cadena de texto no es vacía")

#Pero si hay algún valor dentro lo verá como true.
my_string = "Mi cadena de texto"
    
if my_string:
    print("Mi cadena de texto no es vacía")
#Vemos que también imprime esto porque se cumple también.
if my_string == "Mi cadena de texto":
    print("Estas cadenas de texto coinciden")

#Podemos comprobar si una condición no se cumple con:
my_string = ""

#Aquí le decimos si esto es false o no tiene ningún valor:
if not my_string:
    print("Mi cadena de texto es vacía")