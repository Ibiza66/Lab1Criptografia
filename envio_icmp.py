from scapy.all import IP, ICMP, send
import time

def enviar_mensaje_icmp(destino, mensaje):
    print(f"Enviando mensaje: {mensaje}")

    for i, caracter in enumerate(mensaje):
        paquete = IP(dst=destino)/ICMP(id=1234, seq=i)/caracter
        send(paquete, verbose=0)

        print(f"Enviado: '{caracter}' (seq={i})")

        time.sleep(0.5)  # para simular ping real

if __name__ == "__main__":
    destino = input("IP destino: ")
    mensaje = input("Mensaje a enviar: ")

    enviar_mensaje_icmp(destino, mensaje)
