class Lista :
    def __init__(self, tamano=3):
        self.lista = []
        self.longitud = 0
        self.size = tamano

    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud +=1 
        else:
            print("Lista llena")
    
    def obtener(self):
        self.mostrar()
        dato = int(input("Escriba la posicion del dato que desea obtener: "))
        print("El dato obtenido es :", self.lista[dato])


    def mostrar(self):
        for pos, ele in enumerate(self.lista):
            print("[{}] {}".format(ele , pos))


    def eliminar(self):
        self.mostrar()
        elimninar_dato = int(input("Escribe la posicion del dato a eliminar: "))
        if elimninar_dato < 0 or elimninar_dato>= self.longitud:
            return None
        else:
            self.longitud -=1
            self.lista = self.lista[:elimninar_dato] + self.lista[elimninar_dato +1:]
            return print(f"Se actualizo la lista {self.lista}")
        
lista1 = Lista()
lista1.append( 54)
lista1.append("Edad")
lista1.append("Daniel")
# lista1.append("True")
# lista1.append("Milagro")
# lista1.obtener()
res = lista1.eliminar()

if res ==None:
    print("Por favor ingrese una posicion existente en la lista!")

