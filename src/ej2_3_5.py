"""
Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"
"""

def pedirContraseña(msj: str) -> str:
    entrada = input(msj)
    contraseña = str(entrada)

    return contraseña

def main():
    try:
        contraseña = pedirContraseña("Introduzaca una contraseña: ")

        if contraseña != "contraseña":
            raise NameError("Incorrect Password!!") 
        else:
            print("Correct Password!!") 

    except NameError:
            print("Incorrect Password!!") 

if __name__ == "__main__":
    main()