# Taller 1 de Algoritmia, SENA 2024
# Omar Jordan Jordan, ADSO24, 2999567

import math

funciones = [
        "potenciación de números M^N",
        "suma y promedio de N valores",
        "áreas y perímetros de figuras 2D",
        "tasa de cambio COP y USD",
        "pulsaciónes durante ejercicio",
        "calcular (in/de)cremento salarial",
        "reparto de dinero a hospital",
        "sueldo de empleado según horas",
        "calcular precio para artículos",
        "registro de elefantes",
        "solucionador de polinomios",
        "conversor de horas a min, seg, días",
        "atleta que corre 3 veces a la semana",
        "porcentajes de dinero de inversionistas",
        "evaluación de estudiante por materias",
        "registro de estudiantes",
        "conversor de °C °K °F",
        "calculadora de índice de masa corporal"
    ]

# tendra listas de la forma [nombre, edad, genero, nota]
estudiantes = []

# tendra listas de la forma [nombre, peso, longitud]
elefantes = []

# guardara los tiempos del atleta
corredor = []

# porcentajes de reparto presupuestal hospital
hospital = [
        ["ginecología", 0.4],
        ["traumatología", 0.3],
        ["pediatría", 0.3]
    ]

# tabla de indice de masa corporal
indMasCorp = [
    [15.0, "delgadez muy severa"],
    [15.9, "delgadez severa"],
    [18.4, "delgadez"],
    [24.9, "peso saludable"],
    [29.9, "sobrepeso"],
    [34.9, "obesidad moderada"],
    [39.9, "obesidad severa"],
    [10000.0, "obesidad muy severa"]
]

# modelo de informacion de las notas: [materia, porcent_examen, total_tareas]
notasClase = [
    ["matemáticas", 0.9, 3],
    ["física", 0.8, 2],
    ["química", 0.85, 3]
]

# main loop del software, con seleccion de funciones

def main():
    
    print("******Taller 1 de Algoritmia, SENA 2024******")
    print("(Omar Jordan Jordan, ADSO24, 2999567)")
    
    while True:
        
        print("...")
        print("digite el índice de un problema del taller,")
        print("la palabra 'menu' para ver el listado o")
        print("la palabra 'salir' para cerrar el software")
        
        sel = input("-> ").lower()
        
        if sel == "menu":
            for i in range(len(funciones)):
                print("   " + str(i + 1) + ". " + funciones[i])
            continue
        
        elif sel == "salir":
            print("   fin del programa")
            return 0
        
        elif sel == "1":
            potenciacion()
        elif sel == "2":
            sumaYpromedio()
        elif sel == "3":
            areasYperimetros()
        elif sel == "4":
            tasaDeCambio()
        elif sel == "5":
            pulsaciones()
        elif sel == "6":
            incrementoSalarial()
        elif sel == "7":
            dineroHospital()
        elif sel == "8":
            sueldoHoras()
        elif sel == "9":
            precioArticulos()
        elif sel == "10":
            regiElefantes()
        elif sel == "11":
            polinomios()
        elif sel == "12":
            conversorHoras()
        elif sel == "13":
            atletaCorredor()
        elif sel == "14":
            dineroInversionistas()
        elif sel == "15":
            evaluacionMaterias()
        elif sel == "16":
            registroEstudiantes()
        elif sel == "17":
            ConversorTemp()
        elif sel == "18":
            indiceMasaCorporal()
        
        else:
            print("   comando no válido")
            continue
        
        input("(presione enter)")

# funciones para cada seleccion del usuario

def potenciacion():
    print("   " + funciones[0])
    num_M = getFloat("digite la base M")
    num_N = getFloat("digite el exponente N")
    try:
        result = strRound(num_M ** num_N)
    except:
        result = "???"
    print("   " + strRound(num_M) + " ^ " + strRound(num_N) + " = " + result)

def sumaYpromedio():
    print("   " + funciones[1])
    suma = 0.0
    datos = 0
    while True:
        datos += 1
        suma += getFloat("digite el dato " + str(datos))
        if input("-> desea calcular el promedio (s/n): ").lower() == "s":
            break
    print("   se tienen " + str(datos) + " datos")
    print("   la suma total es: " + strRound(suma))
    print("   el promedio es: " + strRound(suma / datos))

