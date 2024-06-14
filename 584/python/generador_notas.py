from random import randint


if __name__ == '__main__':
    codigo_base = 20240001
    contenido = f"codigo,{','.join(f'lab{idx + 1}' for idx in range(7))},e1,e2\n"

    for i in range(200):
        fila = f"{codigo_base + i},{','.join(f'{randint(0,20)}' for _ in range(9))}\n"
        contenido += fila

    contenido = contenido[:-1]

    with open("notas.csv", "w") as f:
        f.write(contenido)
