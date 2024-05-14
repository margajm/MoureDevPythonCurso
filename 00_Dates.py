### Dates ###

##Tipos básicos de fecha y hora.
'''
Cada uno nos permite trabajar con diferentes funciones concretas y diferenciadas cada uno para ser más eficientes.

datetime = Nos permite agrupar la parte de hora y fecha.
date = Nos permite agrupar solo la parte de hora.
time = Sirve para representar o agruparte la parte de la fecha.

'''



'''
El módulo "datetime" proporciona clases para manipular fechas y horas es decir agrupar los dos tipos de datos.
- Permite operaciones matemáticas con fechas y horas.
- Su principal objetivo es extraer campos de forma eficiente para su posterior manipulación o formateo.

Representación de una fecha, un día, semana, año.
No es un objeto básico por ello tenemos un módulo, porque los objetos básicos fundamentales se reducen a la mínima expresión.
En cmabio este usa código python combinado con objetos de tipo vacío, va a hacer muchas más cosas, pero lo que hace es:
- Encapsular para que entendemos o generemos de una forma más rápida.
'''

#Aquí importamos específicamente la función de datetime

from datetime import datetime

#1. Con esto tendremos la fecha actual!!!

'''
No podemos acceder a este objeto de hora, pero no hemos inicializado el objeto datetime aún.

print(datetime.hour)

Por ello primero lo deiniremos
'''




#Creamos una variable llamada now

'''
Esta es una función que tenemos dentro del propio datetime.
Nos va a inicializar un objeto del tipo date y ahora vamos a irnos a now
'''
#Ya tenemos una fecha inicializada con el valor en que el código pase por aquí.
now = datetime.now()

#print(now) Esto falla porque estamos llamando a datetime que no es nada 

#Ahora si podemos acceder a las propiedades de now.

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
#Esta es una representación única de un tiempo 
#Nosotros en base a un timestamp podemos inferir una fecha.
'''
Es el famoso formato possit.
Si tuvieramos que propagar la fecha o convertirla, o pasarla a través de una llamada a la API.
Sería muy complejo pasarle eñ año, mes, fecha la hora porque eso es un  objeto muy complejo.

Entonces el timestamp dice es el justo momento que corresponde.
Esto es un formato estándar y fijo desde 1970, por ello es más fácil transformarlo a alguna cosa que conozcamos.

'''
timestamp = now.timestamp()
print(timestamp)






#2. Con esto trabajamos con cualquier fechal!!!

'''
Cuando trabajamos por ejemplo con una aplicación con un usuario que está en Marruecos
 y está grabando una hora en base de datos es importante que yo sepa que tiene ese valor localizado en Marruecos,
 para ello le pongo una franja horaria, UTC, etc, 
 para saber que ese GMT-2, SI un usuario
   la recupera desde otra parte del mundo pues tendrá que hacer una conversión.  
'''

#Vamos a querer instanciar el año 2025 por ejemplo.
#Puedo meter los datos que quiero, pero decidí meterle solo el año, el mes y el día.
year_2025 = datetime(2025, 1, 1) #Cuando no le ponemos la hora ni el minuto se pondrá en cero

#Vamos a crear una función para imprimir todo esto
def print_date (date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)
print_date(year_2025)









#Importando solo el time
from datetime import time
'''
Este módulo proporciona varias funciones relacionadas con el tiempo.
Como funcionalidad pues surge datetime y calendar.
Nos permite agrupar solo la parte de hora.
'''

current_time = time()

#print_date(current_time) Esta llamada a la función pasándole time falla, porque quizá hay datos que nos faltan.
print(current_time.hour)
#En la función print_date con "datetime" los minutos se llaman minute, pero aquí se llama min.
print(current_time.min)
#Vemos como cada dato funciona de una manera distinta
'''
Porque "time" es un objeto que en realidad no tiene nada.
Entonces sobre time primero tenemos que lanzar operaciones para después empezar acceder a sus datos.
'''
print(current_time.second)

#Entonces a medida que vamos a crear este objeto, tenemos que trabajar sobre él.
'''
Time es un objeto que nos sirve para encapsular tiempo pero no es un objeto que ya venga rellenado como datetime con now,
nosotros mismos debemos rellenar a "time".

¿Cómo lo rellenamos?
Dándole valores a la hora, el minuto, el segundo.
'''
#Aquí le ponemos 21 con 6 minutos y 0 segundos
current_time = time(21, 6, 0)

'''
También se puede definir un time vacío donde todo sería así.
current_time = time()
current_time = time(0, 0, 0)
'''
print(current_time.hour)
print(current_time.minute)
print(current_time.second)







from datetime import date
'''
Sirve para representar o agruparte la parte de la fecha.
'''
#Instanciamos date 

#current_date = date() Pero como está vacío nos dará error.
current_date = date.today() #Lo inicializamos con la fecha actual

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2024, 4, 3)

print(current_date.year)
print(current_date.month)
print(current_date.day)










#Trabajando con fechas
#Accedemos al año y le sumamos 1 por ejemplo
'''
Podemos acceder a los valores pero no modificarlos de esta manera
current_date.year = current_date.year + 1
print(current_date.year)
'''
#Podemos inicializar de nuevo date y modificarlo de esta manera.
#Sumando 1 al mes
current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.month) #Era 4 ahora es 5 el mes
#Pero la realidad es que no podemos modificar uno en concreto.


#No podemos hacer esta operación porque son distintos tipos
#print(year_2025.date - current_date)


'''Intentaremos imprimir la diferencia entre estas 2 fechas
# diff = year_2025.date - current_date

#diff = year_2025 - current_date
'''

diff = year_2025 - now
print(diff) #272 days, 7:47:59.473366

#Cuando los objetos son del mismo tipo si podemos acceder a ellos.
diff = year_2025.date() - current_date
print(diff) #243 days, 0:00:00

print(year_2025.time()) #00:00:00


from datetime import timedelta
'''
"Con el timedelta si podemos modificar las fechas
Si tenemos 2 fechas nos permitirá operar con ellas.
- Nos sirve para operar y trabajar con diferencias con fechas.
- No sirve para trabajar con fechas como tal, sino con franjas de fechas.

Nos sirve para definir valores absolutos:
- Decir este es un espacio de tiempo que dura X como horas, milisegundos, microsegundos y semanas.
- Sirve para saber en una suscripción cuanto tiempo ha estado activa la persona.
- Podemos extraer de fecha en fecha cuántos días ha estado en cada uno, después creamos un timedelta, obtenemos valores que al final son absolutos y no una fecha como tal.
'''
#200 horas, 100 segundos, 100 microsegundos, 10 semanas
start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
print(end_timedelta / start_timedelta)



