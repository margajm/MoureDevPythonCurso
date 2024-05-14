#importamos my_module pero solo una función en concreto
from Moure_Dev.Python_moureDev.Basic.my_module import sumValues

#my_module.sumValues(5, 3, 1) Esto nos da error

#Porque ahora puedo llamar directamente a mi función que importé
sumValues(5, 3, 1)

'''
Esto me sale error porque solo he importado la función sumValues
printValue("Hola Python!")
'''
### Pero también podemos llamar varias funciones de manera individual:

from Moure_Dev.Python_moureDev.Basic.my_module import sumValues, printValue

sumValues(5, 3, 1)
printValue("Hola Python")

'''
Un Módulo hace operaciones muy concretas
Python también tiene sus propios módulos que por tener instalado podemos usarlo.

Un método es igual a una función no a un módulo, porque:
- Un módulo al final tiene que ser una serie de operaciones y utilidades que intenten resolver problemas con alguna relación.

Un módulo es como una librería.

'''
#import _ Cuando escribimos así nos muestra todos los módulos que tiene el sistema.
#Math es un método de Python 
import math
'''
Escribimos con un "." y nos sale todas las funciones que podemos hacer.
math. 
'''
print(math.pi) #Así podemos acceder al valor de la función

#Aquí es una potencia
print(math.pow(2, 8))




#Podemos importar directamente una función de algún módulo de Python
#Aquí importamos solo la función pi por ejemplo
from math import pi
print(pi)


'''
También podemos importar una función específica de un módulo de Python y asignarle una variable:
Por ejemplo aquí importaremos el exponente y lo guardaremos como "potencia".

'''

from math import pow as potencia
#De nuevo pedimos la potencia de 2 elevado a la 8
print(potencia(2, 8))


from math import pi as PI_VALUE
#Pero si le llamamos por su nombre original fallará porque ya le cambiamos el nombre al importarla.
print(PI_VALUE)
print(pi)

'''
Conclusión:
- Podemos importar todo el módulo
- Solo propiedades concretas
- Incluso importarlas y renombrarlas

'''