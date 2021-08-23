from lista import *
from pila import *
from menu import *
from os import *
from cola import *
import time

class Main(Menu):
    def main(self):
        self.menu('Operaciones con estructura de listas','1: Menu Lista', '2: Menu Pila', '3: Menu Cola' , '4: Salir')
        opcion = input("Elija una opciòn: ")

        if opcion == '1':
            os.system("cls")
            try:
                pregunta = input(
                    f"Por defecto la longitud de su lista sera de 3 elementos\n¿Desea cambiar la longiud? si/no: ").lower()

                if pregunta == "si":
                    size = int(input("Ingrese la longitud maxima de su lista: "))
                    print(Fore.GREEN + f"Su lista tendra un maximo de {size} elementos")
                    input(Fore.GREEN + "CONTINUAR...")
                    os.system("cls")

                    run_lista = Lista(size)
                    if run_lista.menu_opciones() != '5':
                        os.system("cls"), self.main()

                elif pregunta == "no":
                    print(Fore.GREEN + "Su lista tendra un maximo de 3 elemtos")
                    input(Fore.GREEN + "CONTINUAR...")
                    os.system("cls")
                    run_lista = Lista()
                    if run_lista.menu_opciones() != '5':
                        os.system("cls"), self.main()
                else:
                    os.system('cls'), print(Fore.RED + "Debes ingresar los datos correctamente, intentalo nuevamente"), self.main()

            except ValueError:
                os.system('cls'), print(Fore.RED + "Debes ingresar los datos correctamente, intentalo nuevamente"), self.main()

        elif opcion == '2':
            os.system("cls")
            try:
                pregunta = input(
                    f"Por defecto la longitud de su lista sera de 3 elementos\n¿Desea cambiar la longiud? si/no: ").lower()

                if pregunta == "si":
                    size = int(input("Ingrese la longitud maxima de su lista: "))
                    print(Fore.GREEN + f"Su lista tendra un maximo de {size} elementos")
                    input(Fore.GREEN + "CONTINUAR...")
                    os.system("cls")

                    run_pila = Pila(size)
                    if run_pila.mostrar_menu_pila() != '6':
                        os.system("cls"), self.main()

                elif pregunta == "no":
                    print(Fore.GREEN + "Su lista tendra un maximo de 3 elemtos")
                    input(Fore.GREEN + "CONTINUAR...")
                    os.system("cls")
                    run_pila = Pila()
                    if run_pila.mostrar_menu_pila() != '6':
                        os.system("cls"), self.main()
                else:
                    os.system('cls'), print(Fore.RED + "Debes ingresar los datos correctamente, intentalo nuevamente"), self.main()

            except ValueError:
                os.system('cls'), print(Fore.RED + "Debes ingresar los datos correctamente, intentalo nuevamente"), self.main()

        elif opcion == '3':
            os.system("cls")
            try:
                pregunta = input(
                    f"Por defecto la longitud de su lista sera de 3 elementos\n¿Desea cambiar la longiud? si/no: ").lower()

                if pregunta == "si":
                    size = int(input("Ingrese la longitud maxima de su lista: "))
                    print(Fore.GREEN + f"Su lista tendra un maximo de {size} elementos")
                    input(Fore.GREEN + "CONTINUAR...")
                    os.system("cls")

                    run_cola = Cola()
                    if run_cola.mostrar_opciones_cola() != '5':
                        os.system("cls"), self.main()

                elif pregunta == "no":
                    print(Fore.GREEN + "Su lista tendra un maximo de 3 elemtos")
                    input(Fore.GREEN + "CONTINUAR...")
                    os.system("cls")
                    run_cola = Cola()
                    if run_cola.mostrar_opciones_cola() != '5':
                        os.system("cls"), self.main()
                else:
                    os.system('cls'), print(Fore.RED + "Debes ingresar los datos correctamente, intentalo nuevamente"), self.main()

            except ValueError:
                os.system('cls'), print(Fore.RED + "Debes ingresar los datos correctamente, intentalo nuevamente"), self.main()

        elif opcion == '4':
            print(Fore.GREEN + "HASTA PRONTO".center(60,"-"))
            time.sleep(1)
            exit()
        else:
            os.system('cls'), print(Fore.RED + "Elige una opciòn correcta"), self.main()

run = Main()
run.main()
