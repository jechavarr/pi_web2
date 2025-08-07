# Lista para almacenar los numeros ingresados por el usuario
numeros = []

# Mensaje inicial al usuario
print(" Ingresa numeros enteros. Escribe 0 para terminar.\n")

# Ciclo while infinito para seguir pidiendo numeros hasta que el usuario escriba 0
while True:
    try:
        # Solicitamos un numero al usuario
        num = int(input("Ingresa un numero: "))

        # Si el usuario ingresa 0, se termina el ciclo
        if num == 0:
            break
        
        # Si no es 0, se agrega el numero a la lista
        numeros.append(num)

    # Si el usuario ingresa algo que no es un numero entero, se muestra un mensaje de error
    except ValueError:
        print(" Entrada invalida. Ingresa solo numeros enteros.")

# Despues del ciclo, verificamos si se ingresaron numeros
if not numeros:
    # Si la lista esta vacia, no se hace el análisis
    print("\n No se ingresaron numeros.")
else:
    # Inicializamos las variables para el analisis
    pares = 0       # Contador de numeros pares
    impares = 0     # Contador de numeros impares
    suma = 0        # Acumulador para calcular el promedio
    mayor = numeros[0]  # Inicializamos con el primer numero de la lista
    menor = numeros[0]  # Igual que el mayor

    # Recorremos la lista de numeros para analizarlos
    for n in numeros:
        # Contamos pares e impares usando el operador modulo
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1

        # Sumamos cada numero a la variable 'suma'
        suma += n

        # Verificamos si el numero actual es mayor o menor que los guardados
        if n > mayor:
            mayor = n
        if n < menor:
            menor = n

    # Una vez terminado el analisis, mostramos los resultados
    print("\n Resultados:")
    print(f" Total de numeros ingresados: {len(numeros)}")
    print(f" Numeros pares: {pares}")
    print(f" Numeros impares: {impares}")
    print(f" Numero mayor: {mayor}")
    print(f" Numero menor: {menor}")
    print(f" Promedio: {suma / len(numeros):.2f}")  # Se calcula el promedio
