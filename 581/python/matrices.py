from random import randint
import time


if __name__ == '__main__':
    M = 2000  # filas
    N = 2000  # columnas

    matriz = []

    print("Escribiendo la matriz en orden row-major")
    for i in range(M): # iterando en filas
        fila = []
        for j in range(N): # iterando en columnas
            fila.append(randint(0, 100))
        matriz.append(fila)

    print("Leyendo en orden col-major")
    col_major_inicio = time.perf_counter()
    for j in range(N):
        for i in range(M):
            a = matriz[i][j]
    col_major_fin = time.perf_counter()

    print("Leyendo en orden row-major")
    row_major_inicio = time.perf_counter()
    for i in range(M):
        for j in range(N):
            a = matriz[i][j]
    row_major_fin = time.perf_counter()

    print(f"Orden Col-Major toma {col_major_fin - col_major_inicio} segundos")
    print(f"Orden Row-Major toma {row_major_fin - row_major_inicio} segundos")