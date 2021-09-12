class Lista:
    def __init__(self,listas):
        self.__lista = listas
        
    @property   
    def lista(self):
        return self.__lista
    
    def busquedaLineal(self,buscado):
        pos = 0
        enc = False
        lon = len(self.__lista)
        while pos < lon and enc == False:
            if self.__lista[pos]["Nombre"] == buscado:
                enc = True
            else:
                pos += 1
        if enc: return pos
        else: return -1
        
    def ordenar(self,orden):
        orden = orden.lower()
        if orden == "asc":
            for pos in range(0,len(self.__lista)):
                for sig in range(pos+1,len(self.__lista)):
                    if self.__lista[pos]["Nombre"] > self.__lista[sig]["Nombre"]:
                        aux = self.__lista[pos]
                        self.__lista[pos] = self.lista[sig]
                        self.__lista[sig] = aux
        else:
            for pos in range(0,len(self.__lista)):
                for sig in range(pos+1,len(self.__lista)):
                    if self.__lista[pos]["Nombre"] < self.__lista[sig]["Nombre"]:
                            aux = self.__lista[pos]
                            self.__lista[pos] = self.lista[sig]
                            self.__lista[sig] = aux
                
    
    def busquedaBinaria(self,buscado):
        self.ordenar("asc")
        fin = len(self.lista)
        inicio = 0
        enc = False
        while inicio < fin and enc == False:
            medio = (inicio+fin)//2
            if self.lista[medio]["Nombre"] == buscado: enc = True
            elif self.lista[medio]["Nombre"] > buscado: fin = medio-1
            else: inicio = medio+1
        if enc: return medio
        else: return -1

notas = [
    {"Nombre":"Andres","n1":35,"n2":60},
    {"Nombre":"Alex","n1":20,"n2":50},
    {"Nombre":"Daniela","n1":40,"n2":45},
    {"Nombre":"Jesus","n1":50,"n2":30},
    {"Nombre":"Angela","n1":45,"n2":28},
    {"Nombre":"Jimmy","n1":55,"n2":40}
]

bus = Lista(notas)
bus.lista.sort()
posicion = bus.busquedaLineal("Daniela")
if posicion != -1:
    print(bus.lista[posicion])
else:
    print("El nombre no se encuentra en la lista")
bus.ordenar()
print(bus.lista)