from random import randint
import socket

SOCKET_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.0.0.0", 5000)

    print(f"[*] Levantando servidor en direccion {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)

    sock.listen(1)

    while True:
        print("[*] Esperando conexiones...")

        conn, client_address = sock.accept()
        
        print(f"Conexion establecida en {client_address[0]}:{client_address[1]}")

        try:
            while True:
                dato = conn.recv(SOCKET_BUFFER)

                if dato:
                    print(f"[!] Recibi: {dato}")
                    numero_aleatorio = f"{randint(1, 20)}"
                    conn.sendall(numero_aleatorio.encode("utf-8"))
                else:
                    print("[*] No hay mas datos de parte del cliente")
                    break
        except ConnectionResetError:
            print("[!] Cliente cerro la conexion de manera abrupta")
        finally:
            print("[*] Cerrando la conexion")
            conn.close()
