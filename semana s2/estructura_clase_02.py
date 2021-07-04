class condiciones:

    def __init__(self, num1,num2,num3):
        self.numero1 = num1
        self.numero2 = num2
        numero = self.numero1 + self.numero2
        self.numero3 = numero

    def usoif(self):
        print(self.numero3)
        if self.numero1 == self.numero2:
            print("numero1={} =numero2{}:son iguales".format(self.numero1,self.numero2))
        elif self.numero1 ==self.numero3:
            print("numero1 y numero3 son iguales")
        else:
            print("numeros diferentes")

print("instancia de la clase")
cond1 = condiciones(100,250)
cond1.useif()
cond2 = condiciones()
print(cond2.numero3)
cond1.usoif()
cond2.usoif()
print("Gracias por su visita")


class ciclo:
    
    def __init__(self,numero=12):
        self.numero = numero
        self.numero2 = 0
        
    def usowhile(self):
        
        car = input("ingrese vocal")
        car = car.lower()
        
        
        while car not in  ("a","e","i","o","u"):
            car = input("Ingrese vocal").lower()
        print("FELICIDADES {} ES UNA VOCAL".format(car))    
            
            
ciclo_uno = ciclo()
ciclo_uno.usowhile()
print("Fin de un ciclo")
