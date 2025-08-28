import random

# modelo de informacion para el juego
lado = 10 # talla del tablero, area = lado * lado
pos = [0, 0] # posicion en la que esta el player: x, y

# funcion principal que contiene el main loop
def main():
    # inicializa el sistema de numeros aleatorios
    random.seed()
    # muestra el encabezado del software, con titulo e instrucciones
    print("...")
    print("*** Titulo del programa y etc ***")
    print("...")
    # esto pone las variables del modelo de informacion en valores iniciales
    inicializa()
    # se dibuja el talero por primer vez
    drawAll()
    # y se continuan dando instrucciones, en este caso los comandos
    print("digite w,s,a,d para moverse:")
    # aca comienza el main loop del software, hasta que gane o pierda
    while True:
        # primero el usuario movera al personaje protagonista
        plyMove()
        # se dibujara todo el tablero de nuevo, actualizado
        drawAll()

def inicializa():
    # pone al player en un lugar aleatorio del tablero
    global pos, lado
    pos = [
        random.randint(0, lado - 1),
        random.randint(0, lado - 1)
    ]

def plyMove():
    # espera por el comando del jugador (usuario) y hace un movimento
    global pos, lado
    sel = input("->").lower()
    # dado un input en mnusculas, que debe ser w,s,a,d depura la eleccion
    if sel == "a":
        # por ejemplo, para "a" tratara de actualizar la posicion del player
        # en la direccion hacia la izquierda, cuidando no pasar el limite
        pos[0] = max(0, pos[0] - 1)
    elif sel == "d":
        pos[0] = min(lado - 1, pos[0] + 1)
    elif sel == "w":
        pos[1] = max(0, pos[1] - 1)
    elif sel == "s":
        pos[1] = min(lado - 1, pos[1] + 1)

def drawAll():
    # este codigo dibuja todo el tablro en pantalla
    global pos, lado
    # el primer ciclo recorre todas las filas (verticalmente)
    for y in range(lado):
        # la variable txt acumula los caracteres que se pintaran en una fila
        txt = ""
        # el segundo ciclo recorre todas las columnas (horizontalmente)
        for x in range(lado):
            # si el punto actual es el player, se dibujara
            if pos[0] == x and pos[1] == y:
                txt += " x " # player
            # sino, se dibuja un espacio vacio
            else:
                txt += " . " # vacio
        # dibujar toda la fila
        print(txt)

# lanzamiento del programa
main()
