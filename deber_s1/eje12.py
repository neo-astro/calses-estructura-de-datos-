# Diseñe un pseudocódigo para calcular la suma y producto de N números enteros
# utilizando un bucle controlado por centinela.

class Calcular:

    def run(self):
        try:
            acu = 1
            num = int(input("Ingrese un dato:"))
            numeros = []
            numeros.append(num)
            while num != 20:
                num = int(input("Ingrese otro dato:"))
                numeros.append(num)
            print("La suma de los datos es:", sum(numeros))

            for numero in numeros:
                acu *= numero
            print("La multiplicacion de los datos es:", acu)
        except ValueError:
            return print("Lo siento dato incorrecto"), Calcular.run(self)


eje = Calcular()
eje.run()
