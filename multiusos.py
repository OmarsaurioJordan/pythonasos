import numpy as np
import matplotlib.pyplot as plt
import socket
import threading
import time
import datetime as dt
import sounddevice as sd
import soundfile as sf
from scipy import stats
from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav

def optimizar(ini, gra):
    mejor, elite, pico = unidad(ini)
    mejor = abs(opti - mejor)
    for g in range(genera):
        res, gen, pp = unidad(elite + muta * (-1 + np.random.rand(2) * 2))
        if abs(opti - res) < mejor:
            mejor = abs(opti - res)
            elite = gen
            pico = pp
        if mejor <= errorMinimo or g == genera - 1:
            print("generacion {}".format(g + 1))
            break
    print("{:0.3f} fric, {:0.1f} acel".format(elite[0], elite[1]))
    print("{:0.4f} mejor, {:0.1f}s estable".format(mejor, pico))
    print("")
    if gra:
        graficar(elite)
    return elite[0], elite[1], pico

def unidad(gen):
    h = np.zeros(1000)
    pico = 0
    for i in range(1, h.size):
        h[i] = h[i - 1] * gen[0] + gen[1]
        if abs(opti - h[i]) <= opti * 0.005 and pico == 0:
            pico = i / (2 * 20)
    return h[-1], gen, pico

def graficar(gen):
    h = np.zeros(1000)
    for i in range(1, h.size):
        h[i] = h[i - 1] * gen[0] + gen[1]
    g = np.zeros(1000) + opti
    t = np.arange(h.size) / (2 * 20)
    plt.plot(t, h)
    plt.plot(t, g)
    plt.show()

def variosOpti():
    global genera
    global opti
    global errorMinimo
    global muta
    genera = 10000
    opti = (2 * 20) * 10  # s . limiagua
    errorMinimo = 0.05
    muta = np.array([0.001, 0])
    optimizar(np.array([0.95, 2]), True)
    optimizar(np.array([0.95, 20]), True)
    # graficar(np.array([0.95, 4]))

def areaCirculos(r1, r2, d2, paso, draw):
    sw = paso * 0.01
    xxx = np.arange(min(-r1, d2 - r2), max(r1, d2 + r2) + sw, paso)
    yyy = np.arange(min(-r1, -r2), max(r1, r2) + sw, paso)
    area = np.array([0, 0, 0], dtype=float)
    for x in xxx:
        for y in yyy:
            i1 = np.sqrt(np.power(x, 2) + np.power(y, 2))
            if i1 <= r1:
                area[0] += 1
            i2 = np.sqrt(np.power(d2 - x, 2) + np.power(y, 2))
            if i2 <= r2:
                area[1] += 1
            if i1 <= r1 and i2 <= r2:
                area[2] += 1
    area *= np.power(paso, 2)
    if draw:
        print("r1: {:0.2f}, r2: {:0.2f}, d2: {:0.2f}, paso: {:0.2f}".format(r1, r2, d2, paso))
        print("")
        print("Circulo 1:")
        a1 = np.pi * np.power(r1, 2)
        print("area real: {:0.2f}".format(a1))
        print("area virt: {:0.2f}".format(area[0]))
        print("error: {:0.2f}".format(abs(a1 - area[0])))
        print("error%: {:0.2f} %".format(100 * abs(a1 - area[0]) / a1))
        print("")
        print("Circulo 2:")
        a2 = np.pi * np.power(r2, 2)
        print("area real: {:0.2f}".format(a2))
        print("area virt: {:0.2f}".format(area[1]))
        print("error: {:0.2f}".format(abs(a2 - area[1])))
        print("error%: {:0.2f} %".format(100 * abs(a2 - area[1]) / a2))
        print("")
        print("Ambos Circulos Interseccion:")
        print("area virt: {:0.2f}".format(area[2]))
        print("area circulo1%: {:0.2f} %".format(100 * area[2] / area[0]))
        print("area circulo2%: {:0.2f} %".format(100 * area[2] / area[1]))
        print("area total%: {:0.2f} %".format(100 * area[2] / (area[0] + area[1])))
        x = np.linspace(-r1, r1, 100)
        y = np.sqrt(np.power(r1, 2) - np.power(x, 2))
        plt.plot(x, y)
        plt.plot(x, -y)
        x = np.linspace(-r2, r2, 100)
        y = np.sqrt(np.power(r2, 2) - np.power(x, 2))
        x += d2
        plt.plot(x, y)
        plt.plot(x, -y)
        plt.show()
    return area[2]

