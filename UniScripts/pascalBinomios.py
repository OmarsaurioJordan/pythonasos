def fact(n):
    # halla el valor factorial !n
    # Python tiene funciones para esto, pero aqui se muestra como se hace
    tot = 1
    for i in range(1, n + 1):
        tot *= i
    return tot

def coef(n, k):
    # implementa la ecuacion para hallar coeficientes
    return int(fact(n) / (fact(k) * fact(n - k)))

def txt_ecu(n):
    # retornara un string con el binomio expandido, lo inicia en vacio
    txt = ""
    # k sera la columna del triangulo, cada posicion de la sumatoria
    for k in range(n + 1):
        # cada termino, como es una sumatoria debe iniciar con un " + "
        txt += " + "
        # obtiene el valor del coeficiente
        c = coef(n, k)
        # el coeficiente solo se mostrara si es mayor a 1
        if c > 1:
            txt += str(c) + " "
        # A solo debe mostrarse si no es A^0, su exponente debe ser mayor a 0
        if n - k > 0:
            txt += "A"
            # el exponente de A solo se mostrara si es mayor a 1
            if n - k > 1:
                txt += "^" + str(n - k)
            # al final agrega un espacio para no quedar pegado de B
            txt += " "
        # B solo debe mostrarse si no es B^0, su exponente debe ser mayor a 0
        if k > 0:
            txt += "B"
            # el exponente de B solo se mostrara si es mayor a 1
            if k > 1:
                txt += "^" + str(k)
        else:
            # este slicing quita el espacio agregado para separar A de B
            txt = txt[0:-1]
    # como cada ciclo agrega un " + ", este slicing quita el primero
    txt = txt[3:]
    # cuando N=0 pondra el resultado a 1 dado que (A+B)^0=1
    if txt == "":
        txt = "1"
    # agrega a la izquierda el binomio no expandido
    txt = "(A + B)^" + str(n) + " = " + txt
    return txt

def str_fix(txt, tot):
    # dada una string y una talla deseada, le pone espacios
    # hasta alcanzar dicha talla, ej: ("A", 3) -> " A "
    res = txt
    rigth = True
    # el ciclo se repite hasta alcanzar la talla
    while len(res) < tot:
        # los espacios se agregan a derecha o izquierda
        if rigth:
            res = res + " "
        else:
            res = " " + res
        # la variable booleana hace que se intercalen izq y der
        rigth = not rigth
    return res

def draw_pascal(n):
    # ancho guardara la talla que debe ocupar cada dato string, cada celda
    ancho = 1
    for k in range(n + 1):
        # por eso averigua la talla de cada coeficiente, guardando la mayor
        ancho = max(ancho, len(str(coef(n, k))))
    # vacio es un string lleno de espacios, respetando el ancho de la celda
    vacio = str_fix(" ", ancho)
    # este ciclo se repite para pintar las N filas, es la altura del triangulo
    for row in range(n + 1):
        # cada fila inicia su representacion string en vacio
        txt = ""
        # este for llena de celdas vacias el lado izquierdo del triangulo
        for rep in range(n - row):
            txt += vacio
        # este for agrega como tal los coeficientes, limitado a row, la fila actual
        for k in range(row + 1):
            # obtiene el coeficiente y asegura que sea del ancho de la celda
            c = coef(row, k)
            txt += str_fix(str(c), ancho)
            # si el coeficiente no es el ultimo, agrega una celda vacia a su derecha
            if k != row:
                txt += vacio
        # este for llena de celdas vacias el lado derecho del triangulo
        for rep in range(n - row):
            txt += vacio
        # finalmente pinta la fila
        print(txt)

def main():
    # esta es la funcion principal del software, primero imprime el titulo
    print("** Binomio de Newton y Triángulo de Pascal **")
    print("** Omar Jordan Jordan - ADSO24 **")
    # y entra en el main loop, para poder repetir la ejecucion multiples veces
    ciclo = True
    while ciclo:
        print("...")
        # intentara leer un numero entero dado por el usuario
        try:
            num = abs(int(input("digite el grado del binomio: ")))
        except:
            ciclo = False
        # si hay un fallo leyendo el dato, aborta el programa rompiendo el loop
        if not ciclo:
            break
        # si todo va bien, llamara a la funcion que genera el binomio expandido
        print(txt_ecu(num))
        print("...")
        # finalmente para este ciclo, preguntara si quiere dibujar el triangulo
        sel = input("desea dibujar el triangulo (s/n): ").lower()
        if sel == "s":
            draw_pascal(num)

main()
