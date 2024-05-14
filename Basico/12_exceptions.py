### Exception Handling ###
'''
Muchas veces cometemos errores sin querer, y cuando pasa un error la app se muere, se para.
- Y cuando pasa el error no se sabe por qué paso.
- Por ello es importante manejarlo.

Tipos de excepciones:
Try
- Lo usamos si queremos controlar errores lo metemos en un try.

Try {
Corre un bloque de código
}

Except:
- Si este código produce una excepción, es decir falla y da un error:
Entonces se va a ir por un bloque que se llama "except".
except: 


Else:
- Si no se produce una excepción se va por el bloque de else.

Finally:
- Pase lo que pase se de una excepción o un else, se va por el bloque de finally.
- Esto es cuando hemos definido 3 bloques.
'''

#Ejemplo 1 : Una operación normal de 2  números
#Aqupi definimos 2 números
numberOne = 5 
numberTwo = 2
print(numberOne + numberTwo)

#En Python tenemos tipado dinámico, que puede cambiar de un tipo de dato a otro. 
numberTwo = "1" #Cambiamos a un string 
#print(numberOne + numberTwo) #Nos da error y se detuvo el programa.



#Ejemplo 2
#No sirve para manejar los errores poner un if y else porque igual nos da error y no sale otra cosa.
'''
if numberOne > 3:
    print(numberOne + numberTwo)
else: 
    print("No se cumplió")
'''




#Ejemplo 3
#Aquí NO nos da error, pero estamos controlandolo manualmente.
#Esto estaría bien en el caso de que yo esté seguro cuál es el criterio que yo tengo que comparar. 
'''
Con esto no tenemos un manejo de excepciones, 
sino un criterio de aceptaciones en caso se cumpla sale algo y en caso no, no.

if type(numberTwo) == int:
    print(numberOne + numberTwo)
else:
    print("No se cumplió")
'''




#Ejemplo 4  
#Try except

#Lo correcto ###
#De esta forma no se muere el programa
#No se ejecuta esa parte del código, pero continúa con lo demás.
try: 
    #Si esta línea falla, salta directamente al except:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")






#Ejemplo 5
#try except else
#Cuando no se ejecuta el else
#Si nos da la gana podemos añadirle algo más cuando falla.

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    #Se ejecuta si se produce una excepción.
    print("Se ha producido un error 2")
#Este else no se ejecutó porque se produjo una excepción.
else:
    print("Hagamos otra cosas entonces")

'''
Se puede hacer un try except dentro de un try except?
- Si, se pueden anidar, pero tendría sentido si se quieren hacer excepciones muy complejas.
'''




#Ejemplo 6
#Cuando se ejecuta el else

numberOne = 5 
numberTwo = 2

#Vemos que si NO se produjo ningún error se ejecuta el try
# y se imprime el else, porque este solo se ejecuta si:
# - El bloque de código del try se ejecutó correctamente.
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error 2")
except:
    print("Se ha producido un error 3")
#Este else no se ejecutó porque se produjo una excepción.
else:
    #Se ejecuta si no se produce una excepción.
    print("La ejecución continúa correctamente")




#Ejemplo 7
#El finally 
    
numberTwo = "1"

'''
El finally se ejecuta siempre se produzca o no un error.
- En este caso no se produjo ningún error.
'''
    
try: 
    print(numberOne + numberTwo)
    print("No se ha producido un error 7")
except:
    print("Se ha producido un error 7")
else:
    #Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente 7")
finally:
     #Se ejecuta siempre el finally
    print("La ejecución continúa 7")


#Ejemplo 8
#El finally  cuando se produce un error
'''
El finally se ejecuta siempre se produzca o no un error.
- Siempre que hay un "Try" existe un "Except.
- Pero el else y el finally es opcional.
'''
    
try: 
    print(numberOne + numberTwo)
    print("No se ha producido un error 8")
except:

    print("Se ha producido un error 8")
else: #Opcional

    #Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente 8")

finally: #Opcional

    #Se ejecuta siempre el finally
    print("La ejecución continúa 8")



#Nos salimos del try except y volvimos a fallar.
#Pero nos dice que es un type error.
#print (numberOne + numberTwo)