def variosCirculos():
    total = 10
    patrones = np.zeros((total, 4), dtype=float)
    for p in range(total):
        r1 = np.random.rand(1)[0] * 9.0 + 1.0
        r2 = np.random.rand(1)[0] * 9.0 + 1.0
        d2 = np.random.rand(1)[0] * (r1 + r2)
        a = areaCirculos(r1, r2, d2, 0.1, False)
        patrones[p, :] = np.array([r1, r2, d2, a])
    return patrones

def esperaUDP(UDP, escape):
    while True:
        try:
            msj = UDP.recv(1024).decode()
            if msj == escape:
                break
            else:
                print(".")
                print("r: " + msj)
        except:
            pass

def UDP():
    escape = "exit666"
    # servidor
    UDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    port1 = input("port mio (def 1024): ")
    if port1 == "":
        port1 = 1024
    else:
        port1 = int(port1)
    UDP.bind(("127.0.0.1", port1))
    # cliente
    port2 = input("port otro (def 1025): ")
    if port2 == "":
        port2 = 1025
    else:
        port2 = int(port2)
    ip = input("ip otro (def local): ")
    if ip == "":
        ip = "127.0.0.1"
    ipport = (ip, port2)
    # hilo
    h = threading.Thread(target=esperaUDP, args=[UDP, escape])
    h.start()
    while True:
        time.sleep(0.1)
        msj = input("msj (void to exit): ")
        if msj == "":
            UDP.sendto(str.encode(escape), ("127.0.0.1", port1))
            break
        else:
            try:
                UDP.sendto(str.encode(msj), ipport)
                print("enviado")
            except:
                print("error")

def entreno():
    print("Entrenador...")
    inifin = sf.read("ejerinifin.wav")
    # 0: bajo, 1: medio, 2: alto, 3: sostenido
    sonido = [sf.read("ejer0.wav"), sf.read("ejer1.wav"),
              sf.read("ejer2.wav"), sf.read("ejer1.wav")]
    probab = [3, 2, 3, 1]
    demora = [1.5, 1.25, 1.5, 5.75]
    if input("-> con sostenido (S/n): ") == "n":
        probab[3] = 0
    total = input("-> Segundos sesion (vacio 60): ")
    total = 60 if total == "" else int(total)
    input("-> Enter start...")
    sd.play(inifin[0], inifin[1])
    time.sleep(5)
    print("Iniciado...")
    act = -1
    while total > 0:
        aact = act
        while True:
            act = []
            for a in range(len(probab)):
                for n in range(probab[a]):
                    act.append(a)
            act = act[np.random.randint(len(act))]
            if aact != act or probab[3] != 0:
                break
        if (aact != act and not (aact == 1 and act == 3) and
                not (aact == 3 and act == 1)):
            sd.play(sonido[act][0], sonido[act][1])
        az = np.random.ranf() * 0.5
        time.sleep(demora[act] + az)
        total -= demora[act] + az
    print("Finalizado...")
    sd.play(inifin[0], inifin[1])
    time.sleep(2)

def dec2bin2dec(n, todec):
    if todec:
        print(int(n, 2))
    else:
        print(bin(n).replace("0b", ""))

def SSVEP1():
    print("***sesion***")
    tab = "    "
    reloj = ["60", "10", "2", "3"]
    bloque = ["magenta", "azul", "rojo"]
    serie = ["6", "7", "8", "9"]
    trial = [str(i + 1) for i in range(3)]
    total = 0
    for c in bloque:
        print("bloque " + c)
        for f in serie:
            print(tab + "serie " + f)
            for t in trial:
                print(tab + tab + "trial " + t)
                print(tab + tab + tab + reloj[3] + " s")
                total += int(reloj[3])
                if t != trial[-1]:
                    print(tab + tab + "reposo " + reloj[2] + " s")
                    total += int(reloj[2])
            if f != serie[-1]:
                print(tab + "reposo" + reloj[1] + " s")
                total += int(reloj[1])
        if c != bloque[-1]:
            print("reposo " + reloj[0] + " s")
            total += int(reloj[0])
    print("...")
    print("total = " + str(total) + " s = " + str(total / 60) + " min")
    print("***fin***")

