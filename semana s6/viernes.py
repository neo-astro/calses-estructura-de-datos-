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


    def ordenar_asc(self):
        for pos  in range(0, len(self.lista)):
            for sig in range(pos + 1 , len(self.lista)):
                if self.lista[pos] > self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos] = self.lista[sig]
                    self.lista[sig] = aux
    
       
    def ordenar_des(self):
        for pos,ele in enumerate(self.lista):       
        #    ele = 2 pos = 0
            for sig in range(pos +1 , len(self.lista)):
                if ele < self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]= self.lista[sig]
                    self.lista[sig]= aux
                    
# MODO FACIL------------------
    def primer_faci(self):
        print(self.lista[0])
        
    def ultimo_faci(self):
        print(self.lista[-1])

    def primer_eliminado_faci(self):
        primer = self.lista[0]
        self.lista = self.lista[1:]
        return primer
    
#  MODO ALT

    def primer_eliminado(self):
        primer = self.lista[0]
        list = []
        for i in range(1, len(self)):
            list.append(self.lista[i])
        self.lista = list
        return primer
    
    def ultimo_eliminado(self):
        ultimo = self.lista[-1]
        list = []
        for i in range(0, len(self.lista) - 1):
            list.append(self.lista[i])
        self.lista = list
        return ultimo
    # INSERTAR METODO 1
    def insertar(self,num ):
        self.ordenar_asc()
        auxlista = []
        for pos,ele in enumerate(self.lista):
            if num < ele:
                auxlista.append(num)
                break
            # else:
            #     auxlista.append(numero)
        self.lista = self.lista[0: pos] + auxlista + self.lista[pos:]
    # INSERTAR METODO 2
    def insertar2(self,num ):
        self.lista.append(num)
        self.ordenar_asc()


lista = [2, 3, 8, 10] 
# lista = [2, 3, 8, 10] = [2, 3, 5, 8, 10]
        #  0  1  2   3     0  1  2  3   4

# insertar = 5
ord1 = Ordenar(lista)
print(ord1.insertar(5))
print(ord1.lista)
print(ord1.insertar2(5))
print("CON METODO 2\n{}".format(ord1.lista))