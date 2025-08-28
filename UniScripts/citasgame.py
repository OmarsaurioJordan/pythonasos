"""
Juego textual, simulador de citas sencillo, por Omwekiatl 2024
"""

import random

class Atr:
    NEURA = 0
    EMPATIA = 1
    EXTRO = 2
    APERT = 3
    DINERO = 4
    RELA = 5
    FAMILY = 6
    HIJOS = 7
    CUERPO = 8
    VESTIDO = 9
    EDAD = 10
    HOT = 11
    POLI = 12
    RELI = 13
    ARTE = 14
    ENTORNO = 15
    ETNIA = 16
    TOTAL = 17

gustotxt = [ # XX le gusta ...texto
    "la forma en que confrontas los problemas y tus reacciónes",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "tu tono de piel, cree que es muy sexy"
]

infotxtH = [
    ["indiferente", "huidizo", "resolutivo", "neurótico"],
    ["sensible", "comprensivo", "mentiroso", "maligno"],
    ["tímido", "serio", "charlador", "chistoso"],
    ["estricto", "conformista", "explorador", "muy cambiante"],
    ["pobre", "trabajador", "asalariado", "adinerado"],
    ["soltero", "comprometido", "con amante", "con crush"],
    ["ausente", "lejana", "conflictiva", "cercana"],
    ["quiere más", "ya tiene", "no quiere", "desea tener"],
    ["grueso", "delgado", "atlético", "musculoso"],
    ["grunge", "casual", "moda",  "formal"],
    ["joven", "joven-adulto", "adulto", "mayor"],
    ["flácido", "brusco", "romántico", "muy erótico"],
    ["comunismo", "socialismo", "capitalismo", "libremercado"],
    ["ateístas", "espirituales", "hinduístas", "cristianas"],
    ["el baile", "la música", "la literatura", "el dibujo"],
    ["salvaje", "rural", "urbana", "futurista"],
    ["negro", "indio", "mestizo", "blanco"]
]