def SSVEP2():
    print("***sesion***")
    reloj = ["60", "10", "2", "3"]
    bloque = ["magenta", "azul", "rojo"]
    serie = ["6", "7", "8", "9"]
    trial = [str(i + 1) for i in range(3)]
    print("- {}, {}, {}, {}".format("Black", "0", "-1", reloj[0]))
    for c in bloque:
        for f in serie:
            for t in trial:
                print("- {}, {}, {}, {}".format(c, f, t, reloj[3]))
                print("- {}, {}, {}, {}".format(c, f, "-1", reloj[2]))
            print("- {}, {}, {}, {}".format(c, "0", "-1", reloj[1]))
        print("- {}, {}, {}, {}".format("Black", "0", "-1", reloj[0]))
    print("***fin***")

def muestraseno(t):
    n = np.arange(t + 1)
    x = np.sin((n / t) * 2.0 * np.pi)
    for i in n:
        print("{}: {:.4f}".format(i, x[i]))

def conTxt(tot=0, num=0, txt="", palab=[], peso=1):
    # busca si una de las palabras en el array palab esta en el texto
    con = 0
    for p in palab:
        if p in txt:
            con = peso
            break
    # reempaza el texto por el mismo, quitandole las palabras buscadas
    ntxt = txt
    for p in palab:
        ntxt = ntxt.replace(p, "")
    return tot + peso, num + con, ntxt

def complejiPalabra():
    while True:
        # ingresa una frase o parrafo para chequear su complejidad, vacio saldra del programa
        txt = input("Frase: ")
        if txt == "":
            break
        else:
            # prepara el texto para adecuarlo, por ejemplo poniendolo en minusculas y quitando tildes
            txt = " " + txt.lower()
            txt = txt.replace(",", "").replace(".", "").replace(";", "")
            txt = txt.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
            # modularmente, pregunta por letras o fonemas, al final puede agregar un peso diferente a cada uno
            # por ejemplo las vocales por ser importantes pueden tener mayor peso
            # preguntar primero por complejos, por ejemplo, primero ch luego c
            # el primer llamado inicializa tot y num en cero
            [tot, num, txt] = conTxt(0, 0, txt, ["a"], 5)
            [tot, num, txt] = conTxt(tot, num, txt, ["e"], 5)
            [tot, num, txt] = conTxt(tot, num, txt, ["i"], 5)
            [tot, num, txt] = conTxt(tot, num, txt, ["o"], 5)
            [tot, num, txt] = conTxt(tot, num, txt, ["u", "w"], 5)
            [tot, num, txt] = conTxt(tot, num, txt, ["b", "v"])
            [tot, num, txt] = conTxt(tot, num, txt, ["s", "z", "x"])
            [tot, num, txt] = conTxt(tot, num, txt, ["ll", "y"])
            [tot, num, txt] = conTxt(tot, num, txt, ["ch"])
            [tot, num, txt] = conTxt(tot, num, txt, ["c", "q", "k"])
            [tot, num, txt] = conTxt(tot, num, txt, ["rr", " r"])
            [tot, num, txt] = conTxt(tot, num, txt, ["r"])
            [tot, num, txt] = conTxt(tot, num, txt, ["t", "d", "p"])
            [tot, num, txt] = conTxt(tot, num, txt, ["f", "j"])
            [tot, num, txt] = conTxt(tot, num, txt, ["g"])
            [tot, num, txt] = conTxt(tot, num, txt, ["l"])
            [tot, num, txt] = conTxt(tot, num, txt, ["m"])
            [tot, num, txt] = conTxt(tot, num, txt, ["n"])
            [tot, num, txt] = conTxt(tot, num, txt, ["ñ"])
            # muestra el resultado porcentual
            print("Complejidad: {:.4f} %".format((num / max(1, tot)) * 100))

def vozComp(file):
    (rate, sig) = wav.read(file)
    mfcc_feat = mfcc(sig, rate)
    fbank_feat = logfbank(sig, rate)
    return mfcc_feat, fbank_feat

def vozVer(file):
    (mfcc_feat, fbank_feat) = vozComp(file)
    print("fbank(1):")
    print(np.shape(fbank_feat))
    print(fbank_feat[1, :])
    print("mfcc(1):")
    print(np.shape(mfcc_feat))
    print(mfcc_feat[1, :])
    print("mean fbank:")
    print(np.mean(fbank_feat, axis=0))
    print("mean mfcc:")
    print(np.mean(mfcc_feat, axis=0))

