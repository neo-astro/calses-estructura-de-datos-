from lista import *

class Pila(Lista):

    def __init__(self,tamano = 3):
        super().__init__(tamano)

    def mostrar_menu_pila(self):
        self.menu('Operaciones en pila', '1: Agregar dato','2: Mostrar lista','3: Eliminar dato de la lista','4: Obtener valor','5: Desacoplar pila "SHOW"','6: Eliminar dato por valor','7: Salir al menu principal')
        opcion = input("Elija una opciòn: ")

        if opcion == '1':
            try:
                dato = int(input("Escribe una dato para agregarlo a tu lista: "))
                self.append(dato)
                input(Fore.GREEN + "\nCONTINUAR..."),os.system("cls"),self.mostrar_menu_pila()

            except ValueError:
                os.system("cls"), print("Debes ingresar solo valores numericos!"),self.mostrar_menu_pila()
        elif opcion == '2':
            self.mostrar()
            input(Fore.GREEN + "\nCONTINUAR..."), os.system("cls"),self.mostrar_menu_pila()

        elif opcion == '3':
            print(self.eliminar())
            input(Fore.GREEN + "\nCONTINUAR..."), os.system("cls"),self.mostrar_menu_pila()

        elif opcion == '4':
            print(self.obtener())
            input(Fore.GREEN + "\nCONTINUAR..."), os.system("cls"),self.mostrar_menu_pila()

        elif opcion == '5':
            self.show()
            input(Fore.GREEN + "\nCONTINUAR..."), os.system("cls"),self.mostrar_menu_pila()
        
        elif opcion == '6':
            if self.empty() == True:
                try:
                    valor = int(input("Escribe el valor que queires eliminar de tu lista: "))
                    print(self.pop(valor))
                except ValueError:
                    print(Fore.RED + "Ingresa un valor numerico!")
            else:
              print (Fore.RED + "La lista esta vacia!")


            input(Fore.GREEN + "\nCONTINUAR..."), os.system("cls"),self.mostrar_menu_pila()


        elif opcion == '7':
            pass

        else:
            os.system("cls"), print(Fore.RED + "Debes ingresar un numero con la opciòn que deseas!"), self.mostrar_menu_pila()

    def show(self):
        if self.empty() == True:
            lista_reverse = [x for x in self.lista[-1::-1]]
            print("Los datos en pila son los siguientes: ")
            for ele in lista_reverse:
                print(Fore.GREEN + str(ele))
        else:
            print (Fore.RED + "La lista esta vacia!")

    def empty(self):
        if self.longitud != 0:
            return True
        else:
            return False

    def buscar(self,valor):
        for pos, elemento in enumerate(self.lista):
            if valor == elemento:
                return pos


    def pop(self,dato):
        if self.buscar(dato) == None:
            return Fore.RED + "El valor ingresado no se encuentra en la lista"

        elif self.buscar(dato) != None:
            posicion = self.buscar(dato)
            self.lista.pop(posicion)
            self.longitud -= 1
            return Fore.GREEN + f"La lista se actualizo: {self.lista}"
