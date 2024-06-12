from random import randint
import time


if __name__ == '__main__':
    M = 1000 # filas
    N = 1000 # columnas

    matrix = [[randint(0, 100) for _ in range(N)] for _ in range(M)] # escribiendo en orden row-major

    print("[*] Matriz creada")

    print("[*] Empezando a leer la matriz en orden column-major")

    col_major_inicio = time.perf_counter()
    for j in range(N):
        for i in range(M):
            a = matrix[i][j]
    col_major_fin = time.perf_counter()

    print("[*] Empezando a leer la matriz en orden row-major")

    row_major_inicio = time.perf_counter()
    for i in range(M):
        for j in range(N):
            a = matrix[i][j]
    row_major_fin = time.perf_counter()

    print(f"[!] Tiempo que tomó leer la matriz en orden col-major: {col_major_fin - col_major_inicio} segundos")
    print(f"[!] Tiempo que tomó leer la matriz en orden row-major: {row_major_fin - row_major_inicio} segundos")

