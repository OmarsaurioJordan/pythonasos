# Regresion Lineal por Omar Jordan Jordan ADSO24 2024

def main():
    print("***Regresion Lineal por Omar ADSO24***")
    print("...")
    data = cargadatos()
    xmedia = media(data[0])
    ymedia = media(data[1])
    pendiente = dividendo(data, xmedia, ymedia) / divisor(data[0], xmedia)
    desfase = ymedia - pendiente * xmedia
    print("...")
    print("y(x) =", pendiente, "x +", desfase)
    print("...")
    evaluacion(pendiente, desfase)
    print("...")
    revaluacion(pendiente, desfase)
    print("*fin*")

def cargadatos():
    data = [[], []]
    while True:
        try:
            xy = input("digite dupla x,y: ").split(",")
            xy = [float(d) for d in xy]
            if len(xy) == 2:
                data[0].append(xy[0])
                data[1].append(xy[1])
                print("  dupla ", len(data), " agregada")
            else:
                print("  deben ser duplas")
        except:
            print("  mala escritura")
        if input("desea ingresar otra (s/n): ") == "n":
            break
    return data

def evaluacion(pendiente=0.0, desfase=0.0):
    while True:
        try:
            x = float(input("digite un valor para x: "))
            print("y =", pendiente * x + desfase)
        except:
            print("  mala escritura")
        if input("desea ingresar otro (s/n): ") == "n":
            break

def revaluacion(pendiente=0.0, desfase=0.0):
    while True:
        try:
            y = float(input("digite un valor para y: "))
            print("x =", (y - desfase) / pendiente)
        except:
            print("  mala escritura")
        if input("desea ingresar otro (s/n): ") == "n":
            break

def media(lista=[]):
    total = 0.0
    for item in lista:
        total += item
    return total / len(lista)

def dividendo(listas=[[],[]], media1=0.0, media2=0.0):
    total = 0.0
    for i in range(len(listas[0])):
        total += (listas[0][i] - media1) * (listas[1][i] - media2)
    return total

def divisor(lista=[], valmedia=0.0):
    total = 0.0
    for item in lista:
        total += (item - valmedia) ** 2.0
    return total

main()
