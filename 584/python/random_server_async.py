import asyncio
from random import randint
import socket

SOCK_BUFFER = 1024


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    print("[!] Cliente conectado")
    while True:
        msg_bytes = await reader.read(SOCK_BUFFER)
        print(f"[*] Recibi: {msg_bytes}")
        if msg_bytes:
            await writer.write(f"{randint(1, 20)}".encode("utf-8"))
            await writer.drain()
        else:
            print("[*] No hay mas mensajes del cliente")
            break

    writer.close() 
    await writer.wait_closed()
    print("conexion cerrada")


async def main():
    server_address = ("0.0.0.0", 5000)

    server = await asyncio.start_server(handle_client, server_address[0], server_address[1])

    async with server:
        print("[*] Empezando servidor")
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
