import time


if __name__ == '__main__':
    inicio_cpu = time.perf_counter()
    a = 4
    b = 5
    c = a + b
    fin_cpu = time.perf_counter()

    inicio_es = time.perf_counter()
    print(f"El resultado de la operacion es {c}")
    fin_es = time.perf_counter()

    print(f"Tiempo de CPU\t-->\t{fin_cpu - inicio_cpu} segundos\nTiempo de E/S\t-->\t{fin_es - inicio_es} segundos")