def promedioTrozos(matrix, grupo):
    L = np.shape(matrix)[0]
    output = np.zeros((0, 3), dtype=float)
    n = 0
    while n < L:
        aux = np.mean(matrix[n: min(L, n + grupo), :], axis=0)
        output = np.append(output, np.atleast_2d(aux), axis=0)
        n += grupo
    return output.copy()

def Kmedias(matrix, clusters, iteraciones):
    # crear las estructuras de datos y la inicializacion al azar
    L = np.shape(matrix)[0]
    aux = np.zeros((L, 1))
    puntos = np.concatenate((matrix, aux), axis=1)
    dMax = np.max(matrix, axis=0)
    dMin = np.min(matrix, axis=0)
    centros = np.random.random_sample((clusters, np.shape(matrix)[1]))
    centros = (dMax - dMin) * centros + dMin
    # comenzar el ciclo con sus dos partes
    i = 0
    while i < iteraciones:
        i += 1
        fin = True
        # asociar los puntos al centroide mas cercano
        for p in range(L):
            dist = np.sum(np.power(centros - puntos[p, :-1], 2), axis=1)
            puntos[p, -1] = np.argmin(dist)
        # mover los centroides a sus puntos asociados
        for c in range(clusters):
            viejo = centros[c, :].copy()
            t = 0.0
            encola = True
            for p in range(L):
                if puntos[p, -1] == c:
                    if encola:
                        encola = False
                        centros[c, :] *= 0
                    centros[c, :] += puntos[p, :-1]
                    t += 1.0
            centros[c, :] /= (t if t != 0 else 1.0)
            # verificar si hubo cambios
            if fin:
                if not (False in (viejo == centros[c, :])):
                    fin = False
        # frenar si no hubo cambios, termina antes de iteraciones
        if fin:
            break
    return centros

def cambiarFrecuencia(signal, fs, newfs):
    if newfs != fs:
        oriY = signal.copy()
        oriX = np.arange(oriY.size) / fs
        newX = np.arange(oriY.size) / newfs
        newY = np.interp(newX, oriX, oriY)
        return newY, newfs
    else:
        return signal, fs

def notasInstru(soloAct):
    # opcional 1, opcional 2, taller filtrado, simulacion dispositivo

    quisez1 = np.mean([2.5, 1.7, 2.5, 1.7, 1.7, 4.4, 3.1])  # 2.5
    tallerAO = 0.0
    quisez2 = np.mean([4.38, 4.38, 3.75, tallerAO])
    fases = np.array([4.0, 4.5, 3.0])

    proyecto = np.sum(np.array([0.25, 0.25, 0.5]) * fases)
    pond = np.array([0.35, 0.35, 0.3])
    nota = np.array([quisez1, quisez2, proyecto])
    print("nota actual: " + str(round(np.sum(pond * nota), 1)))

    if not soloAct:
        buscar = 2
        nota[buscar] = 0.0
        for i in range(50):
            nota[buscar] = i / 10.0
            final = np.sum(pond * nota)
            if final >= 3.0:
                print("minimo necesitas: " + str(round(nota[buscar], 1)))
                break
        nota[buscar] = 5.0
        print("mejor nota posible: " + str(round(np.sum(pond * nota), 1)))

# notInst(2.5, 1.7, 2.5, 1.7, 1.7, 4.4, 4.9, 3.1, 4.4, 4.4, 3.8, 1, 3.31, 4.0, 4.5, 1, 3.2, 0.0)
def notInst(qA1, qA2, qA3, qA4, qA5, tA1, tA2, tA3, qB1, qB2, qB3, tB1, tB2, f1, f2, f3, op1, op2):
    """
    :param qA1: quiz 1,                               1 parte
    :param qA2: quiz 2,                               1 parte
    :param qA3: quiz 3,                               1 parte
    :param qA4: quiz 4,                               1 parte
    :param qA5: quiz 5,                               1 parte
    :param tA1: taller de medicion en el salon 1,     1 parte
    :param tA2: taller de medicion en el salon 2,     1 parte
    :param tA3: transductores en el laboratorio,      1 parte
    :param qB1: quiz 1,                               2 parte
    :param qB2: quiz 2,                               2 parte
    :param qB3: quiz 3,                               2 parte
    :param tB1: taller de presupuesto AO,             2 parte
    :param tB2: taller sobre filtrado,                2 parte
    :param f1: fase 1, global,                       proyecto
    :param f2: fase 2, subgrupos,                    proyecto
    :param f3: fase 3, global,                       proyecto
    :param op1: opcional 1,                           1 parte
    :param op2: opcional 2,                           2 parte
    :return: nota final
    """
    # ingreso de notas como vectores
    quisez1 = max(op1, np.mean([qA1, qA2, qA3, qA4, qA5, tA1, tA2, tA3]))
    quisez2 = max(op2, np.mean([qB1, qB2, qB3, tB1, tB2]))
    fases = np.array([f1, f2, f3])
    # operacion segun los pesos ponderados
    proyecto = np.sum(np.array([0.3, 0.3, 0.4]) * fases)
    notas = np.array([quisez1, quisez2, proyecto])
    nota = np.sum(np.array([0.35, 0.35, 0.3]) * notas)
    print("Nota: {:.1f}".format(nota))
    return nota