def areasYperimetros():
    print("   " + funciones[2])
    print("   1. Círculo")
    print("   2. Rectángulo")
    print("   3. Triángulo rectangulo")
    print("   4. Trapecio Isósceles")
    print("   5. Hexágono")
    sel = input("-> ")
    if sel == "1": # circulo
        radio = getFloat("digite el radio")
        print("   área: " + strRound(math.pi * (radio ** 2.0)))
        print("   perimetro: " + strRound(2.0 * math.pi * radio))
    elif sel == "2": # rectangulo
        ancho = getFloat("digite el ancho")
        alto = getFloat("digite el alto")
        print("   área: " + strRound(ancho * alto))
        print("   perimetro: " + strRound(2.0 * (ancho + alto)))
    elif sel == "3": # triangulo rectangulo
        base = getFloat("digite la base")
        altura = getFloat("digite la altura")
        print("   área: " + strRound((base * altura) / 2.0))
        print("   perimetro: " + strRound(base + altura +
            math.sqrt((base ** 2.0) + (altura ** 2.0))))
    elif sel == "4": # trapecio isoceles
        base_I = getFloat("digite la base inferior")
        base_S = getFloat("digite la base superior")
        altura = getFloat("digite la altura")
        basesita = (base_I - base_S) / 2.0
        lado = math.sqrt((basesita ** 2.0) + (altura ** 2.0))
        print("   área: " + strRound(((base_I + base_S) / 2.0) * altura))
        print("   perimetro: " + strRound(base_I + base_S + 2.0 * lado))
    elif sel == "5": # hexagono
        lado = getFloat("digite el lado")
        relation = 1.5 * math.sqrt(3.0)
        print("   área: " + strRound(relation * (lado ** 2)))
        print("   perimetro: " + strRound(6.0 * lado))
    else:
        print("   selección incorrecta")

def tasaDeCambio():
    print("   " + funciones[3])
    tasaCambio = abs(getFloat("digite la tasa de cambio (1USD=?COP)"))
    if tasaCambio == 0:
        print("   la tasa es nula")
        return None
    while True:
        print("   digite: 1.COP_USD, 2.USD_COP, 3.salir")
        sel = input("-> ")
        if sel == "1":
            cop = getFloat("digite los pesos")
            print("   dólares: $" + strRound(cop / tasaCambio))
        elif sel == "2":
            usd = getFloat("digite los dólares")
            print("   pesos: $" + strRound(usd * tasaCambio))
        elif sel == "3":
            print("   fin modo tasa de cambio")
            break
        else:
            print("   comando inválido")

def pulsaciones():
    print("   " + funciones[4])
    edad = getInt("digite su edad")
    esperado = (220.0 - edad) / 10.0
    if edad > 200:
        print("   no puede vivir más de 200 años")
    else:
        print("   las pulsaciónes esperadas en 10 segundos son: " + strRound(esperado, 1))
        if input("-> desea ingresar sus pulsaciónes (s/n): ").lower() == "s":
            print("   haga ejercicio intenso... luego")
            pulso = getInt("digite los pulsos tomados en 10 segundos")
            print("   usted está en un " + strRound((pulso / esperado) * 100.0, 1) + "% del valor esperado")

def incrementoSalarial():
    print("   " + funciones[5])
    salario = getFloat("digite el salario anterior")
    incremento = getFloat("digite el porcentaje de incremento (ej: 25)")
    print("   el nuevo salario es: $" + strRound(salario * (1.0 + incremento / 100.0)))

def dineroHospital():
    global hospital
    print("   " + funciones[6])
    while True:
        print("   digite: 1.ingreso, 2.modificar, 3.información, 4.salir")
        sel = input("-> ")
        if sel == "1":
            ingreso = getFloat("digite ingreso presupuestal")
            for i in range(len(hospital)):
                print("   " + hospital[i][0] + " recibe: $" +
                      strRound(ingreso * hospital[i][1], 0))
        elif sel == "2":
            porcent = getPorcent("digite el porcentaje para " + hospital[0][0] +
                " (" + strRound(hospital[0][1] * 100.0, 0) + "%)")
            hospital[0][1] = min(1.0, porcent)
            porcent = getPorcent("digite el porcentaje para " + hospital[1][0] +
                " (" + strRound(hospital[1][1] * 100.0, 0) + "%)")
            hospital[1][1] = min(1.0 - hospital[0][1], porcent)
            hospital[2][1] = 1.0 - (hospital[0][1] + hospital[1][1])
            print("   el porcentaje de " + hospital[2][0] + " será: " +
                strRound(hospital[2][1] * 100.0, 0) + "%")
        elif sel == "3":
            for i in range(len(hospital)):
                print("   " + hospital[i][0] + " con " +
                    strRound(hospital[i][1] * 100.0, 0) + "%")
        elif sel == "4":
            print("   fin modo hospital")
            break
        else:
            print("   comando inválido")

