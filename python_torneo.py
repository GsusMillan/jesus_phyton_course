''' QA Minds Lab con motivo de finalizar el modulo de Introducción a Python realizará un torneo de Starcraft 2.
Para ello requiere de un sistema que permita gestionar el torneo.

En este sentido el sistema debe contar con la posibilidad de crear Jugadores, los cuales tendrán
un nombre, un email, puntos ganados y una raza con la que jugarán, el cual pueden ser: Terran, Zerg o Protoss.

Los jugadores también tendrán unestado el cual puede ser: Activo o Inactivo, el cual permitirá poder asociarlo a nuevas partidas o no.

Los jugadores también tendrán un contador de partidas.
Los jugadores también tendrán un contador de puntos.

Las Partidas tienen un nombre (Ejemplo: A vs B) y estan compuestas por dos jugadores que estarán en estado Jugando.
Siempre habrá un ganador por cada partida quien obtendra 3 puntos y el perdedor obtendra 1 punto y pasará a estado Inactivo, es decir,
no puede seguir jugando.

    *Las partidas se deben crear de manera aleatoria tomando dos jugadores activos con el mismo número de partidas.
    *El resultado de la partida se debe determinar de manera aleatoria.

Por ultimo el sistema debe permitir exportar a archivos los registros de los jugadores existentes con la cantidad de puntos ganados
por cada jugador para su análisis, como las partidas realizadas y poder definir asi al ganador del torneo.'''
import random
import json

#class Estado(Enum):
    #ACTIVO = 1
    #INACTIVO = 2
class Jugador:
    def __init__(self, nombre, email, puntos, raza, partidas, estado):
        self.nombre = nombre
        self.email = email
        self.puntos = puntos
        self.raza = raza
        self.partidas = partidas
        self.estado = estado

#Obtuve muchos errores intentando obtener los valores de esta forma, una disculpa.
    def obtener_nombre(self):
        return self.nombre

    #def obtener_puntos(self):
        #return self.puntos

    def obtener_partidas(self):
        return self.partidas

    #def obtener_estado(self):
        #return self.estado

    def win(self):
        self.puntos += 3
        self.partidas += 1

    def lose(self):
        self.puntos += 1
        self.estado = "Inactivo"
        self.partidas += 1

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"(nombre={self.nombre}, email={self.email}, puntos={self.puntos}, raza={self.raza}, partidas={self.partidas}, estado={self.estado})"


##########################################################################################
# ACCIONES DEL SISTEMA
##########################################################################################

def registro():
    imprimir_header("Ingresar datos del jugador:")
    nombre = input("Nombre:\n")
    email = input("Email:\n")
    puntos = 0
    raza = input("Elija una de las siguientes razas:"
                 "a)Terran b)Zerg o c)Protoss")
    if raza == "a":
        raza = "Terran"
    elif raza == "b":
        raza = "Zerg"
    elif raza == "c":
        raza = "Protoss"
    partidas = 0
    estado = "Activo"
    player = Jugador(nombre, email, puntos, raza, partidas, estado)
    JUGADORES.append(player)
    print(f"Nuevo Jugador añadido: {player}")
def is_list_empty(JUGADORES):
    if len(JUGADORES) == 0:
        return True
    return False


def ronda_uno():
    while len(JUGADORES) != 1:
        player1 = random.randint(0,len(JUGADORES) -1)
        player2 = random.randint(0,len(JUGADORES) -1)
        seleccionado = random.randint(0,2)
        while player1 == player2:
            player2 = random.randint(0,len(JUGADORES) -1)
        if JUGADORES[player1].obtener_partidas() == JUGADORES[player2].obtener_partidas():
            print(f"Partida en Curso: {JUGADORES[player1].obtener_nombre()} VS {JUGADORES[player2].obtener_nombre()}")
            if seleccionado == 0:
                print(f"El ganado fue: {JUGADORES[player1].obtener_nombre()}")
                JUGADORES[player1].win()
                JUGADORES[player2].lose()
                ELIMINADOS.append(player2)
                JUGADORES.pop(player2)
            else:
                print(f"El ganado fue: {JUGADORES[player2].obtener_nombre()}")
                JUGADORES[player2].win()
                JUGADORES[player1].lose()
                ELIMINADOS.append(player1)
                JUGADORES.pop(player1)
        else:
            ronda_uno()
def iniciar_partida():
    if is_list_empty(JUGADORES):
        print("No existe ningun jugador disponible, por favor ingrese nuevos jugadores.")
        registro()
    if len(JUGADORES) < 4:
        print("El número minimo de participantes es 4, por favor ingrese más jugadores.")
        registro()
    else:
        imprimir_header("Seleccionando participantes")
        ronda_uno()
        print(f"El Ganador definitivo fue {JUGADORES[0].nombre} Puntos Acumulados: {JUGADORES[0].puntos}")
        print(f"ELIMINADOS: {ELIMINADOS}")
        print(f"JUGADORES: {JUGADORES}")
        JUGADORES[0].estado = "Inactivo"
        ELIMINADOS.append(JUGADORES[0])
        imprimir_header("Guardando datos en archivo...")
        with open("TORNEO_FINAL", "w") as file:
            file.write("DATOS DEL TORNEO \n")
            for run in ELIMINADOS:
                file.write(f"{run.__repr__()}\n") #No entiendo por que se guarda de esa manera
        imprimir_header("Datos guardados exitosamente en el archivo:  'TORNEO_FINAL'")



def imprimir_header(header: str):
    print(f"{40 * '='} {header} {40 * '='}")


##########################################################################################
# CONTROL PRINCIPAL
##########################################################################################
JUGADORES = []
ELIMINADOS = []
MENU = {
    "Registrar": registro,
    "Iniciar Partida": iniciar_partida,
}

OPTIONS = ' | '.join(MENU.keys())

while True:
    action = input(f"Que accion deases realizar? {OPTIONS}\n")
    if action in MENU.keys():
        MENU[action]()
    else:
        print(f"Accion not soportada: {action}")
