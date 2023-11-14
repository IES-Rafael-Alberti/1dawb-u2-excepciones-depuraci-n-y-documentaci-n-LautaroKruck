"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
def pedirNumero(msj: str) -> int:
    num = None
    try:
        num = int(input(msj))
        if num <= 0:
            raise Exception("Numero negativo o cero. ")
    except ValueError:
        print("**Error** Número introducido no válido")
    except Exception:
        print("**Error** Número introducido no positivo o cero.")
    return num


def serieNum(num):
    serie = ""
    cont = 1
    while cont <= num:
        serie += str(cont) + " , "
        cont += 2
    return serie[:-3]


def main():
    num = pedirNumero("Introduzca un número: ")
    
    if num != None:
        res = serieNum(num)
        if res != "":
            print(res)
        else:
            print("No hay números impares en el rango.")

if __name__ == "__main__":
    main()