def sueldoHoras():
    print("   " + funciones[7])
    horas = getInt("digite las horas trabajadas al mes")
    valor = getFloat("digite el valor de la hora")
    print("   el pago será: $" + strRound(horas * valor))

def precioArticulos():
    print("   " + funciones[8])
    prima = getFloat("digite el precio original del artículo")
    gain = getFloat("digite el porcentaje de ganancia deseada (ej: 30)")
    print("   el precio de venta será: $" + strRound(prima * (1.0 + gain / 100.0)))

def regiElefantes():
    global elefantes
    # la lista elefantes tiene listas asi [nombre, peso, longitud]
    print("   " + funciones[9])
    print("   1. ingresar elefante")
    print("   2. información elefantes")
    print("   3. regresión lineal")
    print("   4. eliminar elefante")
    print("   5. eliminar a todos")
    print("   6. salir al menú")
    while True:
        print("   ...")
        sel = input("-> ")
        if sel == "1":
            ele = input("-> escriba el nombre del elefante: ")
            if ele != "":
                peso = getFloat("digite el peso en libras") * 0.453592
                long = getFloat("digite la longitud en pies") * 0.3048
                ok = False
                for e in range(len(elefantes)):
                    if elefantes[e][0] == ele:
                        elefantes[e][1] = peso
                        elefantes[e][2] = long
                        print("      actualizado exitosamente")
                        ok = True
                        break
                if not ok:
                    elefantes.append([ele, peso, long])
                    print("      agregado exitosamente")
        elif sel == "2":
            if len(elefantes) == 0:
                print("      no hay elefantes")
            else:
                n = 1
                for ele in elefantes:
                    txt = "(" + str(n) + ") " + ele[0]
                    txt += ": " + strRound(ele[1], 1) + " Kg - "
                    txt += strRound(ele[2], 1) + " m"
                    print("      " + txt)
                    n += 1
        elif sel == "3":
            total = len(elefantes)
            print("      hay " + str(total) + " elefantes")
            if total > 0:
                # regresion lineal
                # m = (n*sum(xi*yi)-sum(xi)*sum(yi)) / (n*sum(xi^2)-sum(xi)^2)
                # b = mean(y)-m*mean(x)
                sumXY = 0.0
                sumX = 0.0
                sumY = 0.0
                sumX2 = 0.0
                for ele in elefantes:
                    sumXY += ele[1] * ele[2]
                    sumX += ele[1] # peso
                    sumY += ele[2] # longitud
                    sumX2 += pow(ele[1], 2.0)
                m = ((total * sumXY - sumX * sumY) /
                    (total * sumX2 - pow(sumX, 2.0)))
                b = (sumY / total) - m * (sumX / total)
                if b > 0:
                    print("   longitud = " + strRound(m) + " * peso + " +
                        strRound(b))
                elif b < 0:
                    print("   longitud(peso) = " + strRound(m) + " * peso - " +
                        strRound(abs(b)))
                else:
                    print("   longitud(peso) = " + strRound(m) + " * peso")
        elif sel == "4":
            ele = input("-> escriba el nombre a eliminar: ")
            if ele != "":
                ok = False
                for e in range(len(elefantes)):
                    if elefantes[e][0] == ele:
                        elefantes.pop(e)
                        print("      borrado exitosamente")
                        ok = True
                        break
                if not ok:
                    print("      no se encontró el nombre")
        elif sel == "5":
            elefantes = []
            print("      registro limpio")
        elif sel == "6":
            print("      saliendo del registro")
            break
        else:
            print("      comando no válido")

def polinomios():
    print("   " + funciones[10])
    grado = abs(getInt("digite el grado del polinomio"))
    coef = []
    for i in range(grado + 1):
        coef.append(getFloat("digite el coeficiente X^" + str(i)))
    txt = ""
    for i in range(len(coef)):
        # solo si exite el coeficiente entonces se dibujara
        if coef[i] != 0:
            # encontrar forma string de X
            x = ""
            if i == 1:
                x = "X"
            elif i > 1:
                x = "X^" + str(i)
            # concatenar coeficientes
            if i == len(coef) - 1:
                if coef[i] == -1:
                    txt = "-" + x + txt
                elif coef[i] == 1:
                    txt = x + txt
                else:
                    txt = strRound(coef[i]) + x + txt
            elif coef[i] < 0:
                if coef[i] == -1:
                    txt = " - " + x + txt
                else:
                    txt = " - " + strRound(abs(coef[i])) + x + txt
            else:
                if coef[i] == 1:
                    txt = " + " + x + txt
                else:
                    txt = " + " + strRound(coef[i]) + x + txt
    print("   Y = " + txt)
    # hacer ciclos de ingreso de datos para obtener Y(X)
    while True:
        val_X = getFloat("digite un valor para X")
        val_Y = 0.0
        for i in range(len(coef)):
            val_Y += coef[i] * (val_X ** i)
        print("   Y(" + strRound(val_X) + ") = " + strRound(val_Y))
        if input("-> desea ingresar otro valor (s/n): ").lower() == "n":
            break

