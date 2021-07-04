class Ordenar:
    
    def __init__(self, lista):
        self.lista = lista


    def recorrerElemto(self):
       for ele in self.lista:
           print(ele)

    def recorrerPosicion(self):
       for pos, ele in enumerate(self.lista):
           print(pos, ",", ele)

    def recorrerRange(self):
        for pos in range(len(self.lista)):
            print(pos, self.lista[pos])

    def buscar(self, buscado):
        enco = False

        for pos, ele in enumerate(self.lista):

            if ele == buscado:
                # print(len(self.lista),",", n)
                enco = True
                break
            return enco
        # return pos
        if enco == True:
            return pos
        else:
            return -1


   def ordenar(self):
       for pos in range (0 , len(self.lista)):
           for sig in range(pos + 1 , len(self.lista)):
               if self.lista[pos] >self.lista[sig]:
                   aux = self.lista[pos]
                   self.lista[pos] = self.lista[sig]
                   self.lista[sig] = aux
       # ordenada = []
       # while len(self.lista) != 0:
       #     ordenada.append(min(self.lista))



# ordenar = [5,3,2,6,10,9] = [2,3,5,6,9,10]
list = [20, 33, 10, 54, 86, 5]
eje = Ordenar(list)
# eje.recorrerElemto()
# eje.recorrerPosicion()
# eje.recorrerRange()
print(eje.buscar(5))
# buscado = 5
# resp = eje.buscar(buscado)
# if resp != -1:
#     print(("El Numero {}  se encuentra en la Posicion:({})".format(buscado, resp, eje.lista)))
# else:
#     print("El Numero {} no se encuenta en la lista".format(buscado, eje.lista))
