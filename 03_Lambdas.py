###Lambdas###
'''
Es una clase de función anónima es decir no tiene nombre

Podemos llamar a la función almacenándola en una variable

Así podemos ir a medida que avanzamos en el código ir creando nuestra función cuando queremos hacer algo muy concreto.
Las funciones son ciudadanos de primer nivel es decir podemos tener funciones dentro de funciones, etc.

- Sirve para funciones pequeñitas
- Con scope del propio fichero
- No son de propósito general. 
'''


sum_two_values = lambda first_value, second_value : first_value + second_value
print(sum_two_values(2,5))

print("Lambda2")
sum_two_values2 = lambda first_value, second_value : print(first_value + second_value)

print(sum_two_values2(3,5)) #None porque está retornando el resultado de imprimir algo y no la suma, ya que pusimos un print en la función.

'''
 el None que vemos impreso en la salida proviene de la llamada a print(sum_two_values2(3, 5)),
 ya que sum_two_values2(3, 5) devuelve None y eso es lo que se imprime después de que se imprime el resultado de la suma (8).
'''

print("Tercer lambda el multiplicador")
multiply_values =  lambda first_value, second_value : first_value * second_value - 3
print(multiply_values(8,2))

def sum_three_values(value):
    #return value + sum_three_values (first_value + second_value) NO PODEMOS USAR ESTO porque ya forma parte de la propia definición de la lambda.
    return lambda first_value, second_value : first_value + second_value + value

#5 es value, 2 y 4 es el first_value y second value.
print(sum_three_values(5)(2,4))