def conversorHoras():
    print("   " + funciones[11])
    horas = getInt("digite la cantidad de horas")
    print("   segundos: " + strRound(horas * 60 * 60))
    print("   minutos: " + strRound(horas * 60))
    print("   días: " + strRound(horas / 24))
    print("   semanas: " + strRound((horas / 24) / 7))
    print("   años: " + strRound((horas / 24) / 365.25))

def atletaCorredor():
    global corredor
    print("   " + funciones[12])
    while True:
        print("   digite: 1.ingresar marca, 2.ver promedio, 3.limpiar, 4.salir")
        sel = input("-> ")
        if sel == "1":
            corredor.append(getFloat("digite la marca de tiempo #" + str(len(corredor) + 1)))
        elif sel == "2":
            total = min(6, len(corredor))
            if total == 0:
                print("   no hay datos")
            else:
                promedio = 0.0
                for i in range(len(corredor) -1, len(corredor) - total - 1, -1):
                    promedio += corredor[i]
                promedio /= total
                print("   el promedio de 2 semanas es: " + strRound(promedio, 1))
                print("   el historial tiene " + str(len(corredor)) + " datos")
        elif sel == "3":
            corredor = []
            print("   registro limpio")
        elif sel == "4":
            print("   fin modo corredor")
            break
        else:
            print("   comando inválido")

def dineroInversionistas():
    print("   " + funciones[13])
    nombre = []
    monto = []
    total = 0.0
    indice = 0
    while True:
        indice += 1
        nombre.append(input("-> escriba el nombre del inversionista " + str(indice) + ": "))
        monto.append(getFloat("digite el monto de su inversión"))
        total += monto[-1]
        if input("-> desea analizar las inversiónes (s/n): ").lower() == "s":
            break
    if total == 0:
        print("   no han invertido dinero")
    else:
        print("   se ha invertido un total de: $" + strRound(total))
        for i in range(len(nombre)):
            print("   (" + str(i + 1) + ") " + nombre[i] + ": " + strRound((monto[i] / total) * 100.0, 1) + "%")

def evaluacionMaterias():
    global notasClase
    print("   " + funciones[14])
    # notasClase: [materia, porcent_examen, total_tareas]
    notas = []
    for m in range(len(notasClase)):
        print("    para " + notasClase[m][0])
        nta = min(5.0, abs(getFloat("digite la nota del exámen (0 a 5)")))
        notas.append(nta * notasClase[m][1])
        promTareas = 0.0
        for t in range(notasClase[m][2]):
            nta = min(5.0, abs(getFloat("digite la nota de la tarea " +
                str(t + 1) + " (0 a 5)")))
            promTareas += nta
        promTareas /= max(1, notasClase[m][2])
        notas[-1] += promTareas * (1.0 - notasClase[m][1])
    promTareas = 0.0
    for m in range(len(notas)):
        print("   " + notasClase[m][0] + " en: " + strRound(notas[m], 1))
        promTareas += notas[m]
    promTareas /= max(1.0, len(notas))
    print("   el promedio general fué: " + strRound(promTareas, 1))

