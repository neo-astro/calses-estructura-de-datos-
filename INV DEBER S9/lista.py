from menu import *
import os

class Lista(Menu):
    def __init__(self, tamano=3):
        self.lista = []
        self.longitud = 0
        self.size = tamano

    def menu_opciones(self):
        self.menu('Menu Lista','1: Agregar dato','2: Mostrar lista','3: Eliminar dato de la lista','4: Obtener valor','5: Salir al menu principal')

        opcion = input("Elija una opciòn: ")
        if opcion == '1':
            try:
                dato = int(input("Escribe una dato para agregarlo a tu lista: "))
                self.append(dato)
                input(Fore.GREEN + "\nCONTINUAR..."),os.system("cls"),self.menu_opciones()

            except ValueError:
                os.system("cls"), print("Debes ingresar solo valores numericos!"),self.menu_opciones()
        elif opcion == '2':
            self.mostrar()
            input(Fore.GREEN + "\nCONTINUAR..."), os.system("cls"),self.menu_opciones()

        elif opcion == '3':
            print(self.eliminar())
            input(Fore.GREEN + "\nCONTINUAR..."), os.system("cls"),self.menu_opciones()

        elif opcion == '4':
            print(self.obtener())
            input(Fore.GREEN + "\nCONTINUAR..."), os.system("cls"),self.menu_opciones()

        elif opcion == '5':
            pass
        
        else:
            os.system("cls"), print(Fore.RED + "Debes ingresar un numero con la opciòn que deseas!"), self.menu_opciones()



    def append(self, dato):
        if self.longitud < self.size:
            self.lista = self.lista + [dato]
            self.longitud += 1
        else:
            print(Fore.RED + "Lista llena")

    def obtener(self):
        if self.longitud != 0:
            self.mostrar()
            try:
                dato = int(input("Escriba la posicion del dato que desea obtener: "))
                if dato >= 0 and dato < self.longitud:
                    return "El dato obtenido es : " + str(self.lista[dato])
                else:
                    os.system("cls"), print(Fore.RED + "El valor esta fuera del rango !"), self.menu_opciones()

            except ValueError:
                os.system("cls"), print(Fore.RED + "Debes ingresar un numero con la posiciòn !")
        else:
            self.mostrar()

    def mostrar(self):
        if self.longitud != 0:
            print(Fore.WHITE + "valor" ,   "posiciòn")
            for pos, ele in enumerate(self.lista):
                print(Fore.GREEN + "[{}]        {}".format(ele, pos))
        else:
            print (Fore.RED + "La lista esta vacia!")

    def eliminar(self):
        if self.longitud == 0:
            self.mostrar()
        else:
            self.mostrar()
            try:
                elimninar_dato = int(input("Escribe la posicion del dato a eliminar: "))
                if elimninar_dato < 0 or elimninar_dato >= self.longitud:
                    return Fore.RED + "El rango esta fuera del alcance!"
                else:
                    self.longitud -= 1
                    self.lista = self.lista[:elimninar_dato] + self.lista[elimninar_dato + 1:]
                    return Fore.GREEN + f"Se actualizo la lista {self.lista}"

            except ValueError:
                return Fore.RED + "Debes intruducir una posiciòn"

    def empty(self):
        if self.longitud == 0:
            return True
        else:
            return False
