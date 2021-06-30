# En ejemplos anteriores, diseñamos un pseudocódigo para encontrar la
# superficie de un círculo para un radio cualquiera.
# El Flujograma que representa a dicho ejemplo es el siguiente:

def area():
    try:
        radio = float(input(("Escribe el radio del circulo: ")))
        print("El àrea del circulo es: {}".format(round((radio**2)*3.1415, 2)))
    except ValueError:
        return print("DATO INCORRECTO, INTENTELO NUEVAMENTE"), area()

if __name__ == '__main__':
    area()
