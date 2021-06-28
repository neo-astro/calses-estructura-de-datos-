
# Aplicar los pasos de la metodología para la solución de un problema para leer un número entero N y
# calcular el resultado de la siguiente serie:
# 1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N. Resolveremos el problema utilizando bucle Repeat
# controlado por contador y usando banderas.

class Divisor:
    def run(self):
        try:
            numero = int(input("Escribe un numero entero:"))
            acu = 1
            con = 1
            alter = -1
            proceso = None
            while con != numero:
                con += 1
                alter *= -1
                proceso = (1/con)*alter
                acu -= proceso

            print("El resultado es: ", round(acu, 2))

        except ValueError:
            return print("DATO INCORRECTO INTENTALO NUEVAMENTE"), Divisor.run(self)


hacer = Divisor()
hacer.run()
