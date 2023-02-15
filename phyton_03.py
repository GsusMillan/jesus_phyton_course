print("¿Cuál es su nombre?")
nombre = "Jesus"
print("¿Cuál es su edad?")
edad = 25
print("¿En que ciudad vive")
ciudad = "Mazatlán"
print("¿Estado civil?")
estado_civil = bool(False)
if(estado_civil == False):
    estado_civil = "soltero"
else:
    estado_civil = "casado"
print(estado_civil)
print("Ingrese un valor entre 1 y 100")
primer_valor = 20
print("Ingrese un valor entre 100 y 200")
segundo_valor = 140
resultado = (primer_valor / segundo_valor)
print(f"Mi nombre es {nombre}, mi edad es {edad}, soy de la ciudad de {ciudad} y mi resultado es {resultado}")
