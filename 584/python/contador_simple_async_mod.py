import asyncio
import time


async def count():
    print("Uno")
    time.sleep(1)
    print("Dos")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == '__main__':
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {(fin - inicio):0.6f} segundos")
