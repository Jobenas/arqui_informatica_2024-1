import time


def count():
    print("Uno")
    time.sleep(1)
    print("Dos")


def main():
    for _ in range(3):
        count()


if __name__ == '__main__':
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {(fin - inicio):0.6f}")