accionH = [
    [ # ["indiferente", "huidizo", "resolutivo", "neurótico"],
        "le han servido el helado sin mermelada, él no hace nada por no conflictuar",
        "por accidente dejaron caer una mermelada de un estante, huyamos dice",
        "tu pantalón se manchó en el parque, él te cubre con su bufanda limpia",
        "están jugando en las máquina de pacman, y él se enoja un rato porque no gana"
    ],
    [ # ["sensible", "comprensivo", "mentiroso", "maligno"],
        "van al cine, y le notas lagrimeando ante una escena triste, pero se limpia",
        "ves que le compra una fruta a una vendedora de la calle, dice, pobre señora",
        "recibe una llamada telfónica y miente diciéndo que está en otro lugar",
        "acontece un accidente de motos, él ríe y groseramente dice, se lo merecen"
    ],
    [ # ["tímido", "serio", "charlador", "chistoso"],
        "se le nota ansioso y tenso cuando te habla, casi no sabe qué decir",
        "tiene un tono serio al hablar, incluso ante temas ridículos piensa mucho",
        "le saca cuento a todo, tiene mucho tema de qué hablar, no para",
        "no para de hacer bromas y chistes, es un loco safado de las tuercas"
    ],
    [ # ["estricto", "conformista", "explorador", "muy cambiante"],
        "la cita fué a la hora exacta, él tenía un plan meticuloso del lugar y precios",
        "van a un restaurante, y según los meseros, él siempre come ahí, toda la vida",
        "no tenía idea a dónde iba, te decía que era un lugar de la ciudad por conocer",
        "cada que menciona un plan o idea, cambia, la cita es como un juego de azar"
    ],
    [ # ["pobre", "trabajador", "asalariado", "adinerado"],
        "llega en transporte público a la cita, a un evento público de arte urbano",
        "se moviliza en moto, al final van a un mirador a comer comida rápida",
        "te recoge en su carro de segunda, van al cine y paga las entradas",
        "te lleva en una camioneta a un restaurante fino, te invita a lo que gustes"
    ],
    [ # ["soltero", "comprometido", "con amante", "con crush"],
        "expresa que está soltero y solo desde hace un tiempo, en búsqueda de algo",
        "notas que tiene pareja, él dice que no pasa nada, son relación abierta",
        "está soltero, pero si comenta que estuvo teniendo sexo con una amistad",
        "hablando de relaciónes y el pasado, dice que anda despechado por su crush"
    ],
    [ # ["ausente", "lejana", "conflictiva", "cercana"],
        "al inicio no habla de su familia, luego te das cuenta que no tiene",
        "sobre su familia, viven lejos, los visita para las festividades",
        "no quiere que toques el tema de la familia, tiene peleas con su padre",
        "durante la cita, su madre lo llamó un par de veces, para saber si volvería"
    ],
    [ # ["quiere más", "ya tiene", "no quiere", "desea tener"],
        "te muestra con orgullo fotos de sus hijos, dice que quiere tener más",
        "resulta que ya tiene un hijo y no desea tener más, igual lo tiene su ex",
        "te dice que no quiere tener hijos, prefiere conservar su libertad",
        "comenta que sueña tener una familia, con uno o más hijos propios"
    ],
    [ # ["grueso", "delgado", "atlético", "musculoso"],
        "cuando te abraza sientes sus brazos y barriga mofeltudos como almohadas",
        "están en el rio y ves lo delgado que es, parece Jack Skellington",
        "salen a hacer ejercicio y ves que está en buena forma, aunque no se note",
        "en la piscina aprecias su musculatura, de verdad es muy disciplinado"
    ],
    [ # ["grunge", "casual", "moda",  "formal"],
        "parece no importarle el qué dirán, anda con ropas holgadas y rasgadas",
        "su ropa es muy casual, pantalón y camisa monotonos, le da igual la moda",
        "él usa la ropa más a la moda, con algo de un perfume que no huele mal",
        "ves que viste con un camibuso fino, muy formal y usa gel para el pelo"
    ],
    [ # ["joven", "joven-adulto", "adulto", "mayor"],
        "por su corta edad suele charlar cosas básicas de su vida como estudiante",
        "sentados charlando, los temas giran en torno a cómo vivir la vida adulta",
        "las charlas giran en torno a coquetearte y su día a día en el trabajo",
        "por ser un hombre mayor, te cuenta varias cosas de sus vivencias de antaño"
    ],
    [ # ["flácido", "brusco", "romántico", "muy erótico"], esto no va aqui
        "...", "...", "...", "..."
    ],
    [ # ["comunismo", "socialismo", "capitalismo", "libremercado"],
        "menciona que el edificio de allá debería ser expropiado por ser de ricos",
        "dice estar de acuerdo con las últimas protestas, en favor de los obreros",
        "van a un evento donde se oye hablar a empresarios, y él los admira",
        "él cree que mientras se tenga dinero, uno debería poder hacer lo que quiera"
    ],
    [ # ["ateístas", "espirituales", "hinduístas", "cristianas"],
        "llegando a temas religiosos, dice, naj que estúpido como la gente cree cosas",
        "de un momento a otro charlan sobre chakras y sueños, pero no de religión",
        "ves sus símbolos, y te dice que son de sus varios dioses Hindúes",
        "reafirma que Dios es lo más importante, intenta hablar de su iglesia"
    ],
    [ # ["el baile", "la música", "la literatura", "el dibujo"],
        "la salida es a una discoteca, él toma un poco y se pone a bailar a lo loco",
        "van a un restaurante karaoke, y se pone a cantar y tocar guitarra para tí",
        "se citan en un café, charlan filosóficamente sobre libros interesantes",
        "te lleva a un museo, luego saca su cuaderno y te dibuja a las afueras"
    ],
    [ # ["salvaje", "rural", "urbana", "futurista"],
        "te lleva a una montaña con río, es su lugar favorito, le gustaría vivir ahí",
        "están de paseo en un pueblito tradicional, el ambiente se siente relajante",
        "andan en un evento urbano de cultura, con noche de luces y gastronomía",
        "van a un pub con tecnología y gadgets de realidad virtual, muchos juegos"
    ],
    [ # ["negro", "indio", "mestizo", "blanco"], esto no va aqui
        "...", "...", "...", "..."
    ]
]

