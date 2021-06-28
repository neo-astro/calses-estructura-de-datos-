# Determinar si un número entero proporcionado por el usuario es primo.
# Un número primo es un entero que no tiene más divisores que él mismo y la unidad. Elaborar Pseudocódigo:
class Primo:
    def run(self):
        try:
            numero = int(input("Escribe un numero entero:"))
            if numero % 2 == 0 or numero % 3 == 0:
                print("Lo siento no es un numero primo")
            else:
                print("Felicidades es un numero primo")


        except ValueError:
            return print("DATO INCORRECTO INTENTALO NUEVAMENTE"), Primo.run(self)


hacer = Primo()
hacer.run()
