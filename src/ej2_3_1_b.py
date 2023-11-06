"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

def mostrarSerie(edad: int):
    serie = ""
    for i in range(1, edad ):
        serie += str(i) + ", "
    serie += str(edad)

    return serie


def pedirEdad(msj: str):
    entrada = input(msj)
    
    edad = int(entrada)
    
    if edad <= 0:
        raise Exception("Introduzca una edad válida. ")
    
    return edad


def main():
    
    error = True
    while error:
        try:
            edad = pedirEdad("Introduzaca su edad: ")
            error = False
        except ValueError:
            print("***ERROR***  edad no válida.")
        except Exception:
            print("***ERROR***  edad negativa o cero.")
    
    print (mostrarSerie(edad))

if __name__ == "__main__":
    main()