def tuercas():
    pob = []
    for t in range(100000):
        total = 20.0
        neto = 18.0
        error = 0.3
        peso = 0.0
        for i in range(int(total)):
            peso += neto + (np.random.ranf() * 2.0 - 1.0) * error
        pob.append(peso / total)
    pob = np.array(pob)
    print(np.max(pob))
    print(np.min(pob))
    print(np.mean(pob))

def senox():
    t = np.linspace(0, 1, 3090)
    m = np.array([55.8, 42.0, 38.22, 27.01, 22.5])
    x = m[0] * np.sin(2.0 * np.pi * 130.0 * t) +\
        m[1] * np.sin(2.0 * np.pi * 205.0 * t) + \
        m[2] * np.sin(2.0 * np.pi * 40.0 * t) +\
        m[3] * np.sin(2.0 * np.pi * 666.0 * t) +\
        m[4] * np.sin(2.0 * np.pi * 1000.0 * t)
    print(np.max(x))
    print(np.sum(m))
    plt.plot(t, x)
    plt.show()

def ecuRectaPro():
    ampl = np.array([64.75,59.04,52.72,45.99,38.85,31.47,23.81,15.97,8.02,3.02])
    frec = np.array([900.08,800.07,700.06,600.05,500.05,400.04,300.03,200.02,100.01,9.81])
    m = 0.0715
    b = 7.559
    e = 999999999.0
    iteraciones = 100000
    for i in range(iteraciones):
        vm = m
        vb = b
        z = (1.0 - float(i) / iteraciones) * 10.0
        m += (np.random.ranf() * 2.0 - 1.0) * z
        b += (np.random.ranf() * 2.0 - 1.0) * z
        ne = 0.0
        for v in range(frec.size):
            ne += np.power(ampl[v] - (m * frec[v] + b), 2.0)
        if ne <= e:
            e = ne
        else:
            m = vm
            b = vb
    print("m: {:.4f}\nb: {:.4f}\ne: {:.4f}".format(m, b, e))

def CZener():
    print("***Zener***")
    total = 25
    print("{} with 5 c/u".format(total))
    print(".")
    iteraciones = 1000000
    general = []
    for i in range(iteraciones):
        np.random.seed()
        cartas = np.random.randint(0, 5, total)
        np.random.seed()
        mente = np.random.randint(0, 5, total)
        result = np.where(cartas == mente, 1, 0)
        conteo = np.zeros(5, dtype=int)
        for t in range(total):
            if result[t] == 1:
                conteo[cartas[t]] += 1
        general.append(conteo.sum())
        #print("Result: {}, {}".format(conteo.sum(), conteo.sum() - 5))
    general = np.array(general, dtype=int)
    print(".")
    print("Mean: {}".format(int(general.mean() * 10) / 10))
    print("Median: {}".format(int(np.median(general) * 10) / 10))
    print("Mode: {}".format(stats.mode(general)[0][0]))
    print("Min-Max: {} - {}".format(general.min(), general.max()))
    print(".")
    prob = []
    for t in range(total + 1):
        prob.append(np.where(general == t, 1, 0).sum())
    for p in range(len(prob)):
        if prob[-1] == 0:
            prob.pop(-1)
        else:
            break
    for p in range(len(prob)):
        print("{} -> {} -> {}%".format(p, prob[p], int((prob[p] / iteraciones) * 10000) / 100))
    prob = np.array(prob, dtype=int)
    plt.stem(prob)
    plt.show()

