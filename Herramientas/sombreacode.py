# convierte archivo txt en format BBcode txt

# abrir archivo
nn = input("digite nombre de archivo con extension: ")
f = open(nn, 'r')
txt = f.read()
f.close()

# colores listados, formato #000000
color = []
color.append("92ff8e") # 0 verdecito comentario
color.append("ff8cff") # 1 morado especial keys
color.append("ff9259") # 2 rojizo cadena string
color.append("9298e4") # 3 azules variables

# palabras clave y su ind de color
clave = []
clave.append(["import", 1])
clave.append(["as", 1])
clave.append(["for", 1])
clave.append(["in", 1])
clave.append(["if", 1])
clave.append(["elif", 1])
clave.append(["else", 1])
clave.append(["switch", 1])
clave.append(["case", 1])
clave.append(["break", 1])
clave.append(["continue", 1])
clave.append(["exit", 1])
clave.append(["while", 1])
clave.append(["do", 1])
clave.append(["until", 1])
clave.append(["var", 1])
clave.append(["return", 1])
clave.append(["def", 1])
clave.append(["print", 1])

# para guardar fragmentos [str, ind] ind es abre
tramos = []

# guardar cadenas de texto y comentarios
ok = True
sub = ""
ini = 0
while ok:
    ok = False
    abre = 0 # 0:null, 1:str, 2:cmnt, 3:chr
    for c in range(len(txt)):
        if abre == 2:
            if txt[c] == '\n':
                tramos.append([sub, abre])
                txt = txt[:ini] + "$$$$$" + str(len(tramos) - 1) + txt[c:]
                ok = True
                break
            else:
                sub += txt[c]
        elif abre == 1:
            sub += txt[c]
            if txt[c] == '"':
                tramos.append([sub, abre])
                if c == len(txt) - 1:
                    txt = txt[:ini] + "$$$$$" + str(len(tramos) - 1)
                else:
                    txt = txt[:ini] + "$$$$$" + str(len(tramos) - 1) + txt[c+1:]
                ok = True
                break
        elif abre == 3:
            sub += txt[c]
            if txt[c] == "'":
                tramos.append([sub, abre])
                if c == len(txt) - 1:
                    txt = txt[:ini] + "$$$$$" + str(len(tramos) - 1)
                else:
                    txt = txt[:ini] + "$$$$$" + str(len(tramos) - 1) + txt[c+1:]
                ok = True
                break
        else:
            if txt[c] == '"':
                sub = '"'
                ini = max(0, c)
                abre = 1
            elif txt[c] == '#':
                sub = '#'
                ini = max(0, c)
                abre = 2
            elif txt[c] == "'":
                sub = "'"
                ini = max(0, c)
                abre = 3

# pintar palabras especiales
for c in clave:
    for t in ["\n", "\t", " ", "(", "["]:
        for n in [":", "=", " ", "(", "[", ")", "]"]:
            txt = txt.replace(t + c[0] + n,
                t + "[color=#" + color[c[1]] + "]" + c[0] + "[/color]" + n)

# poner tramos nuevamente
for t in range(len(tramos)):
    if tramos[t][1] == 1 or tramos[t][1] == 3:
        txt = txt.replace("$$$$$" + str(t),
                        "[color=#" + color[2] + "]" +
                        tramos[t][0] + "[/color]")
    elif tramos[t][1] == 2:
        txt = txt.replace("$$$$$" + str(t),
                        "[color=#" + color[0] + "]" +
                        tramos[t][0] + "[/color]")
    else:
        txt = txt.replace("$$$$$" + str(t),
                        "[color=#" + color[3] + "]" +
                        tramos[t][0] + "[/color]")

# guardar nuevo archivo
f = open('tmp.txt', 'w')
f.write(txt)
f.close()
