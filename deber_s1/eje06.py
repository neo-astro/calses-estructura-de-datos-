class Mayor:
    def run(self):
        try:
            n1 = int(input("Escriba un numero entero: "))
            n2 = int(input("Escriba otro numero entero: "))
            n3 = int(input("Escriba otro numero entero: "))
            bi = [n1, n2, n3]
            print("El numero mayor es: ", max(bi))
        except ValueError:
            print("Dato incorrecto, ingrese un numero entero")
            return Mayor.run(self)


ejecutar = Mayor()
ejecutar.run()
