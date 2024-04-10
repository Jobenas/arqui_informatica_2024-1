print("Va a ingresar 5 numeros para ser promediados")
numeros = list()

for i in range(5):
    input_flag = False
    while not input_flag:
        try:
            n = input("Ingrese un numero: ")
            n_int = int(n)
            input_flag = True
        except ValueError:
            print("hubo un error, intentelo de nuevo")
    numeros.append(n_int)

suma = 0

for num in numeros:
    suma += num

suma = suma / len(numeros)

print(f"Promedio: {suma}, la lista usada fue {numeros}")