infotxtM = [
    ["indiferente", "huidiza", "resolutiva", "neurótica"],
    ["sensible", "comprensiva", "mentirosa", "maligna"],
    ["tímida", "seria", "charladora", "chistosa"],
    ["estricta", "conformista", "exploradora", "muy cambiante"],
    ["pobre", "trabajadora", "asalariada", "adinerada"],
    ["soltera", "comprometida", "con amante", "con crush"],
    ["ausente", "lejana", "conflictiva", "cercana"],
    ["quiere más", "ya tiene", "no quiere", "desea tener"],
    ["gruesa", "delgada", "atlética", "bellísima"],
    ["grunge", "casual", "moda",  "formal"],
    ["joven", "joven-adulta", "adulta", "mayor"],
    ["frígida", "insaciable", "romántica", "muy erótica"],
    ["comunismo", "socialismo", "capitalismo", "libremercado"],
    ["ateístas", "espirituales", "hinduístas", "cristianas"],
    ["el baile", "la música", "la literatura", "el dibujo"],
    ["salvaje", "rural", "urbana", "futurista"],
    ["negra", "india", "mestiza", "blanca"]
]

accionM = [
    [ # ["indiferente", "huidiza", "resolutiva", "neurótica"],
        "",
        "",
        "",
        ""
    ],
    [ # ["sensible", "comprensiva", "mentirosa", "maligna"],
        "ven una torcaza herida y ella no puede resistirse a atenderla, casi llora",
        "",
        "",
        ""
    ],
    [ # ["tímida", "seria", "charladora", "chistosa"],
        "",
        "",
        "",
        ""
    ],
    [ # ["estricta", "conformista", "exploradora", "muy cambiante"],
        "",
        "",
        "",
        ""
    ],
    [ # ["pobre", "trabajadora", "asalariada", "adinerada"],
        "",
        "",
        "",
        ""
    ],
    [ # ["soltera", "comprometida", "con amante", "con crush"],
        "",
        "",
        "",
        ""
    ],
    [ # ["ausente", "lejana", "conflictiva", "cercana"],
        "",
        "",
        "",
        ""
    ],
    [ # ["quiere más", "ya tiene", "no quiere", "desea tener"],
        "",
        "",
        "",
        ""
    ],
    [ # ["gruesa", "delgada", "atlética", "bellísima"],
        "",
        "",
        "",
        "están en la piscina y puedes apreciar sus curvas y senos, es perfecta"
    ],
    [ # ["grunge", "casual", "moda",  "formal"],
        "realmente no le importa el qué dirán, usa ropa holgada y desgarrada",
        "notas que es relajada para vestirse, usa pantalón y blusa monotonos",
        "ves que su vestimenta es cuidadosamente elegida, con accesorios y maquillaje",
        "ella viene vestida con un traje de manga larga muy bien aplanchado y fino"
    ],
    [ # ["joven", "joven-adulta", "adulta", "mayor"],
        "",
        "",
        "",
        ""
    ],
    [ # ["frígida", "insaciable", "romántica", "muy erótica"], esto no va aqui
        "...", "...", "...", "..."
    ],
    [ # ["comunismo", "socialismo", "capitalismo", "libremercado"],
        "",
        "",
        "",
        ""
    ],
    [ # ["ateístas", "espirituales", "hinduístas", "cristianas"],
        "",
        "",
        "",
        ""
    ],
    [ # ["el baile", "la música", "la literatura", "el dibujo"],
        "",
        "",
        "",
        ""
    ],
    [ # ["salvaje", "rural", "urbana", "futurista"],
        "",
        "",
        "",
        ""
    ],
    [ # ["negra", "india", "mestiza", "blanca"], esto no va aqui
        "...", "...", "...", "..."
    ]
]

