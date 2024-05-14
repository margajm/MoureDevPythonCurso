""" Operadores Aritmeticos """
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 // 3) # Una flor division, division aproximada a un numero entero
print(10 % 2) #Modulo para saber lo que queda, si tiene algún múltiplo
print(2 ** 3) #Calcular un exponente

#Con los operadores podemos hacer operaciones
print("Hola" + "Python" + "¿Qué tal?")

#No podemos concatenar datos diferentes
#print("Hola" + 5) Aqui nos da ERROR!
#Por ello debemos convertirlo a string
print("Hola" + str(5))


#Podemos hacer operaciones matemáticas
print(2 **3 +3 - 7 / 1 // 4)

#Se puede multiplicar
print("Hola" * 5)
print("Hola" * (2**3))

#Es un float porque nos da 5.0
my_float = 2.5 * 2
print("Hola" * int(my_float))

### Operadores Comparativos ###

print( 3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)
print( 3 > 4 == 2)
print( 3 > 4 > 2)
print("Fin")

#Tambien podemos comparar cadenas
#Compara mediante ordenacion alfabética
#No cuenta los caracteres para eso es len()
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" <= "Python")
print("Hola" >= "Python")
print("Hola" == "Python")
print("Hola" != "Python")
print("Hola" >= "Bola") 
print("Hola">= "Zola") #Ordenacion Alfabetica por ASCII
print("aaaa" >= "abaa") # b es mayor que a
print(len("aaaa")>= len("abaa")) #Cuenta caracteres

### Operadores lógicos ###
#True o False
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")

print(3 < 4 and "Hola" <"Python")
print(3 < 4 or "Hola" < "Python")

print(3 < 4 or ("Hola" > "Python" and 4 == 4) )
print( not (3 > 4) )