### 1. El famoso FizzBuzz
'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
  - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

'''

#Pensamos en un bucle para que itere cada elemento.
#BUscamos en Stackoverflow o google para ver como lo hicieron otros y vemos rangos.

print("Reto Fizzbuzz")

def fizzbuzz ():
    
    for index in range (100):
        print(index)

#Llamamos la función

#fizzbuzz() #Nos imprime del 0 al 99, NO hasta el 100 :c

'''
Creamos otra a ver
'''

def fizzbuzz2():
    for index in range(1, 100):
        print(index)

#fizzbuzz2() #Empezamos desde el 1, pero NO llega al 100.


'''
Probamos ahora hasta el 101 porque incluye el primero pero excluye el rango al último número.

'''

def fizzbuzz3():
    for index in range(1, 101):
        print(index)

#fizzbuzz3()

#Ya cumplimos con imprimir del 1 al 100.

#Ahora nos falta que si múltiplo de 3 imprima fizz o 5 buzz... es decir las condicionales.
'''
Si el índice que estamos inspeccionando su módulo de 3 es igual a 0.
Y si el módulo de 5 es igual a cero.
- Es decir si cumple con ambos módulos entonces imprime "fizzbuzz."

Si es módulo de 3 que diga fizz.
Si es módulo de 5 que diga "buzz"

'''

print("Reto Fizzbuzz: La función final")


def fizzbuzz4():
    for index in range(1, 101):
        #Comprobamos esto primero porque es restrictivo
        #Ya que cuando se cumple una condición, ahí queda.
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

fizzbuzz4()



### RETO 2: ¿Es un anagrama?

'''
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
- Si no tienen la misma longitud, no pueden ser anagramas.
- Comprobar si las palabras son exactamente iguales. Si lo son, según tus instrucciones, no son anagramas.
Ordenar las letras de ambas palabras y luego comparar las versiones ordenadas. Si son iguales, entonces las palabras son anagramas.
*/
'''
print("Reto es un Anagrama")

#Pasaremos parametros a nuestra función que serán las 2 palabras.
#Esto debe devolver un parámetro
def is_anagramita(word_one, word_two):
    #Si las palabras son iguales no es un anagrama
    if word_one == word_two:
        return False
    #Si me apetece poner en mayúscula la primera letra así en realidad sea un anagrama me dará falso.
    is_anagramita("Amor", "Roma")

    #Esto debe devolver un parámetro, debemos comparar si la primera palabra es igual a la segunda.a
    return word_one == word_two

#is_anagramita("amor", "roma")




def is_anagramiwis(word_one, word_two):

    #Lo ponemos en minúscula para que esté en el mismo formato y se pueda comparar bien.
    #if word_one.lower() == word_two.lower():
        #return False
    '''
    Comentamos lo anterior porque queremos ver que así nomás con lo de abajo el código no funciona y sale error.
    '''
    #Le ponemos un sort para que lo ordene en un criterio fijo o alfabéticamente.
    #Si nosotros ordenamos alfabeticamente todas las letras de la palabra, y si las comparamos y nos da la misma palabra quiere decir que estamos ante las mismas letras.
    '''
Las listas de Python tienen un método incorporado list.sort() que modifica la lista in situ y la ordena de menor a mayor alfabéticamente o númericamente. 
También hay una función incorporada sorted() que crea una nueva lista ordenada a partir de un iterable.
el método list.sort() solo aplica para las listas. En contraste, la función sorted() acepta cualquier iterable y lo convierte en una lista.
print(sorted("oveja"))
['a', 'e', 'j', 'o', 'v'] #Ahora tenemos un array de caracteres.
    '''
    #return (word_one).lower().sort()== word_two.lower().sort() Aquí falla porque NO es una lista. ERROR!

    '''
    Probaremos otra vez pero ahora con sorted
    '''
    #return sorted(word_one).lower() == sorted(word_two).lower() Error : El lower no debe ir después que el sorted nos creó una lista en este caso un array de caracteres.

    '''
    Ahora por tercera vez probaremos, también salió error el anterior porque el .lower() es una operación para strings y no para listas, por eso debíamos hacerlo antes.
    Luego lo que debe hacer es ordenarlo y compararlo.
    '''

    return sorted(word_one.lower()) == sorted(word_two.lower()) #Ahora siii nos funcionó.


print(is_anagramiwis("Roma", "amor"))



'''
Aquí tenemos la función ya definitiva.
'''

def is_anagram(word_one, word_two):

    #Si las 2 palabras son iguales en un mismo formato que es minúsculas no es un anagrama.
    if word_one.lower() == word_two.lower():
        return False #Si no es retorna falso y cierra la función.
    
    #Pero si no son iguales continúa y comparame si convirtiendo cada palabra en minúscula y luego en una lista de letras ordenadas ambas listas son iguales.
    return sorted(word_one.lower()) == sorted(word_two.lower())

print("La función final del Anagrama")
print(is_anagram("Roma", "Amor"))

#Fibonacci

'''
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
'''

print("El fibonacci")

#Los dos primeros números del fibonacci son 0 y 1.
#Los siguientes números siempre serán la suma de los 2 anteriores.


def fibonaccito():
    prev = 0
    next = 1

    #Ponemos hasta el 50 porque empezamos en 0, si empezaramos en 1 si sería hasta el 51.
    for _ in range(0, 50):
        #print(_) Con esto es como que vemos el índice.
        print(prev)
        #Sumamos el número anterior con lo que definí como siguiente.
        fib = prev + next
        #Como en la siguiente iteración se volverá a sumar, le asigno el valor de next a prev.
        prev = next
        #Y tenemos que cambiarle el valor a next para que no sean iguales, por ello le aisgnamos el valor de fib que es la suma y nos da el siguiente número.
        next = fib

fibonaccito()


'''
Hora 2:00:00
Si deseas iterar sobre un rango sin asignar los valores a una variable, puedes usar un bucle for con _, que es una convención en Python para indicar que la variable es temporal o insignificante:

