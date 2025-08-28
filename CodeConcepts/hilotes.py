import threading
import time

iteraciones = 100000
hilos = 1000

dese = iteraciones * hilos
suma = 0
activo = True

def imprimir():
    global activo
    while activo:
        print("- " + str(int(suma * 100 / dese)) + "%")
        time.sleep(1)

def libre():
    global iteraciones
    global suma
    for _i in range(iteraciones):
        suma += 1

lock = threading.Lock()
def restri():
    global iteraciones
    global suma
    for _i in range(iteraciones):
        with lock:
            suma += 1

hilo = []
for _h in range(hilos):
    hilo.append(threading.Thread(target=libre))
    hilo[-1].start()

hilin = threading.Thread(target=imprimir)
hilin.start()

for h in hilo:
    h.join()
activo = False
print("Suma: " + str(suma))
print("Dese: " + str(dese))
