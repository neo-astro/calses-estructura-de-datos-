class Fac:

    def run(self):
        try:
            numero = int(input("Ingrese un numero:"))
            acu = 1
            if numero > 0:
                for num in range(numero, 1, -1):
                    acu = acu*num
                print("El factorial de {} es igual a :{}".format(numero, acu))
            else:
                return print("EL DATO INGRESADO ES INCORRECTO"), Fac.run(self)

        except ValueError:
            print("EL DATO INGRESADO ES INCORRECTO")
            return Fac.run(self)


eje = Fac()
eje.run()
