import socket
import time

SOCK_BUFFER = 1024


if __name__ == '__main__':
    nums = list()
    for _ in range(20):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ("localhost", 5000)

        print(f"[*] Conectando a servidor en {server_address[0]}:{server_address[1]}")

        sock.connect(server_address)
    
        msg = "Hola mundo!"

        print(f"[*] A punto de enviar {msg}")
        sock.sendall(msg.encode("utf-8"))

        data = sock.recv(SOCK_BUFFER)
        print(f"[!] Recibi {data}")
        nums.append(int(data.decode("utf-8")))
        time.sleep(1)

        print(f"[*] terminando operacion, cerrando el socket")
        sock.close()
