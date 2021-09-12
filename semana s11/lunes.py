class Cola:
    def __init__(self):
        self.lista = []
        self.size = 4
        self.top = 0
    
    def push(self,dato):
        if self.top < self.size:
            self.lista += [dato]
            self.top += 1
        else:
            print("La lista esta llena")
    
    def pop(self):
        if self.empty():
            return None
        else:
            top = self.lista[0]
            self.lista = self.lista[1:]
            self.top -= 1
            return top
    
    def longitud(self):
        return self.top
        
    def show(self):
        for top in range(0,self.top,1):
            print("[{}]",format(self.lista[top]))            
    
    def empty(self):
        if self.top == 0:
            return True
        else:
            return False
    
cola1 = Cola()
cola1.push(4)
cola1.push(8)
cola1.push(6)
cola1.push(1)
dato = cola1.pop()
if dato: print("El dato eliminado es: {}".format(dato))
else: print("La lista esta vacia")
dato = cola1.pop()
if dato: print("El dato eliminado es: {}".format(dato))
else: print("La lista esta vacia")
dato = cola1.pop()
if dato: print("El dato eliminado es: {}".format(dato))
else: print("La lista esta vacia")
dato = cola1.pop()
if dato: print("El dato eliminado es: {}".format(dato))
else: print("La lista esta vacia")