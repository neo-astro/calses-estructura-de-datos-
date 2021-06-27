class Calcular:
    
    def run(self):
        try:
            ht = int(input("Escriba la cantidad de horas trabajdas: "))
            ph = float(input("Escriba el valor a pagar por hora: "))
            if ht > 0 and ph > 0:
                if ht <= 40 > 0:
                    print("El total a pagar es :{}$".format(ph * ht))

                elif 40 < ht <= 48:
                    he1 = ph * 40 + ((ht - 40) * (2 * ph))
                    print("El total a pagar es :{}$".format(he1))

                elif ht > 48:
                    he2 = (ph * 40) + 8 * (2 * ph) + (ht - 48) * (3 * ph)
                    print("El total a pagar es :{}$".format(he2))
            return print("Ingrese correctamente los datos"), Calcular.run(self)

        except ValueError:
            print("Ingrese correctamente los datos"), Calcular.run(self)


ejecutar = Calcular()
ejecutar.run()