def registroEstudiantes():
    global estudiantes
    print("   " + funciones[15])
    # la lista estudiantes tiene listas asi [nombre, edad, genero, nota]
    print("   1. ingresar estudiante")
    print("   2. información etudiantes")
    print("   3. información general")
    print("   4. eliminar estudiante")
    print("   5. eliminar a todos")
    print("   6. salir al menú")
    while True:
        print("   ...")
        sel = input("-> ")
        if sel == "1":
            est = input("-> escriba el nombre del estudiante: ")
            if est != "":
                edad = getInt("digite la edad")
                genero = input("-> es de género femenino (s/n): ").lower() == "s"
                nota = getFloat("digite la nota obtenida (0 a 5)")
                ok = False
                for e in range(len(estudiantes)):
                    if estudiantes[e][0] == est:
                        estudiantes[e][1] = edad
                        estudiantes[e][2] = genero
                        estudiantes[e][3] = nota
                        print("      actualizado exitosamente")
                        ok = True
                        break
                if not ok:
                    estudiantes.append([est, edad, genero, nota])
                    print("      agregado exitosamente")
        elif sel == "2":
            if len(estudiantes) == 0:
                print("      no hay estudiantes")
            else:
                n = 1
                for est in estudiantes:
                    txt = "(" + str(n) + ") " + est[0]
                    txt += " (Fem " if est[2] else " (Mas "
                    txt += str(est[1]) + ") " + strRound(est[3])
                    print("      " + txt)
                    n += 1
        elif sel == "3":
            total = len(estudiantes)
            print("      hay " + str(total) + " estudiantes")
            if total > 0:
                edades = 0.0
                notas = 0.0
                maxima = 0.0
                minima = 5.0
                aprobados = 0
                generos = 0.0
                for est in estudiantes:
                    edades += est[1]
                    notas += est[3]
                    maxima = max(maxima, est[3])
                    minima = min(minima, est[3])
                    if est[3] >= 3:
                        aprobados += 1
                    if est[2]:
                        generos += 1.0
                print("      edad promedio: " + strRound(edades / total, 0))
                print("      nota promedio: " + strRound(notas / total, 1))
                print("      nota máxima: " + strRound(maxima, 1))
                print("      nota mínima: " + strRound(minima, 1))
                print("      aprobados: " + str(aprobados))
                porcent = (generos / total) * 100.0
                print("      cantidad (Fem): " + strRound(porcent, 0) + "%")
        elif sel == "4":
            est = input("-> escriba el nombre a eliminar: ")
            if est != "":
                ok = False
                for e in range(len(estudiantes)):
                    if estudiantes[e][0] == est:
                        estudiantes.pop(e)
                        print("      borrado exitosamente")
                        ok = True
                        break
                if not ok:
                    print("      no se encontró el nombre")
        elif sel == "5":
            estudiantes = []
            print("      registro limpio")
        elif sel == "6":
            print("      saliendo del registro")
            break
        else:
            print("      comando no válido")

def ConversorTemp():
    print("   " + funciones[16])
    print("   digite la unidad de su dato: 1.Celsius, 2.Kelvin, 3.Fahrenheit")
    sel = input("-> ")
    tmp = getFloat("digite la magnitud de la temperatura")
    if sel == "1": # Celsius
        print("   en Fahrenheit es: " + strRound(32.0 + (9.0 * tmp / 5.0)))
        print("   en Kelvin es: " + strRound(tmp + 273.15))
    elif sel == "2": # Kelvin
        print("   en Fahrenheit es: " + strRound(32.0 + (9.0 * (tmp - 273.15) / 5.0)))
        print("   en Celsius es: " + strRound(tmp - 273.15))
    elif sel == "3": # Fahrenheit
        print("   en Celsius es: " + strRound(5.0 * (tmp - 32.0) / 9.0))
        print("   en Kelvin es: " + strRound(273.15 + (5.0 * (tmp - 32.0) / 9.0)))
    else:
        print("   selección inválida")

def indiceMasaCorporal():
    global indMasCorp
    print("   " + funciones[17])
    altura = abs(getFloat("digite la altura en metros"))
    peso = abs(getFloat("digite el peso en kilogramos"))
    if altura == 0 or peso == 0:
        print("   los valores no pueden ser 0")
    else:
        indice = peso / (altura ** 2)
        for i in range(len(indMasCorp)):
            if indice <= indMasCorp[i][0]:
                print("   el IMC es: " + strRound(indice) + ", " + indMasCorp[i][1])
                break

# herramientas usadas por cualquier funcion del software

def getInt(texto, reintentar=False):
    value = input("-> " + texto + ": ")
    try:
        value = int(value)
    except:
        if reintentar:
            value = getInt(texto, True)
        else:
            value = 0
    return value

def getFloat(texto, reintentar=False):
    value = input("-> " + texto + ": ")
    try:
        value = float(value)
    except:
        if reintentar:
            value = getFloat(texto, True)
        else:
            value = 0.0
    return value

def strRound(value, decimales=4):
    if value == int(value):
        return str(int(value))
    if decimales == 0:
        return str(int(round(value)))
    else:
        return str(round(value, decimales))

def getPorcent(texto, reintentar=False):
    value = input("-> " + texto + ": ")
    try:
        value = abs(float(value)) / 100.0
    except:
        if reintentar:
            value = getPorcent(texto, True)
        else:
            value = 0
    return value

# lanzar el software
main()
