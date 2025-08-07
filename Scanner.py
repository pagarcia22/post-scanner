import socket

def escanear(ip):
    print(f"Escaneando {ip}...")
    for puerto in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        resultado = sock.connect_ex((ip, puerto))
        if resultado == 0:
            try:
                servicio = socket.getservbyport(puerto)
            except:
                servicio = "Desconocido"
            print(f"Puerto {puerto} abierto ({servicio})")
        sock.close()

if __name__ == "__main__":
    objetivo = input("IP a escanear: ")
    escanear(objetivo)

        