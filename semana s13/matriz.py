import os
class Matriz:
    def __init__(self,matriz,fila,col):
        self.matriz = matriz
        self.fila = fila
        self.col = col
        
    def ingresar(self):
        self.matriz = []
        for fila in range(self.fila):
            columnas = []
            os.system("cls")
            for col in range(self.col):
                valor = int(input("Fila[{}] Col[{}]: ".format(fila,col)))
                columnas.append(valor)
            self.matriz.append(columnas)
    
    def presentar(self):
        # os.system("cls")
        print("_______")
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                print("[{}]".format(self.matriz[fila][col]),end=" ")
            print()
        print("_______")
            
    def buscar(self,valor):
        enc = {}
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                if self.matriz[fila][col] == str(valor):
                    enc["Fila"] = fila
                    enc["Columna"] = col
                    break
            if enc: break
        return enc
    
    def buscarW(self,valor):
        enc = []
        fila = 0
        band = True
        while fila < len(self.matriz) and band:
            col = 0
            while col < len(self.matriz) and band:
                if self.matriz[fila][col] == valor:
                    enc["fila"] = fila
                    enc["col"] = col
                else: col += 1
            fila += 1
        return enc
    
    def sumar(self,matriz2):
        matrizSuma = []
        for fila in range(self.fila):
            columnas = []
            for col in range(self.col):
                valor = self.matriz[fila][col] + matriz2[fila][col]
                columnas.append(valor)
            matrizSuma.append(columnas)
        return matrizSuma
    
# numeros = [[10,20,30],[60,80,90],[25,35,45]]
numeros = []
mat1 = Matriz([],2,2)
mat2 = Matriz(numeros,2,2)
mat1.ingresar()
mat2.ingresar()
mat1.presentar()
mat2.presentar()
mat1.matriz = mat1.sumar(mat2.matriz)
mat1.presentar()
# mat.ingresar()
# print(mat.buscar(8))
# mat.presentar()
# resp = mat.buscar(35)
# if resp: print("El valor se encuentra en las siguientes coordenandas: ",resp)
# else: print("El valor ingresado no se encuentra en la matriz")