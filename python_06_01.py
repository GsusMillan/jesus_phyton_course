"""Entregar siguientes ejercicios como python_06_01.py:
Escribe un script que dado la edad de una persona y su altura pueda determinar si la misma puede o no
subirse en la montaña rusa “Push-Pull”, dado que se debe ser mayor a 14 años y tener una altura no menor
de 1,62. El script debe ser capaz de informar si puede o no subirse y en el caso de que no, porque razon
(Si por edad, por tamaño u ambas)"""

edad = int(input("Ingrese su edad:"))
altura = input("Ingrese su estatura:")
e_limite = 14
a_limite = "1.62"

if edad >= e_limite and altura >= a_limite:
    print("Edad y Altura adecuada, disfrute nuestra atracción Push-Pull")
elif edad < e_limite and altura < a_limite:
    print("Lo sentimos, NO tienes edad NI estatura suficiente para ingresar a la atracción.")
elif edad < e_limite:
    print("Lo sentimos, NO tienes edad requerida para ingresar a la atracción")
elif altura < a_limite:
    print("Lo sentimos, NO tienes la estatura requerida para ingresar a la atracción")