# para maltus1
tabla1 = [["NumTrafo", "NumCli", "TariCli", "MarcCli"]]
tabla2 = [["NumCli", "Mes1", "Mes2", "Mes3", "Mes4", "Mes5", "Mes6"]]

def maltus1():
    global tabla1, tabla2
    print("***Trafos de Celsia 2021 UV***")
    print(".")
    print("...Digite:")
    print("trafo cliente tarifa marca m1 m2 m3 m4 m5 m6 (llenar tablas)")
    print("z filas (llenar tablas al azar)")
    print("trafo (verificar transformador)")
    print("v (ver tablas)")
    print("x (salir)")
    print(".")
    while True:
        sel = input("-> ")
        if sel == "":
            pass
        elif sel == "x":
            print(".")
            break
        elif sel == "v":
            total = len(tabla1)
            print("clientes: {}".format(total))
            if total < 26:
                print(".")
                for t in range(total):
                    print(tabla1[t])
                print(".")
                for t in range(total):
                    print(tabla2[t])
        elif sel[0] == "z":
            try:
                data = sel.split(" ")
                azarTabla(int(data[1]))
            except:
                print("   error formato parametro")
        elif sel.count(" ") == 9:
            data = sel.split(" ")
            if len(data) == 10:
                try:
                    addTabla(int(data[0]), int(data[1]), data[2], data[3],
                             float(data[4]), float(data[5]), float(data[6]),
                             float(data[7]), float(data[8]), float(data[9]))
                except:
                    print("   error formato parametros")
            else:
                print("   error numero parametros")
        else:
            try:
                verificador(int(sel))
            except:
                print("   error formato parametro")
        print(".")
    print("***finalizado***")

def addTabla(trafo, cliente, tarifa, marca, m1, m2, m3, m4, m5, m6, chillar=True):
    global tabla1, tabla2
    ok = True
    for t in range(1, len(tabla2)):
        if cliente == tabla2[t][0]:
            ok = False
            break
    if ok:
        tabla1.append([trafo, cliente, tarifa, marca])
        tabla2.append([cliente, m1, m2, m3, m4, m5, m6])
    elif chillar:
        print("   error cliente duplicado")

def azarTabla(filas):
    for i in range(filas):
        m = np.round(np.random.random_sample(6) * 2000.0) / 10.0 # kWh de consumo
        addTabla(np.random.randint(1, 20), # numero de transformadores
                 np.random.randint(1, 100000), # numero de clientes
                 "R" + str(np.random.randint(1, 4)), # numero de estratos (tarifas)
                 np.random.choice(["G", "P", "U", "A", "B", "C", "Z", "M"]), # marcas
                 m[0], m[1], m[2], m[3], m[4], m[5], False)

def verificador(trafo):
    global tabla1, tabla2
    total = 0
    inteli = 0
    pobres = 0
    promed = 0
    okpromedio = True
    for t in range(1, len(tabla1)):
        if tabla1[t][0] == trafo:
            total += 1
            if tabla1[t][3] == "G" or tabla1[t][3] == "P" or tabla1[t][3] == "U":
                inteli += 1
                if tabla1[t][2] == "R1" or tabla1[t][2] == "R2":
                    pobres += 1
                    promed += (tabla2[t][1] + tabla2[t][2] + tabla2[t][3] +
                           tabla2[t][4] + tabla2[t][5] + tabla2[t][6]) / 6.0
    promed /= pobres
    if promed < 100.0:
        okpromedio = False
    if total != 0:
        print("   total clientes: {} (100.0%)".format(total))
        print("   marca inteligente: {} ({:.1f}%)".format(inteli, (inteli / total) * 100))
        print("   pobres con marca-i: {} ({:.1f}%)".format(pobres, (pobres / total) * 100))
        porcent = (pobres / inteli) * 100
        print("   pobres / marca-i: {:.1f}%".format(porcent))
        print("   promedio kWh: {:.1f}".format(promed))
        if porcent > 80 and okpromedio:
            print("   Proceder")
        elif porcent > 70:
            print("   Tentativo")
        else:
            print("   Impensable")
    else:
        print("   no se encontro trafo")

