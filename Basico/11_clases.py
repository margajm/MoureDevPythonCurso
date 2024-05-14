### Clases ###
'''
Es otro gran concepto dentro de los lenguajes orientados a objetos.
- Son una gran forma de agrupar código, dividir, de dotar de funcionalidad y contexto.

Si tenemos una clase persona puede que dentro tengamos:
- Una función llamada dormir
Identificar el código dentro de un pambito lógico.
'''

#Los nombres de las clases según las buenas prácticas
'''
- Se empieza en mayúsculas
- Sin guiones
'''
#Esta clase 1 no hace nada.
class MyEmptyPerson: 
    pass #no hace nada es código nulo

print(MyEmptyPerson)
print(MyEmptyPerson())




#Clase 2

'''
Las clases necesitan hacer algo, por ello usamos parámetros.

- Y usamos un constructor de clase

'''

class Person:
    def __init__(self, name, surname):
        pass #Le ponemos porque no tiene nada y es nulo.

'''
No está bien tener un fichero donde mezclemos funciones con clases.

- Lo mejor sería tener un fichero que se llamara Person dónde ahí seria el unico lugar que tuviera la clase.
- Desde ahí llamar desde fuera las clases.

- self es requerido siempre, se refiere a la clase misma.
- Con def creabamos una función, pero si hacemos:

def _init_(Self) Se vuelve un constructor de clase

'''

#Le pasamos la clase 2 con unos parámetros
#Pero no podemos acceder a los valores de esta persona
#Le llega el name, surname pero hacíamos pass con los datos, así que nulo se acabó.

my_person = Person("Brais", "Moure")
print(my_person)
#print(my_person.name)



#Clase 3

'''
Los valores que le llegan a la clase persona ahora si fueron almacenados.
- El self es obligatorio si queremos hacer un constructor.
- Self se refiere a el mismo a la clase persona en este caso.


Por ello aquí usamos self y le asignamos propiedad name, surname.
- En el momento que le asigno los valores pasan a existir fuera.
- Por ello puedo acceder a ella desde afuera.
'''

class Person2:
    #def __init__(self) es obligatorio para que Python interprete que es un constructor.
#Para que sea capaz de tener el self y guardar sus propiedades.
    def __init__(self, name, surname):
        #Aquí le asignamos a la clase las propiedades
        #Le podemos pasar listas, etc, veamoslo como una función.
        self.name = name
        self.surname = surname

my_person2 = Person2("Brais", "Moure")
print(my_person2.name)
#Formateo inferido que es la mejor porque agarra el valor de las variables tal cual
print(f"{my_person2.name} {my_person2.surname}")



#Clase 4
#Podemos pasarle defrente con el sef sin poner en parámetros sus propiedades.
#Podemos tener propiedades que definamos dentro del constructor o fuera.
class Person3:
    def __init__(self):
        self.name = "Lisa"
        self.surname = "Moure"

my_person3 = Person3()
print(f"{my_person3.name} {my_person3.surname}")


#Clase5
'''
Le pasaré un nombre, un apellido, pero no podremos acceder desde fuera a esas propiedades.
- Ya no almacenamos el valor de name y surname.
- Sino que creamos una propiedad almacenada que es fullname.
'''
class Person4:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"

my_person4 = Person4("Chete", "Moure")
#Ya no puedo acceder a nombre y apellido.
#Solo tengo una propiedad llamada fullname.
print(my_person4.full_name)


#Clase 6 con función
'''
Tenemos una clase persona que tiene un constructor de clase 
Y una función que es caminar.

- Dentro de la propia clase para llamar a la misma clase es con self.

Si yo tengo un constructor, inicializador o función:
- Uno de los parámetros que le puedo pasar y funcionará por arte de magia es self.
- Si yo le paso self accedere a todo lo que este guardado dentro de la clase.
'''

class Person5:
    def __init__ (self, name, surname):
        self.full_name = f"{name} {surname}"

    #Una función dentro de una clase le podemos pasar self.
    #No debemos llamar a person porque está dentro de la clase
    def walk(self):
        print(f"{self.full_name} Está caminando")

my_person5 = Person5("Plu", "Moure")
print(my_person5.full_name)
my_person5.walk()

