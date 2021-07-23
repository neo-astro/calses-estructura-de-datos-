# import os
class Menu():
    def __init__(self,titulo,opciones):
        self.titulo = titulo
        self.opciones = opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija opcion[1...{}] ".format(len(self.opciones)))
        return opc


men = Menu("Menu Listas", ["1) Calculadora", "2) Operaciones Numeros", "3) Tratamiento de Listas","4) Operaciones de Cadenas","5) Salir"])
opc = men.menu()

if opc == "1":
    men = Menu("Menu Calculadora", ["1) Suma","2) Resta","3) Multiplicacion","4) Division","5) Salir"])
    opc = men.menu()

elif opc == "2":
    men2 = Menu("Menu Numeros",["1) Perfecto","2) Primo","3) Salir"])
    opc = men2.menu()

# menu2 = Menu("Menu Listas", ["1) Recorrido","2) Buscar","3) Listas","4) Salir" ])
# menu2.menu

        # try:
        #     opcion = input("\nEliija una opcione: ")
        #     if opcion == 1:
        #         print("Calculadora")

        #     elif opcion ==2:
        #         print("Operaciones con nùmeros")

        #     elif opcion ==3:
        #         print("Tratamiento de Listas")

        #     elif opcion ==4:
        #         print("Operaciones con Cadenas")

        #     elif opcion ==5:
        #         print("Salir")

        #     else:
        #         raise ValueError("Seleciona una opciòn correcta")
        # except ValueError as f:
        #     return os.system("cls") + f,Menu.menu