Python

for _ in range(5):
    print("Hola")

Este código imprimirá la palabra “Hola” cinco veces, sin almacenar la posición de la iteración en una variable. Es una forma de iterar sin preocuparse por el valor actual del rango, útil cuando no necesitas el número en sí durante la iteración.

Hacemos esto por que el "index" que era el indice que teníamos estaba de más.
El indice es el que te dice, este el numero 1 de fibonacci, 2 de fibonacci y así, y no necesitabamos esa variable.

Sin embargo el (_) igual lo interpreta como una variable.
for index in range(1, 51):


'''
#Números Primos
print("Numeros Primos")

'''
#4
¿ES UN NÚMERO PRIMO?
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */

 Los números primos son aquellos que solo son divisibles entre ellos mismos y el 1, es decir, que si intentamos dividirlos por cualquier otro número, 
 el resultado no es entero. Dicho de otra forma, si haces la división por cualquier número que no sea 1 o él mismo, se obtiene un resto distinto de cero.

'''

'''
¿Qué son los números compuestos?
Cuando hablamos de los números primos, también es importante saber qué son los números compuestos.

Los números compuestos son aquellos que son divisibles por ellos mismos, por la unidad y también por otros números.

Recuerda, el número 1 no se considera ni compuesto ni primo por convenio.

El 25 es un número compuesto. Entonces es divisible por 1, por 25 y por 5. Es decir, 25/25= 1, 25/1= 25 y  25/5=5.

El 14 es un número compuesto y no es primo. Es divisible por 1, por 2, por 7 y por 14. Lo comprobamos: 14/1 = 14, 14/2 = 7 ; 14/7 = 2 y 14/14 = 1.
'''

#E En este caso la función deberá retornar true y en algunos casos false para saber si es o no.
def is_prime():

    for number in range (1, 101):
        
        #Si es primo debe ser mayor que 1
        if number >= 2:
            #Esta variable nos dice si ha encontrado que se puede dividir por otros números.
            is_divisible = False

            #Comprobaremos si NO es primo.
            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break
            '''
            Este es un bucle for que recorre los números desde 2 hasta number - 1. range(2, number)
            genera una secuencia de números empezando desde 2 (inclusive) hasta number (exclusivo). 
            Es importante comenzar desde 2 porque todos los números son divisibles por 1, y si empezamos desde 1,
            siempre sería divisible y no nos daría información útil.


            El operador % calcula el resto de la división entre dos números. Si el resultado de number % index es igual a 0, 
            significa que number es divisible por index sin dejar residuo. En otras palabras, index es un divisor de number.

            Una vez que encontramos un divisor, ya no necesitamos continuar buscando más divisores. Por lo tanto, usamos break para salir del bucle y detener la búsqueda.

            . Si encuentra un divisor, establece is_divisible en True y termina la búsqueda. Si no encuentra ningún divisor, is_divisible permanece como False.
            '''
            #Decimos si es falso que tiene divisores entonces imprime porque es primo.
            if not is_divisible:
                print(number)
    
is_prime()





#7 INVIRTIENDO CADENAS
print("Invirtiendo cadenas")

'''
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
'''

def reverse(text):

    #Cuando ponemos "." son operaciones asociadas a un tipo de dato. 
    #Hay funciones que son propias del lenguaje y no están asociadas a un tipo de dato.
    #Calcula la longitud del texto (es decir, cuántos caracteres hay en el texto) y lo almacena en la variable text_len.

    text_len = len(text)

    #Aquí almacenamos el texto invertido
    reversed_text= " "

    '''
    Recorre los índices desde 0 hasta text_len - 1.
    range(0, text_len) genera una secuencia de números desde 0 hasta text_len - 1, lo que significa que el bucle recorrerá todos los caracteres del texto.
    '''
    for index in range (0, text_len):
        #Imprimimos cada letra recorrida en el fror
        #print(text[index])

        #Añadimos cada letra a la cadena reversa.
        
        reversed_text += text[text_len - index - 1]

    return reversed_text

print(reverse("Hola Mundo"))
print(len("Hola Mundo")) #Len nos dice cuál es la longitud, en este caso cuantos carácteres tiene.


'''
Claro, vamos a desglosar la expresión `text[text_len - index - 1]` paso por paso para entender cómo funciona y por qué se usa para invertir el texto:

1. **`text`**: Este es el string (cadena de caracteres) que estamos intentando invertir.

2. **`text_len`**: Representa la longitud total del texto. Por ejemplo, si `text` es `"Hola"`, entonces `text_len` sería 4 porque hay 4 caracteres en `"Hola"`.

3. **`index`**: Es la variable del bucle que comienza en 0 y va incrementando en 1 en cada iteración del bucle hasta llegar a `text_len - 1`.
 Esto significa que `index` recorrerá todas las posiciones posibles del string, empezando desde la primera posición (0).

4. *text_len - index - 1: Aquí es donde la magia sucede. Esta expresión calcula la posición del carácter que queremos agregar a `reversed_text` en cada paso del bucle.
   - **`text_len - 1`** nos da la posición del último carácter del texto. Por ejemplo, si `text_len` es 4 (como en "Hola"), 
   `text_len - 1` sería 3, que es la posición del último carácter `'a'`.
   -¡¡¡ Al restarle `index`, vamos moviéndonos hacia atrás en el texto¡¡¡. 
    En la primera iteración del bucle (`index = 0`), `text_len - index - 1` es simplemente `text_len - 1`,
    lo que nos da el último carácter. En la siguiente iteración (`index = 1`), nos movemos un carácter hacia atrás, y así sucesivamente.

5. **`text[text_len - index - 1]`**: Accede al carácter en la posición calculada por `text_len - index - 1`.
    En cada iteración del bucle, esto se traduce en tomar el último carácter, luego el penúltimo, y así sucesivamente hasta llegar al primer carácter de `text`.

Por ejemplo, si `text` es "Hola" y queremos invertirlo:
- En la primera iteración (`index = 0`), `text_len - index - 1` es `4 - 0 - 1 = 3`. Entonces, `text[3]` es `'a'`, el último carácter de "Hola".
- En la segunda iteración (`index = 1`), `text_len - index - 1` es `4 - 1 - 1 = 2`. Entonces, `text[2]` es `'l'`, el penúltimo carácter.

Este proceso se repite hasta que se han recorrido todos los caracteres en orden inverso, construyendo así la cadena invertida en `reversed_text`.

'''


'''
La razón por la cual no puedes usar simplemente text_len - 1 para añadir los caracteres a la variable vacía reversed_text en un bucle, 
y esperar que el texto se invierta, es porque text_len - 1 es un valor fijo. Este valor representa siempre la posición del último carácter en la cadena, 
 independientemente de la iteración del bucle en la que te encuentres.

Si solamente utilizas text[text_len - 1] dentro de un bucle para intentar invertir el texto, 
lo que sucedería es que siempre estarías añadiendo el mismo carácter (el último carácter del texto original) a reversed_text en cada iteración del bucle. Como resultado, si tu texto original fuera "Hola", en lugar de obtener "aloH" como resultado, terminarías con "aaaa" (asumiendo que tu bucle ejecute 4 iteraciones, basado en la longitud de "Hola").

La clave para invertir el texto está en acceder a cada carácter del original en el orden inverso, 
empezando por el último y terminando por el primero. Esto se logra ajustando dinámicamente el índice del carácter que estás accediendo en cada iteración del bucle,
lo cual se hace con text_len - index - 1. Esta expresión calcula el índice correcto para acceder a los caracteres en orden inverso durante cada iteración del bucle:

En la primera iteración, index es 0, por lo que accedes al último carácter (text_len - 1).
En la segunda iteración, index es 1, lo que te lleva al penúltimo carácter (text_len - 2), y así sucesivamente.
De esta manera, utilizando text_len - index - 1 en lugar de simplemente text_len - 1, 
aseguras que cada carácter del texto original se añada a reversed_text en el orden inverso, logrando efectivamente invertir el texto.
'''