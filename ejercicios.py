#ejercicio 1
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

area = (base * altura) / 2

print("El área del triángulo es: ", area)

#ejercicio 2

num1 = float(input("Introduzca el primer número: "))
num2 = float(input("Introduzca el segundo número: "))

suma = num1 + num2
print("La suma de", num1, "y", num2, "es:", suma)

#ejercicio 3
num = float(input("Introduzca un número: "))
cuadrado = num ** 2
print("El cuadrado de", num, "es:", cuadrado)


#ejercicio 4
suma = 1234 + 532
print("La suma de 1234 y 532 es:", suma)

#ejercicio 5
resta = 1234 - 532
print("La resta de 1234 y 532 es:", resta)


#ejercicio 6
resta = 1234 - 532
print("La resta de 1234 y 532 es:", resta)


#ejercicio 7
division = 1234 / 532
print("El resultado de la división de 1234 entre 532 es:", division)

#ejercicio 8
modulo = 1234 % 532
print("El módulo de 1234 entre 532 es:", modulo)

#ejercicio 9
tipo_cambio = 1.22 # tipo de cambio euro-dólar
cantidad_euros = float(input("Introduce la cantidad en euros: ")) # pedimos al usuario que introduzca la cantidad en euros
cantidad_dolares = cantidad_euros * tipo_cambio # calculamos la cantidad equivalente en dólares

print(cantidad_euros, "euros equivalen a", cantidad_dolares, "dólares.")

#ejercicio 10
altura = float(input("Introduce la altura del rectángulo: "))
anchura = float(input("Introduce la anchura del rectángulo: "))
area = altura * anchura
print("El área del rectángulo es:", area)



#ejercicio 11
lado = float(input("Introduce el lado del cuadrado: "))
area = lado ** 2
perimetro = 4 * lado
print("El área del cuadrado es:", area)
print("El perímetro del cuadrado es:", perimetro) 

#ejercicio 12
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


#ejercicio 13
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

#ejercicio 14
# Pedir al usuario que introduzca los tres números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Calcular el promedio
promedio = (num1 + num2 + num3) / 3

# Mostrar el resultado en la pantalla
print("El promedio de los tres números es:", promedio)