nombresH = [
    "Aurelio", "Armando", "Andy", "Alexander", "Alejandro",
    "Ariel", "Adam", "Adolfo", "Alberto", "Antonio",
    "Boris", "Brandon", "Brayan", "Bruce", "Bart",
    "Carlos", "Camilo", "Christian", "Cesar", "Cory",
    "Cain", "Charly", "Chuck", "Conan", "Clark",
    "Daniel", "Dante", "Dario", "Denis", "Dustin",
    "Ernesto", "Esteban", "Erick", "Emilio", "Efrain",
    "Francisco", "Federico", "Fabio", "Fernando", "Felipe",
    "Gabriel", "Galvin", "German", "Gonzalo", "Gaston",
    "Hector", "Humberto", "Herbert", "Hugo", "Harry",
    "Ignacio", "Izidro", "Ismael", "Ivan", "Isaac",
    "Jose", "John", "Juan", "Jeremias", "Jean",
    "Kevin", "Kenner", "Kenny", "Klaus", "Karin",
    "Luis", "Leonardo", "Lucas", "Leandro", "Leo",
    "Mateo", "Mauricio", "Manuel", "Marcos", "Martin",
    "Michael", "Marino", "Matias", "Merlin", "Max",
    "Norman", "Nicolas", "Nestor", "Nelson", "Nacho",
    "Omar", "Oswaldo", "Oliver", "Orion", "Ovidio",
    "Pablo", "Paco", "Pancho", "Paul", "Pedro",
    "Ramon", "Remi", "Ragnar", "Ramiro", "Rafael",
    "Santiago", "Samuel", "Sebastian", "Stephen", "Salvador",
    "Tomas", "Tadeo", "Teodoro", "Teofilo", "Tulio",
    "Victor", "Vicente", "Vladimir", "Ventura", "Van",
    "Wilfredo", "William", "Waldo", "Wally", "Walter",
    "Xander", "Yael", "Zamir", "Querubin", "Ulises"
]

nombresM = [
    "Angy", "Angela", "Alejandra", "Amanda", "Andrea",
    "Ana", "Adriana", "Allison", "Aurora", "Agata",
    "Bonnie", "Bianca", "Barbara", "Bety", "Brenda",
    "Cony", "Camila", "Carolina", "Celeste", "Cindy",
    "Celia", "Catherine", "Cristina", "Coral", "Claudia",
    "Darian", "Diana", "Dafne", "Dora", "Delia",
    "Estefany", "Eliza", "Emily", "Elena", "Esmeralda",
    "Frida", "Florencia", "Fiona", "Fabiola", "Fatima",
    "Guisela", "Gema", "Gloria", "Gabriela", "Ginna",
    "Homura", "Helena", "Hilda", "Heidy", "Harley",
    "Ingrid", "Ines", "Isabella", "Irene", "Iris",
    "Jackie", "Jazmin", "Jade", "Jenny", "Jessica",
    "Karen", "Kimi", "Kala", "Keiko", "Kyoko",
    "Luisa", "Luz", "Luna", "Laura", "Lorena",
    "Maria", "Martha", "Maribel", "Melisa", "Marcela",
    "Marisol", "Melanie", "Miranda", "Monica", "Margarita",
    "Nora", "Nancy", "Nereida", "Natalia", "Nadia",
    "Olivia", "Olga", "Oriana", "Ofelia", "Ovidia",
    "Patricia", "Paula", "Paloma", "Paola", "Priscila",
    "Regina", "Rebeca", "Rocio", "Rosa", "Rubi",
    "Samanta", "Sara", "Susana", "Sonia", "Selina",
    "Tania", "Tamara", "Tatiana", "Teresa", "Trixie",
    "Victoria", "Valentina", "Valery", "Vanessa", "Vania",
    "Wanda", "Wendy", "Willow", "Winny", "Wynona",
    "Ximena", "Yolanda", "Zaira", "Quira", "Ursula"
]

apellidos = [
    "Acosta", "Aguilar", "Aguirre", "Alonso", "Andrade",
    "Báez", "Ballesteros", "Barrios", "Benítez", "Blanco",
    "Cabrera", "Calderón", "Campos", "Cano", "Carrillo",
    "Delgado", "Díaz", "Domínguez", "Duarte", "Durán",
    "Escalante", "Escobar", "Espinosa", "Estrada", "Echeverría",
    "Fernández", "Figueroa", "Flores", "Fonseca", "Franco",
    "Gálvez", "García", "Gil", "Gómez", "Guerrero",
    "Hernández", "Herrera", "Huerta", "Hurtado", "Huertas",
    "Ibáñez", "Iglesias", "Ibarra", "Izquierdo", "Islas",
    "Jáuregui", "Jiménez", "Juárez", "Jaramillo", "Jordán",
    "Lara", "León", "López", "Luján", "Lozano",
    "Maldonado", "Márquez", "Martínez", "Medina", "Molina",
    "Navarro", "Nieto", "Núñez", "Novoa", "Naranjo",
    "Olivares", "Orozco", "Ortega", "Ortiz", "Oviedo",
    "Pacheco", "Padilla", "Palma", "Pérez", "Ponce",
    "Quevedo", "Quintero", "Quiroga", "Quintana", "Quispe",
    "Ramírez", "Ramos", "Reyes", "Ríos", "Romero",
    "Salazar", "Salinas", "Sánchez", "Sandoval", "Soto",
    "Téllez", "Torres", "Trejo", "Trujillo", "Tovar",
    "Urbina", "Ureña", "Uribe", "Ulloa", "Urdiales",
    "Valdés", "Valencia", "Valenzuela", "Vásquez", "Vega",
    "King", "Walker", "Xu", "Yosa", "Werner",
    "Zambrano", "Zapata", "Zavala", "Zúñiga", "Zárate"
]

