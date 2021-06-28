class Contar:
    def run(self):
        try:
            ht = int(input("Escriba la cantidad de horas trabajdas: "))
            ph = int(input("Escriba el valor a pagar por hora: "))
            if ht >= 0:
                if ht <= 40 > 0:
                    print("El total a pagar es :{}".format(ph * ht))

                elif 40 < ht <= 48:
                    he1 = ph * 40 + ((ht - 40) * (2 * ph))
                    print("El total a pagar es :{}".format(he1))

                elif ht > 48:
                    he2 = (ph * 40) + 8 * (2 * ph) + (ht - 48) * (3 * ph)
                    print("El total a pagar es :", he2)
        except ValueError:
            return print("Dato incorrecto"), Contar.run(self)


eje = Contar()
eje.run()



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