def Cuy(lim, neg):
    for n in range(1, lim + 1):
        res = "->{}".format(n)
        for s in ([1, -1] if neg else [1]):
            mul = pow(2, n)
            for i in range(mul):
                m = "{0:b}".format(i)
                while len(m) < n:
                    m = "0" + m
                m = m.replace("1", "2").replace("0", "1")
                m = s * int(m)
                w = m / mul
                if w == round(w):
                    res += ": {}".format(m)
                    mul = -1
                    break
            if mul == -1:
                break
        print(res)
        if not ":" in res:
            break

def charOk():
    txt = "#|!$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿЀЁЂЃЄЅІЇЈЉЊЋЌЍЎЏАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяѐёђѓєѕіїјљњћќѝўџѠѡѢѣѤѥѦѧѨѩѪѫѬѭѮѯѰѱѲѳѴѵѶѷѸѹѺѻѼѽѾѿҀҁ҂҃҄҅҆҇҈҉ҊҋҌҍҎҏҐґҒғҔҕҖҗҘҙҚқҜҝҞҟҠҡҢңҤҥҦҧҨҩҪҫҬҭҮүҰұҲҳҴҵҶҷҸҹҺһҼҽҾҿӀӁӂӃӄӅӆӇӈӉӊӋӌӍӎӏӐӑӒӓӔӕӖӗӘәӚӛӜӝӞӟӠӡӢӣӤӥӦӧӨөӪӫӬӭӮӯӰӱӲӳӴӵӶӷӸӹӺӻӼӽӾӿ֐ְֱֲֳִֵֶַָֹֺֻּֽ֑֖֛֢֣֤֥֦֧֪֚֭֮֒֓֔֕֗֘֙֜֝֞֟֠֡֨֩֫֬֯־ֿ׀ׁׂ׃ׅׄ׆ׇ׈׉׊׋׌׍׎׏אבגדהוזחטיךכלםמןנסעףפץצקרשת׫׬׭׮ׯװױײ׳״׵׶׷׸׹׺׻׼׽׾׿؀؁؂؃؄؅؆؇؈؉؊؋،؍؎؏ؘؙؚؐؑؒؓؔؕؖؗ؛؜؝؞؟ؠءآأؤإئابةتثجحخدذرزسشصضطظعغػؼؽؾؿـفقكلمنهوىيًٌٍَُِّْٕٖٜٟٓٔٗ٘ٙٚٛٝٞ٠١٢٣٤٥٦٧٨٩٪٫٬٭ٮٯٰٱٲٳٴٵٶٷٸٹٺٻټٽپٿڀځڂڃڄڅچڇڈډڊڋڌڍڎڏڐڑڒړڔڕږڗژڙښڛڜڝڞڟڠڡڢڣڤڥڦڧڨکڪګڬڭڮگڰڱڲڳڴڵڶڷڸڹںڻڼڽھڿۀہۂۃۄۅۆۇۈۉۊۋیۍێۏېۑےۓ۔ەۖۗۘۙۚۛۜ۝۞ۣ۟۠ۡۢۤۥۦۧۨ۩۪ۭ۫۬ۮۯ۰۱۲۳۴۵۶۷۸۹ۺۻۼ۽۾ۿ"
    new = ""
    for t in txt:
        if t.isdigit():
            new += t
    print(new)
    new = ""
    for t in txt:
        if t.isalpha():
            new += t
    print(new)
    new = ""
    for t in txt:
        if t.isprintable() and not t.isalnum():
            new += t
    print(new)
    new = ""
    for t in txt:
        if t.isprintable():
            new += t
    print(new)

def Ordenar(listPrior, mayor):
    res = []
    n = len(listPrior)
    while n > 0:
        n -= 1
        mej = -1
        ind = -1
        for i in range(len(listPrior)):
            if listPrior[i] > mej:
                mej = listPrior[i]
                ind = i
        res.append(ind)
        listPrior[ind] = -1
    if not mayor:
        res.reverse()
    return res

def Colores(cuantos, ver):
    x = np.linspace(0, 2 * np.pi, cuantos)
    y = []
    for d in range(3):
        y.append(100 + 155 * np.cos(x * (d + 1) * 0.5 + (d * 0.5 * np.pi)))
        plt.plot(x, y[-1])
    t = "["
    for i in range(cuantos):
        t += "QColor("
        for d in range(3):
            t += str(int(y[d][i]))
            if d < 2:
                t += ", "
        t += ")"
        if i < cuantos - 1:
            t += ", "
    t += "]"
    print(t)
    if ver:
        plt.show()

Colores(16, True)
