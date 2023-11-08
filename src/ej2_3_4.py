"""
Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
"""
def pedirNumero(msj: str):
    entrada = input(msj)
    num = int(entrada)
    return num

def main():
    try:
        num = pedirNumero("Introduzaca su edad: ")
    except ValueError:
        print("La entrada no es correcta." )
if __name__ == "__main__":
    main()
