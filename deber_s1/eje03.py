#Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, obtenga el resultado de la siguiente función:
# R = {100*v      sin num= 1
#      100^v      si num = 2
#      100/v      si num = 3
#       0}        si num es != 1,2,3s
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
