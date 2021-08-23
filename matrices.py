class Matriz:
    def __init__(self,matriz):
        self.matriz = matriz
        
    def ingresar(self,dato):
        pass
    
    def presentar(self):
        for fila in range(len(numeros)):
            columna = numeros[fila]
            for col in range(len(columna)):
                print(columna[fila][col],end=" ")
            print()

numeros = [[10,20,30],[60,80,90],[25,35,45]]
mat = Matriz(numeros)
mat.presentar()
    