#Excepciones por tipo de dato
'''
De esta forma controlamos los errores de tipo de dato
'''

#Ejemplo 9

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")

except TypeError:
    #Se ejecuta si se produce una excepción o falla el try
    print("Se ha producido un error de tipo de dato")



#Ejemplo 10 : ValueError
'''
Si le colocamos un ValueError no hace nada y nos da error.
Porque solo le estamos diciendo:
- Controlame los errores de valor.
Y en este caso es un TypeError
'''
#Aquí dará error y se detendrá todo el programa.
'''
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")

except ValueError:
    #Se ejecuta si se produce una excepción o falla el try
    print("Se ha producido un error de tipo de dato")
'''



### Ejemplo 11 ###
'''
Podemos controlar varios tipos de errores.
- Debido a que es un TypeError ignorará el except de Value Error y pasará defrente a donde corresponde.
- De esta forma podemos controlar según el tipo de error que se produzca y ejecutar un código muy concreto.
'''
    
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")

except ValueError:
    print("Se ha producido un ValueError")

except TypeError:
    print("Se ha producido un TypeError")





#Ejemplo 12
'''
Podemos capturar errores muy concretos como el tipo de valor
- Simplemente le metemos en el except el tipo de valor y listo.
'''

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")

#De esta forma le ponemos un error muy concreto.
#e podemos nombrarlo comos nos de la gana solo es para tener una variable de este tipo de error.
except ValueError as e:
    print("Se ha producido un ValueError")

except TypeError:
    print("Se ha producido un TypeError 2")





#Ejemplo 13
#Captura de la información de las excepciones
'''
Supongamos que queremos:
-  capturar la excepción y :
- La información de consola que nos sale en los errores.

Aquí ya sabemos que nuestro programa falla con el TypeError:
Pero en caso no sepamos siempre queremos saber:
- ¿Por qué se ha producido un error?
- ¿En dónde se ha producido el error?

Imaginemos que pasó a producción, llegó al usuario, y no tenemos el código, la terminal.
- En ese caso vamos a querer saber cuál fue el error.
- Así le damos feedback del error al usuario.
- Una cosa es que la app falle y no se rompa.

En caso no querramos informar al usuario:
- Podriamos informarnos con datos.
- Escribir un log que se produjo un error.
- Integrar una herramienta de analítica y control de errores 
- Para que si está en el otro lado del mundo nos diga cuál fue el error.

*No se trata de llenar el código de try excepts*
- Se trata de que nuestro código no produzca errores.
- Si se produce un error lo siguiente será corregirlo


Cuando la app se rompe por consola vemos la información.
Pero cuando no se rompe y lo tenemos controlado se va al except y hacemos lo que nos da la gana.
'''

#Ejemplo 13
#Captura de la información de las excepciones
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")

except ValueError as errorcito:
#Capturando en una variable en los errores
    print(errorcito) 
    #Cuando se imprime tenemos lo mismo que antes se imprimía en la consola un traceback.
    #La diferencia es que antes lo imprimía cuando paraba todo el programa porque falló, pero ahora solo imprime y continuará con lo siguiente del código.
    #Esta información la podríamos escribir en un log, o pasarle al usuario, o a un faiarfails analytic y nos lo pasamos entre devs para saber cuál y en qué línea.
    '''
    Por ello hay casos donde:
    - No se hace nada con el error
    - Que hacemos algo.
    - Que queremos capturar la info y hacer algo.
        - Que aparte de capturar el tipo de error queremos hacer algo con la información.
    '''
except TypeError: #Tenemos que ponerle el error si lo dejabamos con el ValueError que no es su error se tira todo el programa.
    print("Se ha producido un TypeError 3")


#Ejemplo 14
#Usando Exception
'''
Exception es una exception genérica 

En este caso sería:
Si en el caso el error que se produce aquí NO es un ValueError,
entonces ve por el bloque de Exception.

Es decir "Sea lo que sea el error se controla, no importa si no sé que tipo de error es".
- Es lo mismo que poner

except:

'''

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")

#Si solo dejamos esto, el programa entero falla.
except ValueError as error:
    print(error)

#Pero con el except ya lo controlamos.
#De igual forma podemos capturarle la información del error.
except Exception as exception:
    print(exception)

