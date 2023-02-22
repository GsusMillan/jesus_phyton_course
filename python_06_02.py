"""Entregar siguientes ejercicios como python_06_02.py:
Escribe un script que dado el día,mes y año de nacimiento de una persona determine lo siguiente:
Cuántos años tiene.
Si en lo que va del año ya cumplio o no.
Determinar a qué generación pertenece:
La generación silenciosa. Nacidos entre 1920 y 1939.
Los baby boomers. Nacidos entre 1940 y 1959.
Generación X. Nacidos entre 1960 y 1979.
Generación Y o millennials. Nacidos entre 1980 y 1989.
Generación Z. Nacidos entre 1990 en adelante.
Extra: Utilizar libreria de datetime para obtener mes y año."""
import datetime

day = int(input("Ingresa tú día de nacimiento:"))
month = int(input("Ingresa tú mes de nacimiento:"))
year = int(input("Ingresa tú año de nacimiento:"))

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
actual_day = date.strftime("%d")
actual_day = int(actual_day)
actual_month = date.strftime("%m")
actual_month = int(actual_month)
actual_year = date.strftime("%Y")
actual_year = int(actual_year)

def edad(anio):
    edad_result = (actual_year - anio)
    return edad_result


edadd = edad(year)
cumplio = month <= actual_month and day <= actual_day
if cumplio == False:
    print(f"Actualmente tienes {edadd-1} años, Este año cumpliras {edadd} años")
else:
    print(f"Ya cumplio años, tu edad es {edadd} años")


if year >= 1920 and year <= 1939:
    print("Perteneces a La generación silenciosa")
elif year >= 1940 and year <= 1959:
    print("Perteneces a La generación de Los baby boomers.")
elif year >= 1960 and year <= 1979:
    print("Perteneces a La generación X")
elif year >= 1980 and year <= 1989:
    print("Perteneces a La generación Y o millennials")
elif year >= 1990:
    print("Perteneces a La generación Z")


