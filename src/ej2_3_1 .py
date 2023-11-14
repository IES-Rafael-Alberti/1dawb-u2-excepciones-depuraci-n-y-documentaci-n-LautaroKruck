"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""


def mostrarSerie(edad: int):
    serie = ""
    for i in range(1, edad + 1):
        serie += str(i) + ", "

    return serie


def pedirEdad(msj: str):
    error = True
    while error:
        try:
            edad = int(input(msj))
            error = False
        except:
            print("###ERROR###  edad no válida.")
        
    return edad


def main():

    edad = pedirEdad("Introduce su edad: ")
    print (mostrarSerie(edad))


if __name__ == "__main__":
    main()