fichas = []
conocidos = []

class Ficha:

    def __init__(self):
        self.amistad = 0 # cantidad de citas que han tenido
        self.isFem = random.choice([True, False])
        if self.isFem:
            self.nombre = nombresM[random.randrange(len(nombresM))]
        else:
            self.nombre = nombresH[random.randrange(len(nombresH))]
        self.nombre += " " + apellidos[random.randrange(len(apellidos))]
        self.data = [] # como es el personaje
        self.gusto = [] # que le atrae al personaje
        self.disgusto = [] # que le disgusta al personaje
        self.califica = [] # puntaje dado por el jugador -1:noini, 0,0.5,1:likes
        self.opinion = [] # si ya le ha dicho al jugador lo que piensa, =califica
        for i in range(Atr.TOTAL):
            self.data.append(random.randint(0, 3))
            self.gusto.append(random.randint(0, 3))
            dis = random.randint(0, 3)
            while dis == self.gusto[-1]:
                dis = random.randint(0, 3)
            self.disgusto.append(dis)
            self.califica.append(-1.0)
            self.opinion.append(-1.0)
        self.orient = [True, True] # mujeres, hombres
        if random.random() < 0.75:
            if self.isFem:
                self.orient = [False, True]
            else:
                self.orient = [True, False]
        elif random.random() > 0.75:
            if self.isFem:
                self.orient = [True, False]
            else:
                self.orient = [False, True]
    
    def __str__(self):
        return self.vistazo() +\
            ", está " + self.dato(Atr.RELA) + "\nsu familia es " +\
            self.dato(Atr.FAMILY) + ", " + self.dato(Atr.HIJOS) + " hijos" +\
            "\nante situaciónes difíciles es " + self.dato(Atr.NEURA) +\
            "\notros dirán que es " + self.dato(Atr.EMPATIA) + " y " +\
            self.dato(Atr.APERT) + "\nusualmente " + self.dato(Atr.HOT) +\
            " durante el sexo, con\ninclinación política al " +\
            self.dato(Atr.POLI) + " e\nideas religiosas " + self.dato(Atr.RELI) +\
            ", su hobbie\nes " + self.dato(Atr.ARTE) + " y añora la vida " +\
            self.dato(Atr.ENTORNO)

    def getAnalisis(self, textIni=""):
        return self.vistazo(textIni) +\
            ", está " + self.datin(Atr.RELA) + "\nsu familia es " +\
            self.datin(Atr.FAMILY) + ", " + self.datin(Atr.HIJOS) + " hijos" +\
            "\nante situaciónes difíciles es " + self.datin(Atr.NEURA) +\
            "\notros dirán que es " + self.datin(Atr.EMPATIA) + " y " +\
            self.datin(Atr.APERT) + "\nusualmente " + self.datin(Atr.HOT) +\
            " durante el sexo, con\ninclinación política al " +\
            self.datin(Atr.POLI) + " e\nideas religiosas " + self.datin(Atr.RELI) +\
            ", su hobbie\nes " + self.datin(Atr.ARTE) + " y añora la vida " +\
            self.datin(Atr.ENTORNO)

    def vistazo(self, textIni=""):
        g = ["un ", " vestido de "]
        if self.isFem:
            g = ["una ", " vestida de "]
        ori = "het"
        if self.orient[0] and self.orient[1]:
            ori = "bi"
        elif self.isFem and self.orient[0]:
            ori = "hom"
        elif not self.isFem and self.orient[1]:
            ori = "hom"
        return textIni + self.nombre + " (" + ori + "):\n" +\
            g[0] + self.dato(Atr.ETNIA) + " " + self.dato(Atr.CUERPO) +\
            " " + self.dato(Atr.EDAD) + g[1] + self.dato(Atr.VESTIDO) +\
            "\nluce " + self.dato(Atr.EXTRO) + " y " + self.dato(Atr.DINERO)

    def dato(self, indice=Atr.ETNIA):
        v = self.data[indice]
        if self.isFem:
            return infotxtM[indice][v]
        else:
            return infotxtH[indice][v]
    
    def datin(self, indice=Atr.ETNIA):
        if self.califica[indice] != -1:
            v = self.data[indice]
            if self.isFem:
                return infotxtM[indice][v]
            else:
                return infotxtH[indice][v]
        return "??????"
    
    def existe(self, fichas=[]):
        for f in range(len(fichas)):
            if fichas[f].nombre == self.nombre:
                return f
        return -1
    
    def getLike(self, otro=None):
        # retorna 0:disgusto 0.5:normal 1:gusto
        pts = 0.0
        for i in range(Atr.TOTAL):
            if self.gusto[i] == otro.data[i]:
                pts += 1.0
            elif self.disgusto[i] != otro.data[i]:
                pts += 0.5
        return pts / Atr.TOTAL

    def getAfinidad(self, otro=None):
        # retorna 0:disgusto 0.5:normal 1:gusto
        pts = 0.0
        tot = 0.0
        for i in range(Atr.TOTAL):
            if self.opinion[i] != -1:
                pts += self.opinion[i]
                tot += 1.0
            if self.califica[i] != -1:
                pts += self.califica[i]
                tot += 1.0
        return pts / max(1, tot)

    def cuestionario(self):
        print("a continuación crearás un personaje:")
        self.isFem = getValor("género: 1.Mujer - 2.Hombre", 2) == 0
        ddt = infotxtH
        if self.isFem:
            ddt = infotxtM
        n1 = ""
        while n1 == "":
            n1 = input("   un nombre: ").replace(" ", "")
        n1 = n1[0].upper() + n1[1:].lower()
        n2 = ""
        while n2 == "":
            n2 = input("   un apellido: ").replace(" ", "")
        n2 = n2[0].upper() + n2[1:].lower()
        self.nombre = n1 + " " + n2
        self.orient[0] = getValor("le gustan las mujeres: 1.Si - 2.No", 2) == 0
        self.orient[1] = getValor("le gustan los hombres: 1.Si - 2.No", 2) == 0
        self.data[Atr.ETNIA] = getQuest("etnia o color de piel", ddt, Atr.ETNIA)
        self.data[Atr.CUERPO] = getQuest("tipo de cuerpo", ddt, Atr.CUERPO)
        self.data[Atr.EDAD] = getQuest("edad o etapa de vida", ddt, Atr.EDAD)
        self.data[Atr.VESTIDO] = getQuest("estilo de vestimenta", ddt, Atr.VESTIDO)
        self.data[Atr.EXTRO] = getQuest("nivel de extroversión", ddt, Atr.EXTRO)
        self.data[Atr.DINERO] = getQuest("situación económica", ddt, Atr.DINERO)
        self.data[Atr.RELA] = getQuest("situación amorosa", ddt, Atr.RELA)
        self.data[Atr.FAMILY] = getQuest("cómo es su familia", ddt, Atr.FAMILY)
        self.data[Atr.HIJOS] = getQuest("respecto a los hijos", ddt, Atr.HIJOS)
        self.data[Atr.NEURA] = getQuest("ante situaciónes difíciles", ddt, Atr.NEURA)
        self.data[Atr.EMPATIA] = getQuest("cómo es la empatía y ética", ddt, Atr.EMPATIA)
        self.data[Atr.APERT] = getQuest("apertura a la experiencia", ddt, Atr.APERT)
        self.data[Atr.HOT] = getQuest("durante el sexo suele ser", ddt, Atr.HOT)
        self.data[Atr.POLI] = getQuest("idelogía política más afín", ddt, Atr.POLI)
        self.data[Atr.RELI] = getQuest("ideología religiosa más afín", ddt, Atr.RELI)
        self.data[Atr.ARTE] = getQuest("cuál hobbie le gusta más", ddt, Atr.ARTE)
        self.data[Atr.ENTORNO] = getQuest("qué estilo de vida preferiría", ddt, Atr.ENTORNO)

    def isOkOrient(self, otro=None):
        this = 0 if self.isFem else 1
        utr = 0 if otro.isFem else 1
        return self.orient[utr] and otro.orient[this]

    def isPrimeraVista(self, otro=None):
        if self.isOkOrient(otro):
            pp = [True, False, False, False, False]
            random.shuffle(pp)
            n = 0
            for atr in [Atr.CUERPO, Atr.EDAD, Atr.VESTIDO, Atr.EXTRO, Atr.DINERO]:
                if pp[n]:
                    otro.gusto[atr] = self.data[atr]
                    dis = random.randint(0, 3)
                    while dis == otro.gusto[atr]:
                        dis = random.randint(0, 3)
                    otro.disgusto[atr] = dis
                n += 1
            otro.gusto[Atr.ETNIA] = self.data[Atr.ETNIA]
            dis = random.randint(0, 3)
            while dis == otro.gusto[Atr.ETNIA]:
                dis = random.randint(0, 3)
            otro.disgusto[Atr.ETNIA] = dis
            otro.califica[Atr.ETNIA] = 1.0
            otro.opinion[Atr.ETNIA] = 1.0
            return True
        return False

    def getIndCalificable(self):
        ind = []
        for i in range(Atr.TOTAL):
            if i == Atr.HOT:
                continue
            if self.califica[i] == -1:
                ind.append(i)
        if len(ind) == 0:
            return -1
        return random.choice(ind)
    
    def getIndOpinable(self):
        ind = []
        for i in range(Atr.TOTAL):
            if i == Atr.HOT:
                continue
            if self.opinion[i] == -1:
                ind.append(i)
        if len(ind) == 0:
            return -1
        return random.choice(ind)

