"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.
"""

def pedirNumero(msj: str) -> int:
    num = int(input(msj))
    
    if num <= 0:
        raise Exception("**Error** Número introducido no válido") 
    
    return num


def serieNum(num):
    serie = ""
    cont = num
    while cont >= 0:
        serie += str(cont) + ", "
        cont -= 1
    return serie[:-2]


def main():
    
    error = True
    while error:
        try:
            num = pedirNumero("Introduzca un número: ")
            error = False
        except ValueError:
            print("**Error** Número introducido no válido")
        except Exception:
            print("**Error** Número introducido no positivo o cero.")
    
    print (serieNum(num))

if __name__ == "__main__":
    main()