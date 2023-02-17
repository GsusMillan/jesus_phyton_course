"""Entregable ejercicio modulo 5 (python_05.py):
Pide al usuario dos variables a = 12.5 y b = 34, crea funciones que permitan calcular la suma,
resta, multiplicación y división, como también el valor del módulo de b entre a
Crea un método que permita convertir cualquier numero entero y a flotante
Extra: Define una función para convertir de grados Celsius a Fahrenheit,
pide al usuario que ingrese la temperatura en Celsius e imprima la conversión."""
def suma(param1, param2):
    sum = param1 + param2
    return sum
def resta(param1, param2):
    res = param1 - param2
    return res

def multiplicacion(param1, param2):
    mul = param1 * param2
    return mul

def division(param1, param2):
    div = param1 / param2
    return div

def modulo(param1, param2):
    mod = param1 % param2
    return mod

def convierte_enteros(param1: int):
    conv = float(param1)
    return conv

def conversor_celcius_to_farenheit(param1: int):
    parametro1 = float(1.8)
    parametro2 = int(32)
    con = param1 * parametro1
    con += 32
    return con


value_1 = int(input("ingresa un numero:"))
value_2 = int(input("ingresa otro numero:"))
sum = suma(value_1, value_2)
print(f"El resultado de la suma es: {sum}")
res = resta(value_1, value_2)
print(f"El resultado de la resta es: {res}")
mul = multiplicacion(value_1, value_2)
print(f"El resultado de la multiplicación es: {mul}")
div = division(value_1, value_2)
print(f"El resultado de la devision es: {div}")
mod = modulo(value_1, value_2)
print(f"El resultado del modulo es: {mod}")

valor_flotante = int(input("ingresa un numero entero:"))
result = convierte_enteros(valor_flotante)
print(f"El resultado de la conversion a flotante fue: {result}")

celcius = int(input("Ingresa los grados celcius a convertir en Farenheit:"))
show = conversor_celcius_to_farenheit(celcius)
print(f"Los Celcius ingresados equivalen a {show} Farenheit")

"""""EXTRA:
Escribe una función llamada "es_par" que tome un número entero como parámetro y 
devuelva True si el número es par o False si el número es impar.
Luego, escribe un programa que pida al usuario que introduzca un número entero y
utilice la función "es_par" para determinar si el número es par o impar. 
Imprime en pantalla un mensaje indicando si el número es par o impar."""

def es_par(param1):
    return param1%2

num = int(input("Ingresa un numero para verificar si es par o inpar:"))
par_inpar = es_par(num)
if (par_inpar == 0):
    print("El numero ingresado es Par")
else:
    print("El numero ingresado es Inpar")

#error en el nombre del commit