import random
from datetime import datetime, timedelta
from usuario import Usuario
from producto import Producto
from db_sql import Conector

# configuracion del sistema
total_usuarios = 1000 # recomendable 1000+
year_ini = 2023 # year para iniciar el sistema
month_ini = 1 # mes para iniciar el sistema, 1 es enero
password = "$2y$10$gl68EE0OBsVO8JX.r9k/Tu2BDUWj3qqirrd9L6f0w5N8rKbErqsKS" # 123456
prob_tener_link = 0.15 # para que compartan su link a redes sociales
prob_notifi = 0.25 # recibir correos, notifi push y usar datos
prob_descripcion = 0.666 # prob de tener una descripcion en el perfil
prob_superdescripcion = 0.333 # prob que la descripcion sea larga
prob_troll = 1 / 5 # acciones troll: chat, producto, perfil, pqrs, denuncia
prob_lacra = 1 / 3 # acciones lacra: chat, producto, perfil
tipo_usr_porc = { # probabilidad existir, deben sumar 100%
    "master": 0,
    "admin": 0.01,
    "comprador": 0.4,
    "curioso": 0.3,
    "lacra": 0.04,
    "troll": 0.08,
    "vendeuno": 0.07,
    "vendeall": 0.1
}
tipo_usr_vende = { # probabilidad vender algo
    "master": 0,
    "admin": 0,
    "comprador": 0.03,
    "curioso": 0.01,
    "lacra": 0.05,
    "troll": 0.1,
    "vendeuno": 0.05,
    "vendeall": 0.2
}
tipo_usr_compra = { # probabilidad comprar algo
    "master": 0,
    "admin": 0,
    "comprador": 0.2,
    "curioso": 0.01,
    "lacra": 0.01,
    "troll": 0.01,
    "vendeuno": 0.05,
    "vendeall": 0.03
}
tipo_usr_ver = { # probabilidad ver algo
    "master": 0.01,
    "admin": 0.05,
    "comprador": 0.15,
    "curioso": 0.25,
    "lacra": 0.05,
    "troll": 0.2,
    "vendeuno": 0.1,
    "vendeall": 0.03
}
tipo_usr_chatok = { # probabilidad la compra salga bien
    "master": 0,
    "admin": 0,
    "comprador": 0.07,
    "curioso": 0.15,
    "lacra": 0.03,
    "troll": 0.01,
    "vendeuno": 0.1,
    "vendeall": 0.2
}

# estructuras para los agentes
usuarios = []
productos = []

def limpiar_db():
    Conector.run_sql("DELETE FROM `favoritos`")
    Conector.run_sql("DELETE FROM `bloqueados`")
    Conector.run_sql("DELETE FROM `vistos`")
    Conector.run_sql("DELETE FROM `auditorias`")
    Conector.run_sql("DELETE FROM `notificaciones`")
    Conector.run_sql("DELETE FROM `pqrs`")
    Conector.run_sql("DELETE FROM `denuncias`")
    Conector.run_sql("DELETE FROM `mensajes`")
    Conector.run_sql("DELETE FROM `chats`")
    Conector.run_sql("DELETE FROM `productos`")
    Conector.run_sql("DELETE FROM `usuarios`")
    Conector.run_sql("DELETE FROM `correos`")

# crear a los usuarios
def crear_usuarios():
    global usuarios, total_usuarios, year_ini, month_ini, password, prob_tener_link, prob_notifi, tipo_usr_porc, prob_descripcion, prob_superdescripcion, prob_troll, prob_lacra

    ini_dt = datetime(year_ini, month_ini, 1, 0, 0, 0).timestamp()
    fin_dt = datetime.now().timestamp()
    fecha = datetime.fromtimestamp(ini_dt).strftime("%Y-%m-%d %H:%M:%S")
    usuarios.append(Usuario("master@sena", password, "1", False, fecha,
        True, True, True, 0, "master", prob_troll, prob_lacra))
    for i in range(total_usuarios):
        r = pow(random.random(), 3)
        dt = ini_dt + r * (fin_dt - ini_dt)
        fecha = datetime.fromtimestamp(dt).strftime("%Y-%m-%d %H:%M:%S")
        rol = "2" if random.random() < tipo_usr_porc["admin"] else "3"
        correo = "usr" + str(i) + "@sena"
        con_link = random.random() < prob_tener_link if rol == "3" else False
        noti_correo = random.random() < prob_notifi if rol == "3" else True
        noti_push = random.random() < prob_notifi if rol == "3" else True
        uso_datos = random.random() < prob_notifi if rol == "3" else True
        lvl_descripcion = (2 if random.random() < prob_superdescripcion else 1) if random.random() < prob_descripcion else 0
        lvl_descripcion = lvl_descripcion if rol == "3" else 0
        if rol == "2":
            tipo = "admin"
        else:
            r = random.random() * (1 - tipo_usr_porc["admin"])
            if r < tipo_usr_porc["vendeall"]:
                tipo = "vendeall"
            elif r < tipo_usr_porc["vendeall"] + tipo_usr_porc["vendeuno"]:
                tipo = "vendeuno"
            elif r < tipo_usr_porc["vendeall"] + tipo_usr_porc["vendeuno"] +\
                    tipo_usr_porc["troll"]:
                tipo = "troll"
            elif r < tipo_usr_porc["vendeall"] + tipo_usr_porc["vendeuno"] +\
                    tipo_usr_porc["troll"] + tipo_usr_porc["lacra"]:
                tipo = "lacra"
            elif r < tipo_usr_porc["vendeall"] + tipo_usr_porc["vendeuno"] +\
                    tipo_usr_porc["troll"] + tipo_usr_porc["lacra"] +\
                    tipo_usr_porc["curioso"]:
                tipo = "curioso"
            else:
                tipo = "comprador"
        usuarios.append(Usuario(correo, password, rol, con_link, fecha,
            noti_correo, noti_push, uso_datos, lvl_descripcion, tipo, prob_troll, prob_lacra))

def crear_productos():
    pass

def ver_productos():
    pass

def generar_chats():
    pass

def generar_fav_bloq():
    pass

def eliminar_productos():
    pass

def generar_pqrs_resp():
    pass

def generar_denuncias_resp():
    pass

def abandonar_usuarios():
    pass

def main():
    print("***Sist Poblador DB TuMercadoSena***")
    print("limpiando DB")
    limpiar_db()
    print("creando usuarios")
    crear_usuarios()
    print("creando productos")
    crear_productos()
    print("viendo productos")
    ver_productos()
    print("generando chats")
    generar_chats()
    print("generando fav bloq")
    generar_fav_bloq()
    print("eliminando productos")
    eliminar_productos()
    print("generando pqrs resp")
    generar_pqrs_resp()
    print("generando denuncias resp")
    generar_denuncias_resp()
    print("abandonando usuarios")
    abandonar_usuarios()
    print("***finalizado***")

main()
