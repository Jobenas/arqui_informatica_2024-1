import time


if __name__ == '__main__':
    inicio = time.perf_counter()
    print("Este es un print de prueba")
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion: {(fin - inicio):0.6f} segundos")
