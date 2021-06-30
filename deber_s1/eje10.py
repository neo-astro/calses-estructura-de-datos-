#  Elabore pseudocódigo para el caso en que se desean escribir los números del 1 al 100
class EscribirHasta:
    def run(self):
        try:
            num = float(input("Escribir un numero del 1 hasta el 100:"))
            if num >= 1:
                while num >= 1:
                    num = float(input("Escribir un numero del 1 hasta el 100:"))
            else:
                return print("Lo siento tu numero no se encuentra en el rango del 1 a 100"), EscribirHasta.run(self)

        except ValueError:
            return print("Lo siento tu numero no se encuentra en el rango del 1 a 100"), EscribirHasta.run(self)


eje = EscribirHasta()
eje.run()
