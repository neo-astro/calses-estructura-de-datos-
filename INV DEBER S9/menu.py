from colorama import Fore


class Menu:
    def __init__(self):
        pass

    def menu(self, titulo, *args):
        print(Fore.WHITE + titulo.center(60, "="))
        for opciones in args:
            print(opciones)
