class Variables:
    def run(self):
        try:
            num = int(input("Escriba un numero entero: "))
            v = int(input("Escriba un valor entero: "))
            if num == 1:
                print("La respuesta es 100*{} = {}".format(v, 100*v))
            elif num == 2:
                print("La respuesta es 100^{} = {}".format(v, 100 ^ v))

            elif num == 3:
                print("La respuesta es 100/{} = {}".format(v, 100/v))

            else:
                print("La respuesta es 0")

        except ValueError:
            print("Dato incorrecto, ingrese un numero entero")
            return Variables.run(self)


ejecutar = Variables()
ejecutar.run()
