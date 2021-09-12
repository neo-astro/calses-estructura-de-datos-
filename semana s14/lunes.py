class Lista:
    def __init__(self, listas):
        self.__lista = listas

    @property
    def lista(self):
        if self.__lista != None:
            return self.__lista
        else :
            return "La lista esta vacia"
    
    @lista.setter
    def lista(self, x):
        self.__lista =  x
        


    def busquedaLineal(self, buscado):
        pos = 0
        enc = False
        lon = len(self.__lista)

        while pos < lon and enc == False:
            if self.__lista[pos]["nombre"] == buscado:
                enc = True
            else:
                pos += 1

        if enc:return pos
        else:return -1


    def ordenar(self,ordenar):
        for pos in range(len(lista)):
            pass

    def busquedaBinaria(self, buscado):
        pass

listaNotas = [
    {"nombre":"adrian","nota1":20,"nota2":40},
    {"nombre":"pepe","nota1":20,"nota2":40},
    {"nombre":"jose","nota1":20,"nota2":40}
    ]

busqueda = Lista(listaNotas)
#print(busqueda.lista)
#busqueda.setter([4,5,7,89])
#print(busqueda.lista)
pos = busqueda.busquedaLineal("pepe")
if pos == -1:
    print("No exite el nombre")
else :
    print(bus.lista[pos])