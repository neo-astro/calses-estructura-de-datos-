# Aplicar las fases  para  la resolución de un problema para leer un vector de 20 números enteros y a continuación
# escribir en un vector A todos los números negativos y en un vector B todos los positivos o iguales a cero. Imprimir
# dichos vectores.

class Vectores:
    def run(self):
        vector = []
        vectorA = []
        vectorB = []
        try:

            while len(vector) != 4:
                numeros = float(input("Escribe otro numero:"))
                vector.append(numeros)

            for numero in vector:
                if numero < 0:
                    vectorA.append(numero)

                elif numero >= 0:
                    vectorB.append(numero)

            print("Los numeros negativos encontrados son: ", vectorA)
            print("Los numeros positivos encontrados son: ", vectorB)


        except ValueError:
            return print("Solo puedes escribir numeros!"), Vectores.run(self)


eje = Vectores()
eje.run()