def getQuest(question="", infotxt=[], indice=Atr.ETNIA):
    if question != "":
        print("   " + question)
    for i in range(4):
        print("   " + str(i + 1) + ". " + infotxt[indice][i])
    return getValor()

def getValor(question="", limite=4, allowVoid=False):
    # 0,1,2,3 para limite 4
    v = 0
    if question != "":
        print("   " + question)
    while True:
        try:
            v = input("-> ")
            if allowVoid and v == "":
                return -1
            v = int(v)
            if v < 1 or v > limite:
                continue
        except:
            continue
        break
    return v - 1

def testUno():
    global fichas
    nuevaFicha()
    print("")
    fichas[-1].cuestionario()
    print("")
    print(str(fichas[-1]))

def testAll():
    global fichas
    print("\npulsa Enter, digita algo para salir...")
    while True:
        if input("") != "":
            break
        nuevaFicha()
        print(str(fichas[-1]))
    printMatch(fichas) 

def printMatch(fichas=[]):
    ubest = 0.0
    quienes = [None, None]
    for f in range(len(fichas)):
        best = 0.0
        quien = None
        for i in range(len(fichas)):
            if i == f:
                continue
            if fichas[f].isFem == fichas[i].isFem:
                continue
            like = fichas[f].getLike(fichas[i])
            if like > best:
                best = like
                quien = fichas[i]
        if quien == None:
            print(fichas[f].nombre + "...")
        else:
            olike = quien.getLike(fichas[f])
            print(fichas[f].nombre + " > " + quien.nombre +
                " (" + str(int(best * 100.0)) + "% > " +
                str(int(olike * 100.0)) + "%)")
            dlike = (like + olike) / 2.0
            if dlike > ubest:
                ubest = dlike
                quienes = [fichas[f], quien]
    if quienes[0] != None:
        print("*** " + quienes[0].nombre + " + " + quienes[1].nombre +
            " (" + str(int(ubest * 100.0)) + "%) ***")

