"""

El algoritmo burbuja

El algoritmo burbuja te permite ordenar valores de un array. Funciona revisando cada elemento con el elemanto adyacente. Si ambos elementos no están ordenados, se procede a intercambiarlos, si por el contrario los elementos ya estaban ordenados se dejan tal como estaban. Este proceso sigue para cada elemento del arreglo hasta que quede completamente ordenado.

"""
def pedirNum():
    """Función que solicita una serie de números al usuario."""
    numeros_str = input("Ingresa una serie de números separados por espacio: ")
    numeros = [int(num) for num in numeros_str.split()]
    return numeros

def guardar_en_lista():
    """Función que utiliza pedir_numeros y almacena los números en una lista."""
    lista_numeros = pedir_numeros()
    return lista_numeros

def ordenarSerie(lista_numeros):
    n = len(a)

    for i in range(n):
        # Últimos i elementos ya están ordenados, así que no necesitamos revisarlos
        for j in range(0, n-i-1):
            # Si el elemento actual es mayor que el siguiente, intercambiamos
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return lista_numeros

print("Array ordenado:")
print(lista_numeros)

def main():
    a

if __name__ == "__main__":
    main()