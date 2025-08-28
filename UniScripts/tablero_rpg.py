# Omar Jordan Jordan - ADSO24 - 2024 - Calabozin v5

import random
import math

# modelo de informacion para el juego

lado = 10 # talla del tablero, area = lado * lado
pos = [0, 0] # posicion en la que esta el player
enemy = [] # listado de posiciones 2D (x,y) de enemigos
muro = [] # listado de posiciones 2D (x,y) de muros
punto = [] # listado de posiciones 2D (x,y) de puntos
puerta = [0, 0] # posicion en la que esta la puerta
salida = False # se pondra a verdadero cuando tome todos los puntos, podra irse

# funcion principal que contiene el main loop

def main():
    # inicializa el sistema de numeros aleatorios
    random.seed()
    # muestra el encabezado del software, con titulo e instrucciones
    print("...")
    print("*** Omwekiatl - Calabozin - 2024 ***")
    print("...")
    print("x:tú, □:muro, o:enemigo, *:punto, []:puerta")
    print("x debe tomar todos los * y salir por [] evadiendo a o")
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
        # luego los eneigos se moveran por el talero
        enemysIA()
        # se dibujara todo el tablero de nuevo, actualizado
        drawAll()
        # finalmente se comprobara si un enemigo capturo al player
        if isMuerto():
            print("...")
            print("(capturado)")
            print("...")
            break
        # o sino, se compruea si el player tomo un punto o salio por la puerta
        elif takePoint():
            print("...")
            print("(exito)")
            print("...")
            break
    # esto evita un cierre instantaneo del software, espera comando del usuario
    input("")

# funciones que ponen las partes del juego en su lugar inicial

def inicializa():
    # pone al player en un lugar aleatorio del tablero
    global pos
    pos = rand2()
    # crea una cantidad de enemigos proporcional al area del tablero
    area = pow(lado, 2)
    iniEnemys(math.floor(area * 0.05))
    # crea una catidad de muros, primero halla dos cantidades min y max
    # utilizando el area del tablero y un par de densidades, luego
    # elige una catidad al azar entre estas dos cantidades
    iniMuros(random.randint(
        math.floor(area * 0.1),
        math.floor(area * 0.2)
    ))
    # crea una cantidad de puntos proporcional al area del tablero
    iniPuntos(math.floor(area * 0.05))
    # pone la puerta en algun lugar del tablero al azar, solo por los bordes
    iniPuerta()

def iniEnemys(cuantos):
    # crea enemigos agregando al array duplas 2D (x,y) con posiciones aleatorias
    global enemy
    for e in range(cuantos):
        # obtiene una posicon aleatoria
        xy = rand2()
        # mientras el espacio esta ocupado por un ete movil, intentara una nueva posicion
        while isAny(xy):
            xy = rand2()
        # agrega la posicion como tal al array
        enemy.append(xy)

def iniMuros(cuantos):
    # crea muros en lugares al azar, solo donde no haya entes moviles
    global muro
    for m in range(cuantos):
        xy = rand2()
        while isAny(xy):
            xy = rand2()
        muro.append(xy)

def iniPuntos(cuantos):
    # crea puntos al azar, los agrega al array, se asegura que lo espacios esten libres
    global punto
    for p in range(cuantos):
        xy = rand2()
        while not isFree(xy):
            xy = rand2()
        punto.append(xy)

def iniPuerta():
    # crea una puerta en un lugr al azar, en los bordes del tablero
    while True:
        # aleatoriamente se elige si crearla en los bordes horizontales o verticales
        if random.random() < 0.5:
            # elegir borde izquierdo o derecho
            puerta[0] = random.choice([0, lado - 1])
            # elegir altura a la que esta la puerta
            puerta[1] = random.randint(0, lado - 1)
        else:
            # elegir borde supeior o inferior
            puerta[1] = random.choice([0, lado - 1])
            # elegir posicion horizontal a la que esta la puerta
            puerta[0] = random.randint(0, lado - 1)
        # solo cuando no colisiona la puerta con un muro, el ciclo termina
        if not isMuro(puerta):
            break

# funciones principales del main loop, administran las partes del juego

def plyMove():
    # espera por el comando del jugador (usuario) y hace un movimento
    global pos
    sel = input("->").lower()
    # dado un input en mnusculas, que debe ser w,s,a,d depura la eleccion
    if sel == "a":
        # por ejemplo, para "a" tratara de actualizar la posicion del player
        # en la direccion hacia la izquierda
        pos = paso(pos, [-1, 0])
    elif sel == "d":
        pos = paso(pos, [1, 0])
    elif sel == "w":
        pos = paso(pos, [0, -1])
    elif sel == "s":
        pos = paso(pos, [0, 1])

