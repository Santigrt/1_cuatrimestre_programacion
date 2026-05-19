# Dos equipos de futbol están disputando el saque inicial del juego.
# Los capitanes de cada equipo deciden jugar el clásico juego "Piedra, papel o tijera" para definir quien hace el saque.
# Las reglas son las usuales: Piedra vence a Tijera, Tijera vence a Papel y Papel vence a Piedra.
# Juegan una sola vez.

# resolucion 1
# mostrar que la expresion larga del elif se puede guardar en una variable.
""" jugador1 = input("Jugador 1, elija Piedra, Papel o Tijera: ")
jugador2 = input("Jugador 2, elija Piedra, Papel o Tijera: ")

if jugador1 == jugador2:
    print("Empate")
elif (jugador1 == "Piedra" and jugador2 == "Tijera") or (jugador1 == "Tijera" and jugador2 == "Papel") or (jugador1 == "Papel" and jugador2 == "Piedra"):
    print("Gana el jugador 1")
else:
    print("Gana el jugador 2") """


# resolucion2 (match case con tuplas)
""" jugador1 = input("Jugador 1, elija Piedra, Papel o Tijera: ")
jugador2 = input("Jugador 2, elija Piedra, Papel o Tijera: ")

match (jugador1, jugador2):
    case (j1, j2) if jugador1 == jugador2:
        print("Empate")
    case ("Piedra", "Tijera") | ("Tijera", "Papel") | ("Papel", "Piedra"):
        print("Gana el jugador 1")
    case ("Tijera", "Piedra") | ("Papel", "Tijera") | ("Piedra", "Papel"):
        print("Gana el jugador 2")
    case _:
        print("Elección inválida") """


# resolucion3 (match case sin tuplas)
""" jugador1 = input("Jugador 1, elija Piedra, Papel o Tijera: ")
jugador2 = input("Jugador 2, elija Piedra, Papel o Tijera: ")

match jugador1:
    case "Piedra":
        match jugador2:
            case "Piedra":
                print("Empate")
            case "Tijera":
                print("Gana el jugador 1")
            case "Papel":
                print("Gana el jugador 2")
            case _:
                print("Elección inválida de Jugador 2")

    case "Tijera":
        match jugador2:
            case "Tijera":
                print("Empate")
            case "Papel":
                print("Gana el jugador 1")
            case "Piedra":
                print("Gana el jugador 2")
            case _:
                print("Elección inválida de Jugador 2")

    case "Papel":
        match jugador2:
            case "Papel":
                print("Empate")
            case "Piedra":
                print("Gana el jugador 1")
            case "Tijera":
                print("Gana el jugador 2")
            case _:
                print("Elección inválida de Jugador 2")

    case _:
        print("Elección inválida de Jugador 1") """


# resolucion4 (concatenacion)
""" jugador1 = input("Jugador 1, elija Piedra, Papel o Tijera: ")
jugador2 = input("Jugador 2, elija Piedra, Papel o Tijera: ")

combinacion = jugador1 + jugador2

if jugador1 == jugador2:
    print("Empate")
elif combinacion == "PiedraTijera" or combinacion == "TijeraPapel" or combinacion == "PapelPiedra":
    print("Jugador 1")
else:
    print("Jugador 2") """


# resolucion5 (jugar contra computadora)
""" import random

opciones = ["piedra", "papel", "tijera"]

jugador1 = input("Selecciona Piedra, Papel o Tijera: ")
computadora = random.choice(opciones)
print(computadora)

if jugador1 == computadora:
    print("Empate")
elif (jugador1 == "piedra" and computadora == "tijera") or (jugador1 == "tijera" and computadora == "papel") or (jugador1 == "papel" and computadora == "piedra"):
    print("Ganaste! 🤩")
else:
    print("Gano la Computadora! 🥲")  """



# Ahora nos solicita nuestro lider de equipo que hagamos una funcion con este codigo que realizamos
# para poder reutilizarlo mas facilmente en otro lado del codigo y en otro proyecto.

""" def jugar_piedra_papel_tijera(jugador1, jugador2):
    
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "Piedra" and jugador2 == "Tijera") or (jugador1 == "Tijera" and jugador2 == "Papel") or (jugador1 == "Papel" and jugador2 == "Piedra"):
        return "Gana el jugador 1"
    else:
        return "Gana el jugador 2"


jugador1 = input("Jugador 1, elija Piedra, Papel o Tijera: ")
jugador2 = input("Jugador 2, elija Piedra, Papel o Tijera: ")

jugar_piedra_papel_tijera(jugador1, jugador2) """

# Links: funcion debe tener uno o muchos returns
# https://youtu.be/YVLE5axjusc?feature=shared
# https://softwareengineering.stackexchange.com/questions/118703/where-did-the-notion-of-one-return-only-come-from


# Ahora nos solicitan un menu, que debe tener las siguientes caracteristicas:
# 1. Jugar --> se ejecutara la funcion para comenzar el juego
# 2. Mostrar las reglas del juego -->
# 3. Salir --> terminara el programa

def jugar_piedra_papel_tijera(jugador1, jugador2):
    
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "Piedra" and jugador2 == "Tijera") or (jugador1 == "Tijera" and jugador2 == "Papel") or (jugador1 == "Papel" and jugador2 == "Piedra"):
        return "Gana el jugador 1"
    else:
        return "Gana el jugador 2"

seleccion = ""
while seleccion != "3":

    print("1. Comenzar juego ")
    print("2. Mostrar reglas del juego ")
    print("3. Salir del juego")
    seleccion = input("Selecciona una opcion: ")
    
    if seleccion == "1":
        jugador1 = input("Jugador 1, elija Piedra, Papel o Tijera: ")
        jugador2 = input("Jugador 2, elija Piedra, Papel o Tijera: ")
        resultado = jugar_piedra_papel_tijera(jugador1, jugador2)
        print(resultado)
    elif seleccion == "2":
        print("\nPiedra aplasta tijera. 🪨  ✂️\n"
              "Tijera corta papel. ✂️  🧻\n"
              "Papel envuelve piedra. 🧻 🪨\n"
              "Empate: Si ambos jugadores muestran la misma figura, se vuelve a jugar.\n")
    elif seleccion == "3":
        print("Gracias por jugar! 💞") # ¿Si no quieremos poner nada? --> Podriamos poner un pass
    else:
        print("Opcion incorrecta. ⛔")