def nuevaFicha():
    global fichas
    ficha = Ficha()
    while ficha.existe(fichas) != -1:
        ficha = Ficha()
    fichas.append(ficha)
    return ficha

def juego():
    global fichas
    print("\n*** Juego de Citas Loquillo - Omwekiatl ***\n")
    print("¿deseas jugar con un personaje aleatorio?")
    while True:
        prs = input("(1.Mujer, 2.Hombre, 3.Personalizado): ")
        if prs in ["1", "2", "3"]:
            print("")
            if prs == "1":
                ficha = Ficha()
                while not ficha.isFem:
                    ficha = Ficha()
                fichas.append(ficha)
            elif prs == "2":
                ficha = Ficha()
                while ficha.isFem:
                    ficha = Ficha()
                fichas.append(ficha)
            else:
                nuevaFicha()
                fichas[-1].cuestionario()
                print("")
            print(str(fichas[-1]))
            break
    print("")
    dias = 40
    print("tienes " + str(dias) + " días para hallar una pareja adecuada!!!")
    menu(dias)

def menu(limiteDias=32):
    dia = 1
    while dia <= limiteDias:
        print("\nDía: " + str(dia))
        print("1. conocer gente")
        print("2. salir con contacto")
        print("3. proponer a contacto")
        print("4. analizar contactos")
        sel = ""
        while sel == "":
            sel = input("-> ")
            if sel in ["1", "2", "3", "4"]:
                break
            sel = ""
        if sel == "1":
            conocer()
        elif sel == "2":
            salir()
        elif sel == "3":
            proponer()
        elif sel == "4":
            analizar()
        dia += 1