def enemysIA():
    # esta funcion recorre todos los enemigos y dice a donde se ueve cada uno
    global enemy
    for e in range(len(enemy)):
        # verifica que el player este al alcance de la vista, obtiene la direccion
        # normalizada de ser asi, sino una dupla x,y nula 0,0
        xy = vePlayer(enemy[e])
        if xy[0] != 0 or xy[1] != 0:
            # cuando la dupla no es nula, este enemigo se movera hacia el player
            # segun la direccion dada por la busqueda
            ant = enemy[e]
            enemy[e] = [ant[0] + xy[0], ant[1] + xy[1]]
            continue
        # de lo contrario, hara una probabilidad de que el enemigo no se mueva
        if random.random() < 0.5:
            continue
        # pero si si se mueve, lo hara al azar, eligiendo una direccion random
        # xy aun no mueve al enemigo, sino que es una posicion nueva obtenida
        xy = paso(enemy[e], dirRand())
        # mientras haya un enemigo (otro) en la nueva posicion, no podra moverse ahi
        # entonces re-intentara hasta lograrlo o hasta que un freno f aborte la busqueda
        f = 8
        while isEnemy(xy):
            # el freno trata de abortar la busqueda para prevenir un ciclo infinito
            f -= 1
            if f <= 0:
                break
            # obtiene una nueva posicion de movimiento al azar
            xy = paso(enemy[e], dirRand())
        # en caso de que el ciclo termine sin haber sido abortado, efectuara el cambio
        if f > 0:
            enemy[e] = xy

def drawAll():
    # este codigo dibuja todo el tablro en pantalla
    global pos, lado
    # el primer ciclo recorre todas las filas (verticalmente)
    for y in range(lado):
        # la variable txt acumula los caracteres que se pintaran en una fila
        txt = ""
        # el segundo ciclo recorre todas las columnas (horizontalmente)
        for x in range(lado):
            # en caso de haber un muro, se agregara su simbolo
            if isMuro([x, y]):
                txt += " □ " # muro
            # sino, si hay un enemigo, se dibujara segun su estado
            elif isEnemy([x, y]):
                if pos[0] == x and pos[1] == y:
                    txt += "(x)" # atrapando al player
                elif puerta[0] == x and puerta[1] == y:
                    txt += "[o]" # enemy + puerta
                else:
                    txt += " o " # enemy
            # sino, si el punto actual es el player, se dibujara segun su estado
            elif pos[0] == x and pos[1] == y:
                if puerta[0] == x and puerta[1] == y:
                    txt += "[x]" # player + puerta
                else:
                    txt += " x " # player
            # sino, si hay un punto, se dibujara segun su estado
            elif isPunto([x, y]):
                if puerta[0] == x and puerta[1] == y:
                    txt += "[*]" # punto + puerta
                else:
                    txt += " * " # punto
            # sino, si esta la puerta, se dibuja
            elif puerta[0] == x and puerta[1] == y:
                txt += "[.]" # puerta
            # sino, se dibuja un espacio vacio
            else:
                txt += " . " # vacio
        print(txt)

# funciones para obtener informacion o modificar el modelo de informacion

def takePoint():
    # retorna verddero si el player ha ganado el juego, esta funcion se encarga de
    # hacer la recoleccion de puntos y verificar la condicion de victoria
    global punto, pos, salida
    # para cada punto, verifica si esta en la posicon del player
    for p in range(len(punto)):
        if pos[0] == punto[p][0] and pos[1] == punto[p][1]:
            # de ser asi, elimina al punto de la lista (array)
            punto.pop(p)
            # si la lista esta vacia, entonces activara la puerta
            if len(punto) == 0:
                salida = True
            break
    # verifica i puede irse por la puerta, solo podra si recogio todos los puntos
    return isDoor(pos)

def isEnemy(xy):
    # dada una posicion, retorna verdadero si en ella hay un enemigo
    global enemy
    for e in enemy:
        if xy[0] == e[0] and xy[1] == e[1]:
            return True
    return False

def isMuro(xy):
    # dada una posicion, retorna verdadero si en ella hay un muro
    global muro
    for m in muro:
        if xy[0] == m[0] and xy[1] == m[1]:
            return True
    return False

def isPunto(xy):
    # dada una posicion, retorna verdadero si en ella hay un punto
    global punto
    for p in punto:
        if xy[0] == p[0] and xy[1] == p[1]:
            return True
    return False

def isAny(xy):
    # dada una posicion, retorna verdadero si en ella esta el player o
    # hay algun enemigo, mejor dicho, hay algun ente movil
    global pos
    if xy[0] == pos[0] and xy[1] == pos[1]:
        return True
    return isEnemy(xy)

