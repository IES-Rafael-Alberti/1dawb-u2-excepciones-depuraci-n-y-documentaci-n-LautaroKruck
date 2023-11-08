"""
El algoritmo burbuja
El algoritmo burbuja te permite ordenar valores de un array. Funciona revisando cada elemento con el elemanto adyacente. Si ambos elementos no están ordenados, se procede a intercambiarlos, si por el contrario los elementos ya estaban ordenados se dejan tal como estaban. Este proceso sigue para cada elemento del arreglo hasta que quede completamente ordenado.
"""

a = [8, 3, 1, 19, 14]

n = 1
for i in range (1,len(a)):
    n += 1
    for j in range (0, len(a)-n):
        a