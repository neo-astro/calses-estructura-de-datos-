class Pila:
    def __init__(self, tamano=4):
        self.lista = []
        self.size = tamano
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
            top = self.lista[-1]
            self.lista = self.lista[:self.top]
            return top
        
    def long(self):
        return self.top
    
    def empty(self):
        if self.top == 0:
            return True
        else:
            return False 
    def show(self):
        for top in range(self.top -1,-1,-1):
            print([{self.lista[top]}])

obj = Pila(3)
obj.push(8)
obj.push(12)
obj.push(20)

obj.show()
print(obj.long())
obj.push(10)