# repoCristian

Código PYTHON que permita calcular el área de un triángulo.:

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

area = (base * altura) / 2

print("El área del triángulo es: ", area)


Código PYTHON para introducir dos números por teclado y sumarlos:

num1 = float(input("Introduzca el primer número: "))
num2 = float(input("Introduzca el segundo número: "))

suma = num1 + num2
print("La suma de", num1, "y", num2, "es:", suma)


Código PYTHON para introducir un número por teclado y visualizar el número elevado al cuadrado:
num = float(input("Introduzca un número: "))
cuadrado = num ** 2
print("El cuadrado de", num, "es:", cuadrado)


Escribir un programa en PYTHON que imprima por pantalla la suma de 1234 y 532: 
suma = 1234 + 532
print("La suma de 1234 y 532 es:", suma)


Escribir un programa en PYTHON que imprima por pantalla la resta de 1234 y 532: 
resta = 1234 - 532
print("La resta de 1234 y 532 es:", resta)





Escribir un programa en PYTHON que imprima por pantalla la multiplicación de 1234 y 532:
multiplicacion = 1234 * 532
print("El resultado de la multiplicación de 1234 y 532 es:", multiplicacion)


Escribir un programa en PYTHON que imprima por pantalla la división de 1234 entre 532:
division = 1234 / 532
print("El resultado de la división de 1234 entre 532 es:", division)


Escribir un programa en PYTHON que imprima por pantalla el módulo de 1234 entre 532 
modulo = 1234 % 532
print("El módulo de 1234 entre 532 es:", modulo)


Escribir un programa en PYTHON que convierta de euros a dólares. Recibirá un número 
decimal correspondiente a la cantidad en euros y contestará con la cantidad 
correspondiente en dólares:

tipo_cambio = 1.22 # tipo de cambio euro-dólar
cantidad_euros = float(input("Introduce la cantidad en euros: ")) # pedimos al usuario que introduzca la cantidad en euros
cantidad_dolares = cantidad_euros * tipo_cambio # calculamos la cantidad equivalente en dólares

print(cantidad_euros, "euros equivalen a", cantidad_dolares, "dólares.")


Escribir un programa en PYTHON que calcule el área de un rectángulo del cual se le 
proporcionará por el teclado su altura y anchura (números decimales):

altura = float(input("Introduce la altura del rectángulo: "))
anchura = float(input("Introduce la anchura del rectángulo: "))
area = altura * anchura
print("El área del rectángulo es:", area)







Escribir un algoritmo que pida el lado de un cuadrado y muestre el valor del área y del 
Perímetro:

lado = float(input("Introduce el lado del cuadrado: "))
area = lado ** 2
perimetro = 4 * lado
print("El área del cuadrado es:", area)
print("El perímetro del cuadrado es:", perimetro) 


Diseñar un algoritmo que determine el área y el volumen de un cilindro:

1. Pedir al usuario que introduzca el radio del cilindro.
2. Pedir al usuario que introduzca la altura del cilindro.
3. Calcular el área de la base del cilindro: 
   a. Aplicar la fórmula del área del círculo A = π * r^2, donde π es el valor de la constante pi y r es el radio del cilindro.
4. Calcular el área lateral del cilindro:
   a. Aplicar la fórmula del área lateral del cilindro Al = 2πr * h, donde h es la altura del cilindro.
5. Calcular el área total del cilindro:
   a. Sumar el área de la base y el área lateral: At = A + Al.
6. Calcular el volumen del cilindro:
   a. Aplicar la fórmula del volumen del cilindro V = π * r^2 * h.
7. Mostrar en pantalla el área total y el volumen del cilindro calculados. 

Con codigo Python: 

import math

# Pedir al usuario que introduzca el radio y la altura del cilindro
radio = float(input("Introduce el radio del cilindro: "))
altura = float(input("Introduce la altura del cilindro: "))

# Calcular el área de la base del cilindro
area_base = math.pi * radio ** 2

# Calcular el área lateral del cilindro
area_lateral = 2 * math.pi * radio * altura

# Calcular el área total del cilindro
area_total = area_base + area_lateral

# Calcular el volumen del cilindro
volumen = math.pi * radio ** 2 * altura

# Mostrar en pantalla el área total y el volumen del cilindro
print("El área total del cilindro es:", area_total)
print("El volumen del cilindro es:", volumen)
Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la 
misma, y el área (Pi*R) A2 del círculo inscrito:

1.Pedir al usuario que introduzca el radio de la circunferencia.
2.Leer el radio desde el teclado y almacenarlo en una variable llamada "radio".
3.Calcular la longitud de la circunferencia utilizando la fórmula "longitud = 2 * pi * radio", donde "pi" es la constante matemática 3.14159.
4.Calcular el área del círculo inscrito utilizando la fórmula "area = pi * radio^2".
5.Mostrar los resultados de la longitud y el área en la pantalla.

Código Python:
import math

# Paso 1
print("Introduce el radio de la circunferencia: ")

# Paso 2
radio = float(input())

# Paso 3
longitud = 2 * math.pi * radio

# Paso 4
area = math.pi * radio ** 2

# Paso 5
print("La longitud de la circunferencia es:", longitud)
print("El área del círculo inscrito es:", area) 


Calcular el promedio de tres números introducidos por teclado:

# Pedir al usuario que introduzca los tres números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Calcular el promedio
promedio = (num1 + num2 + num3) / 3

# Mostrar el resultado en la pantalla
print("El promedio de los tres números es:", promedio)

