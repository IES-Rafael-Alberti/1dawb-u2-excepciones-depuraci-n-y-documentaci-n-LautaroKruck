"""

El algoritmo burbuja

El algoritmo burbuja te permite ordenar valores de un array. Funciona revisando cada elemento con el elemanto adyacente. Si ambos elementos no están ordenados, se procede a intercambiarlos, si por el contrario los elementos ya estaban ordenados se dejan tal como estaban. Este proceso sigue para cada elemento del arreglo hasta que quede completamente ordenado.

"""
def pedir_num():

    numeros_str = input("Ingresa una serie de números separados por espacio: ")
    numeros = [int(num) for num in numeros_str.split()]
    return numeros

def guardar_en_lista(numeros):

    listaNum = numeros
    return listaNum

def ordenar_serie(listaNum):
    
    n = len(listaNum)
    for i in range(n):

        for j in range(0, n-i-1):
            if listaNum[j] > listaNum[j+1]:
                listaNum[j], listaNum[j+1] = listaNum[j+1], listaNum[j]
    listaOrdenada = listaNum 
    
    return listaOrdenada

def main():
    numeros = pedir_num()
    listaNum = guardar_en_lista(numeros)
    listaOrdenada = ordenar_serie(listaNum)
    print("Lista ordenada:")
    print(listaOrdenada)

if __name__ == "__main__":
    main()