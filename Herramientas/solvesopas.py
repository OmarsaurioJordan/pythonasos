# Solucionador de sopas de letras by Omwekiatl

# copie y pegue las palabras en el siguiente formato
palabras_txt = "\
    - BANK\
    - SCHOOL\
    - PARK\
    - HOSPITAL\
    - SUPERMARKET\
    - POSTOFFICE\
    - NEXTTO\
    - BEHIND\
    - BETWEEN\
    - IN\
    - ON\
    - UNDER\
    - THEREIS\
    - THEREARE\
    - MAP\
    - CITY\
    - CROSSWORD\
    - DIRECTIONS\
    - PLACES\
    - PREPOSITIONS"

# copie y pegue la sopa de letras en el siguiente formato
sopa_txt = "\
    W A T H E R E A R E Z F H F G\
    S O V B T C O N G B J T U F I\
    I H D C B C M Y T P E J Y C W\
    T A G I A P R P A R K H P N K\
    S F I W N P O O B D T X I J X\
    G U Q H K B L S S E S E C N O\
    N W P N S F F A T S T N B R D\
    K E O E E S U I C O W W P J K\
    J M X S R T C N T E F O E P U\
    U C A T W M H H D Z S F R E U\
    M D I P T U A E O E Z I I D N\
    G A D T C O Q R R O R E Y C C\
    U O B C Y Q M Q K E L X L H E\
    H O S P I T A L O E I S L R S\
    D I R E C T I O N S T S Y D J"

# adecuacion de las palabras como array
palabras = palabras_txt.replace(" ", "").split("-")[1:]

# crea un listado de soluciones para cada palabra
# una solucion: [row, colu, movrow, movcolu]
solucion = []
for _pal in palabras:
    solucion.append([])

# adecuacion de la sopa como matrix
sopa = []
for row in sopa_txt.split("    ")[1:]:
    sopa.append(row.split(" "))

# iterativamente ira encontrando las palabras en la sopa
for p in range(len(palabras)):
    pal = palabras[p]
    # obtiene el caracter inicial
    inicial = pal[0]
    # dos for recorren la sopa como matrix
    for row in range(len(sopa)):
        for colu in range(len(sopa[0])):
            # verifica si la celda actual es el caracter inicial
            if sopa[row][colu] == inicial:
                # dos for definen las 8 direcciones de movimiento
                for movrow in [-1, 0, 1]:
                    for movcolu in [-1, 0, 1]:
                        # pero la direccion 9: 0,0 no debe tenerse en cuenta
                        if movrow == 0 and movcolu == 0:
                            continue
                        # se recorre la palabra letra por letra, sin inicial
                        esta = True
                        for c in range(1, len(pal)):
                            # verifica si sobrepaso los limites de la sopa
                            if row + movrow * c >= len(sopa) or\
                                    row + movrow * c < 0 or\
                                    colu + movcolu * c >= len(sopa[0]) or\
                                    colu + movcolu * c < 0:
                                esta = False
                                break
                            # verifica si la letra actual no esta en la sopa
                            if sopa[row + movrow * c]\
                                    [colu + movcolu * c] != pal[c]:
                                esta = False
                                break
                        # como logro recorrerla toda, agrega la solucion
                        if esta:
                            solucion[p] = [row, colu, movrow, movcolu]
                            break
                    # evitar busqueda movrow si ya encontro
                    if len(solucion[p]) != 0:
                        break
            # evitar busqueda colu si ya encontro
            if len(solucion[p]) != 0:
                break
        # evitar busqueda row si ya encontro
        if len(solucion[p]) != 0:
            break

# crear la sopa finalizada, primero dos for pondran las celdas por defecto
result = []
for _row in range(len(sopa)):
    result.append([])
    for _colu in range(len(sopa[0])):
        result[-1].append("-")
# ahora se recorren las palabras y sus soluciones asociadas
for p in range(len(palabras)):
    pal = palabras[p]
    sol = solucion[p]
    # se verifica que se hallo solucion
    if len(sol) != 0:
        # recorrera toda la palabra caracter por caracter
        for c in range(len(pal)):
            # pondra el caracter en la solucion
            result[sol[0] + sol[2] * c]\
                [sol[1] + sol[3] * c] = pal[c]

# dibujar la sopa resultante
print("")
for row in range(len(sopa)):
    print(" ".join(result[row]))

# escribir uno por uno los resultados
print("")
for p in range(len(palabras)):
    pal = palabras[p]
    sol = solucion[p]
    # se verifica que se hallo solucion
    if len(sol) != 0:
        print(f"{sol[1]+1},{sol[0]+1}: " + pal)
    else:
        print("Nothing: " + pal)
print("")
