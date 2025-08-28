import random
data = []
for i in range(20):
    data.append(int(20.0 + random.random() * 20.0))
for i in range(10):
    data.append(int(25.0 + random.random() * 10.0))
for i in range(5):
    data.append(int(28.0 + random.random() * 4.0))

data = [21, 30, 20, 24, 21, 31, 30, 35, 36, 22, 39,
    31, 20, 33, 25, 27, 27, 35, 24, 35, 25, 31, 28,
    31, 28, 25, 29, 25, 33, 26, 28, 31, 30, 30, 28]
print(data)

media = 0.0
for d in data:
    media += d
media /= len(data)
print("media A:", media)

mediag = 1.0
for d in data:
    mediag *= d
mediag = pow(mediag, 1.0 / len(data))
print("media G:", mediag)

mediah = 0.0
for d in data:
    mediah += 1.0 / d
mediah = len(data) / mediah
print("media H:", mediah)

unicos = [[], []]
for d in data:
    if not d in unicos[0]:
        unicos[0].append(d)
        unicos[1].append(1)
    else:
        unicos[1][unicos[0].index(d)] += 1
moda = unicos[0][unicos[1].index(max(unicos[1]))]
print("moda:", moda)

data.sort()
n = len(data)
if n % 2 != 0:
    mediana = data[int((n+1)/2)]
else:
    mediana = (data[int(n/2)] + data[int((n/2)+1)]) / 2.0
print("mediana:", mediana)

varianza = 0.0
for d in data:
    varianza += pow(d - media, 2.0)
varianza /= len(data)
print("varianza:", varianza)

desviest = pow(varianza, 0.5)
print("desv. estándar: ", desviest)