#Clase 7
#Clase con alias con valor defecto o parámetro con valor por defecto.

class Person6:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} {alias}"
    
    def dance (self):
            print(f"{self.full_name} está bailando")

my_person6 = Person6("Petolon", "More")
print(my_person6.full_name)
my_person6.dance()

#Al darle un valor al alias, ahora se elimina el valor por defecto.
my_other_person = Person6("Yuca", "Moure", "Yuyu")
print(my_other_person.full_name)
my_other_person.dance()


#Clase 8
#Incluso podemos hacer que se imprima con paréntesis el alias

class Person7:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"
    
    def dance (self):
            print(f"{self.full_name} está bailando")

my_person7 = Person7("Petolon", "More")
print(my_person7.full_name)
my_person7.dance()

#Podemos acceder al valor almacenado y cambiarle.
my_other_person2 = Person7("Chibi", "Moure", "Mimi")
print(my_other_person2.full_name)
'''
Yo puedo acceder a mi clase, puedo acceder a una propiedad que tenga y cambiarla ya no con el constructor.
- El constructor para crear por primera mi instancia de mi clase.
- Entonces una vez lo tenemos creado podemos hacer lo que queramos con el.
- Aquí llamamos a la operación de caminar o llamar a el valor full name por ejemplo y cambiarle su variable.

'''
#El constructor de clase no es inmutable porque podemos cambiarle los valores como hicimos.
#Asi lo que le pasamos al constructor de clase importa poco porque ya le cambiamos los valores.
#Aquí NO le dimos nombre, apellido y alias, simplemente lo cambiamos por una string.
my_other_person2.full_name = "Hector, de León (El loco de los perros)"
print(my_other_person2.full_name)

'''
Si le quitamos el valor por defecto del alias, 
y no le agregamos ningún valor cuando llamamos a la función, saldrá error.
- Pero al darle por defecto ya no se necesecita definir el alias.
'''
#El tipado en Python es débil
#Ahora podemos decir a full name que es un número por ejemplo.
my_other_person2.full_name = 777
print(my_other_person2.full_name)





#Clase 9
class Person8:
    def __init__(self, name, surname, alias = "Sin alias"):
        #Aparte de imprimirse con paréntesis, podemos que sean asteriscos o lo que fuese.
        #Porque esto es simplemente una cadena de texto.
        self.full_name = f"{name} {surname} ***{alias}***"
    
    def dance (self):
            print(f"{self.full_name} está bailando")

my_person8 = Person8("Galleta", "More", "Garfield")
print(my_person8.full_name)
my_person8.dance()


#Clase10
#Privatizando variables, dando permisos solo de lectura y no escritura para que no se modifiquen.
'''
Aquí haremos que full name sea normal
Y el name y surname privados para que no los pueda modificar
'''

class Person9:
    def __init__(self, name, surname, alias = "Sin alias"):
         self.full_name = f"{name} {surname} ({alias})"
         #Privatizando
         self.__name = name 
         self.__surname = surname

    def walk(self):
              print(f"{self.full_name} está caminando")

my_person9 = Person9("Amercia", "Sueño")
print(my_person9.full_name)
my_person9.walk()

'''
Ahora esto nos sale error porque ya no podemos acceder a las propiedades porque están privatizadas.

print(my_person9.__name)

'''

#Clase 11
#Podemos acceder al valor de una propiedad privatizada pero NO modificarlo.
class Person10:
    def __init__(self, name, surname, alias = "Sin alias"):
         self.full_name = f"{name} {surname} ({alias})" #Propiedad pública.
         #Privatizando
         self.__name = name #Propiedad privada

    #De esta forma accedemos al parámetro privatizado pero NO podemos modificarlo.
    def get_name(self):
     return self.__name

    def walk(self):
              print(f"{self.full_name} está caminando")

my_person10 = Person10("Amercia", "Sueño")
print(my_person10.full_name)
#Ahora sí podemos acceder al nombre pero no modificarlo.
print(my_person10.get_name())
my_person9.walk()

#Para acceder y modificar debería crear un set.
#Lo correcto sería que todo fue privada y uno acceder a la par pero no pudiera modificarla.