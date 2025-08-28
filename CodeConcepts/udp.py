import socket
import threading

# configuracion del puerto de escucha
UDP_RECV_PORT = 29567

# configuracion del destino de los mensajes enviados
UDP_SEND_IP = "127.0.0.1"
UDP_SEND_PORT = 4749

# crear el socket UDP que enviara y recibira los mensajes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", UDP_RECV_PORT))
print("sistema inicializado...")

# funcion para recibir mensajes
def recibir_mensajes():
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print("")
            print("de: " + addr)
            print("msj: " + str(data))
        except:
            pass

# crear e iniciar el hilo para recibir mensajes
hilo_recibir = threading.Thread(target=recibir_mensajes, daemon=True)
hilo_recibir.start()

# funcion para enviar mensajes
def enviar_mensaje(mensaje):
    try:
        sock.sendto(mensaje.encode(), (UDP_SEND_IP, UDP_SEND_PORT))
        print("enviado...")
    except:
        pass

# enviar mensajes continuamente
while True:
    mensaje = input("escriba su mensaje: ")
    if mensaje == "":
        break
    enviar_mensaje(mensaje)

# cerrar el socket antes de salir
sock.close()
print("sistema finalizado...")