def conocer():
    global fichas, conocidos
    candis = []
    for i in range(random.randint(0, 3)):
        can = nuevaFicha()
        while not fichas[0].isPrimeraVista(can):
            can = nuevaFicha()
        candis.append(can)
    if len(candis) == 0:
        print("   hoy no encontraste a nadie...")
    else:
        tot = len(candis)
        print("   en el lugar hay " + str(tot) + " personas interesadas")
        print("   ...")
        for c in range(tot):
            print(candis[c].vistazo("   " + str(c + 1) + ". "))
            print("   ...")
        v = getValor("¿a quién quieres contactar? (vacío si a nadie)", tot, True)
        if v != -1:
            conocidos.append(candis[v])
            print("   ahora tienes el teléfono de " + conocidos[-1].nombre)
        else:
            print("   has ignorado a todo mundo...")

def salir():
    global conocidos
    print("   ¿a quién deseas invitar?")
    for i in range(len(conocidos)):
        otro = conocidos[i]
        print("   " + str(i + 1) + ". " + otro.nombre + " (" +
            str(otro.amistad) + " - " + str(int(otro.getAfinidad() * 100.0)) + "%)")
    v = getValor("", len(conocidos))
    otro = conocidos[v]
    otro.amistad += 1
    print("...\n   la cita con " + otro.nombre + " transcurre\n...")
    if random.random() < 0.5:
        hablar(otro)
        escuchar(otro)
    else:
        escuchar(otro)
        hablar(otro)

def hablar(otro=None):
    global fichas
    ind = otro.getIndOpinable()
    if ind != -1:
        sel = fichas[0].data[ind]
        if otro.gusto[ind] == sel:
            otro.opinion[ind] = 1.0
            print("   Si le gusta " + gustotxt[ind][sel])
            print("...")
        elif otro.disgusto[ind] == fichas[0].data[ind]:
            otro.opinion[ind] = 0.0
            print("   No le gusta " + gustotxt[ind][sel])
            print("...")
        else:
            otro.opinion[ind] = 0.5

def escuchar(otro=None):
    global fichas
    le = "él"
    if otro.isFem:
        le = "ella"
    ind = otro.getIndCalificable()
    if ind == -1:
        print("   escuchandle te das cuenta que ya sabes todo sobre " + le)
    else:
        act = accionH
        if otro.isFem:
            act = accionM
        print("   " + act[ind][otro.data[ind]])
        v = getValor("¿qué opinas de esto? (1.disgusto 2.neutral 3.gusto):", 3)
        otro.califica[ind] = v / 2.0
        if v == 2:
            fichas[0].gusto[ind] = otro.data[ind]
            print("   vaya, tu gusto hacia " + le + " va en aumento")
        elif v == 0:
            fichas[0].disgusto[ind] = otro.data[ind]
            print("   parece que esta interacción con " + le + " fué incómoda")
    print("...")

def proponer():
    pass

def analizar():
    global conocidos
    tot = len(conocidos)
    print("   tienes " + str(tot) + " contactos:")
    for i in range(tot):
        print("...")
        print(conocidos[i].getAnalisis("   " + str(i + 1) + ". "))

def main():
    #testUno()
    #testAll()
    juego()

main()

"""
TAREAS:
- terminar escritos de modo accion / escuchar
- hacer sistema de modo hablar con opinión de otro
- hacer que algunas combinaciones como rico comunista sean poco probables
"""