def isFree(xy):
    # dada una posicion, retorna verdadero si en ella hay algun ente movil
    # como el player o un enemigo, y tambien si hay algun muro
    if isAny(xy):
        return False
    return not isMuro(xy)

def isMuerto():
    # retorna verdadero si la posicion del player coincide con algun enemigo
    global pos
    return isEnemy(pos)

def isDoor(xy):
    # solo cuando la puerta esta activa (segun la variable salida), devolvera
    # verdadero si esta coincide con el punto dado
    global salida, puerta
    if salida:
        return puerta[0] == xy[0] and puerta[1] == xy[1]
    return False

# funciones mas avanzadas para el manejo de la IA

def paso(posAnt, dirMov):
    # retorna la nueva posicion, moviendo la dada en la direccion dada
    global lado
    # esta nueva posicion esta limitada a la talla del tablero
    xy = [
        clamp(posAnt[0] + dirMov[0], 0, lado - 1),
        clamp(posAnt[1] + dirMov[1], 0, lado - 1)
    ]
    # verifica si la nueva posicion colisiona con un muro, entonces devuelve la original
    if isMuro(xy):
        return posAnt
    return xy

def vePlayer(xy):
    # retorna la direccion normalizada en la cual ha visto al player desde xy
    # este array tiene las posibles direcciones no normalizadas de busqueda
    dirs = [
        [-2, 0], # izquierda
        [2, 0], # derecha
        [0, 2], # abajo
        [0, -2] # arriba
    ]
    # el ciclo testea para cada direccion si ve al player usando raycast
    for d in dirs:
        if raycast(xy, d):
            # de verlo, retorna la direccion de busqueda, normalizandola antes
            return [d[0] / max(1, abs(d[0])),
                    d[1] / max(1, abs(d[1]))]
    # de no encontrarlo retorna una direccion vacia, vector nulo
    return [0, 0]

def raycast(xy, dir):
    # retorna verdadero si desde el punto xy dado, en la direccio no normalizada dir, hay
    # colision con el player, devolvera falso si hay obstaculos en el medio
    global lado, pos
    # se copia el array para no modificarlo por si se pasa como referencia
    ray = xy.copy()
    # se repetira este ciclo hasta que xy avance el valor dado por dir, avazando de 1 en 1
    while dir[0] != 0 or dir[1] != 0:
        # hara el avance de xy en la direccion dir, pero de a un solo paso
        ray[0] += dir[0] / max(1, abs(dir[0]))
        ray[1] += dir[1] / max(1, abs(dir[1]))
        # disminuira dir en 1 en cualquiera que sea su direccion
        if dir[0] > 0:
            dir[0] -= 1
        elif dir[0] < 0:
            dir[0] += 1
        if dir[1] > 0:
            dir[1] -= 1
        elif dir[1] < 0:
            dir[1] += 1
        # verificara si el nuevo punto esta fuera del tablero
        if ray[0] < 0 or ray[0] > lado - 1:
            return False
        if ray[1] < 0 or ray[1] > lado - 1:
            return False
        # verifica si el nuevo punto choca con un muro
        if isMuro(ray):
            return False
        # verifica si el nuevo punto choca con un enemigo
        if isEnemy(ray):
            return False
        # finalmente verifica si el nuevo punto coincide con el player
        if ray[0] == pos[0] and ray[1] == pos[1]:
            return True
    # al llegar al final siempre retorna falso, no encontro nada
    return False

# funciones que son herramientas, independientes del modelo de informacion

def rand2():
    # retorna una posicion aleatoria x,y limitada a la talla del tablero
    global lado
    return [
        random.randint(0, lado - 1),
        random.randint(0, lado - 1)
    ]

def clamp(val, vmin, vmax):
    # retorna el valor dado, limitado a un max y min
    return min(vmax, max(val, vmin))

def dirRand():
    # retorna una direccion 2D aleatoria y unitaria, limitada a 4 lados en cruz
    p = random.randint(0, 3)
    if p == 0:
        return [1, 0] # derecha
    elif p == 1:
        return [0, -1] # arriba
    elif p == 2:
        return [-1, 0] # izquierda
    return [0, 1] # abajo

# lanzamiento del programa

main()

"""
TAREAS:
- hacer test al algoritmo de los enemigos para
  verificar si persiguen al player como debe ser
- garantizar que desde la posicion inicial se pueda
  alcanzar todo punto y la puerta de salida, tambien
  que los enemigos desde su posicion inicial puedan
  alcanzar al jugador en su posicion inicial
"""
