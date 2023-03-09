"""QA Minds Labs estaría necesitando de un sistema que permita administrar sus cursos.
   En este sentido el sistema debe contar con la posibilidad de crear un  Curso, el cual tendrán un nombre,
   cantidad de alumnos, un estado y cantidad de clases.
    El sistema debe poder dar de alta un Curso.
    El sistema debe permitir buscar un curso y poder modificar su estado (Ejemplo: de No Iniciado a Activo)
    El sistema debe permitir mostrar TODOS los Cursos existentes, como también la posibilidad de mostrar toda
    la información del curso."""


def agregar(nuevos_cursos: list):
    print("--AGREGAR CURSO--")
    nombre = input("Ingresa el nombre del curso:")
    cant_alumnos = input("Ingresa la cantidad de alumnos:")
    cant_clases = input("Ingresa la cantidad de clases:")
    estado = "No Iniciado"
    curso = {
        "Nombre del curso": nombre,
        "Cantidad de Alumnos": cant_alumnos,
        "Cantidad de Clases": cant_clases,
        "Estado": estado
    }
    nuevos_cursos.append(curso)
    print(nuevos_cursos)


def buscar(bsq: list):
    print("--BUSCAR CURSO--")
    valor_ingresado = input("Ingresa el nombre del curso que deseas buscar: \n")
    obt = None
    for curso in bsq:
        if curso.get("Nombre del curso") == valor_ingresado:
            obt = curso
            break
    if obt:
        print(f"Detalles del curso ingresado: {obt}")
        modif = input("¿Deseas cambiar el estado del curso a 'Activo'? Responde s/n: \n")
        if modif == "s":
            curso["Estado"] == "Activo"
            print(curso)
        else:
            pass
    else:
        print("En este momento no contamos con el curso ingresado")

def mostrar(most: dict):
    print("--MOSTRAR CURSOS DISPONIBLES--")
    print(most)
    answer = input("¿Desea ver algun curso en especifico? Responda s/n:\n")
    if answer == "s":
        valor_ingresado = input("Ingrese el nombre del curso que desea ver: \n")
        obt = None
        for curso in most:
            if curso.get("Nombre del curso") == valor_ingresado:
                obt = curso
                print(obt)
                break

QA_Minds = []

while True:
    opcion = input(f"¿Desea Agregar, Buscar&Modificar, Mostrar los cursos o salir? Responda con -a/b/m/s- : \n")
    if opcion == "a":
        agregar(QA_Minds)
    elif opcion == "b":
        buscar(QA_Minds)
    elif opcion == "m":
        mostrar(QA_Minds)
    elif opcion == "s":
        exit_confirm = input("Usted ha seleccionado abandonar el menú, ¿esta seguro? \n "
                             "La información ingresada anteriormente se eliminara permanentemente. Responda s/n \n")
        if exit_confirm == "s":
            break
        else: pass
    else:
        print(f"La opción igresada no esta disponible.")


